from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import random


class Grid(models.Model):
    x_len = models.IntegerField()
    y_len = models.IntegerField()


class Mineral(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class SubGrid(models.Model):
    g_id = models.ForeignKey('Grid')
    pos_x = models.IntegerField()
    pos_y = models.IntegerField()

    def __unicode__(self):
        return "Grid = " + str(self.g_id.id) + "  x_pos = " + \
            str(self.pos_x) + "  y_pos = " + str(self.pos_y)


class MineralDis(models.Model):
    sg_id = models.ForeignKey('SubGrid')
    mi_id = models.ForeignKey('Mineral')
    quantity = models.IntegerField()


class Rover(models.Model):
    user_id = models.ForeignKey(User)
    sg_id = models.ForeignKey('SubGrid')
    dirn = models.CharField(max_length=1)

    def __unicode__(self):
        return str(self.id)

    def process_instruction(self, inst):
        for i in range(len(inst)):
            self.move(inst[i])

    def move(self, dirn):
        if dirn == 'R' or dirn == 'L':
            self.change_dirn(dirn)
        else:
            self.move_a_step()

    def change_dirn(self, dirn):
        direction = "NESW"
        if dirn == 'R':
            self.dirn = direction[(direction.find(self.dirn) + 1) % 4]
            self.save()
        else:
            self.dirn = direction[(direction.find(self.dirn) - 1)]
            self.save()

    def increment_y(self):
        """docstring for increment_y"""
        sg = self.sg_id
        temp = sg.pos_y + 1
        sg = SubGrid.objects.filter(g_id=sg.g_id, pos_x=sg.pos_x, pos_y=temp)
        self.sg_id = sg[0]
        self.save()

    def decrement_y(self):
        """docstring for decrement_y"""
        sg = self.sg_id
        temp = sg.pos_y - 1
        sg = SubGrid.objects.filter(g_id=sg.g_id, pos_x=sg.pos_x, pos_y=temp)
        self.sg_id = sg[0]
        self.save()

    def increment_x(self):
        """docstring for increment_x"""
        sg = self.sg_id
        temp = sg.pos_x + 1
        sg = SubGrid.objects.filter(g_id=sg.g_id, pos_x=temp, pos_y=sg.pos_y)
        self.sg_id = sg[0]
        self.save()

    def decrement_x(self):
        """docstring for decrement_x"""
        sg = self.sg_id
        temp = sg.pos_x - 1
        sg = SubGrid.objects.filter(g_id=sg.g_id, pos_x=temp, pos_y=sg.pos_y)
        self.sg_id = sg[0]
        self.save()

    def move_a_step(self):
        """docstring for move_a_step"""
        if self.dirn == 'N':
            self.increment_y()
        elif self.dirn == 'E':
            self.increment_x()
        elif self.dirn == 'S':
            self.decrement_y()
        else:
            self.decrement_x()
        self.investigate()

    def investigate(self):
        r_sen = RoverSen.objects.filter(r_id=self.id)
        for i in r_sen:
            temp_r = i.r_id.id
            temp_m = i.m_id.id
            rovr = Rover.objects.get(id=temp_r)
            mnrl = Mineral.objects.get(id=temp_m)
            mn_dis = MineralDis.objects.filter(sg_id=rovr.sg_id, mi_id=mnrl)[0]
            if mn_dis.quantity > 0:
                mn_dis.quantity -= 1
                mn_dis.save()


class RoverSen(models.Model):
    r_id = models.ForeignKey('Rover')
    m_id = models.ForeignKey('Mineral')

    class Meta:
        unique_together = ("r_id", "m_id")


def add_subgrid(sender, instance, **kwargs):
    for i in range(instance.x_len):
        for j in range(instance.y_len):
            temporary = SubGrid(g_id=instance, pos_x=i, pos_y=j)
            temporary.save()


def add_mineral(sender, instance, **kwargs):
    tot_mineral = Mineral.objects.all()
    for i in range(tot_mineral.count()):
        quan = random.randint(3, 10)
        temporary = MineralDis(
            sg_id=instance, mi_id=tot_mineral[i], quantity=quan)
        temporary.save()

post_save.connect(add_subgrid, sender=Grid)
post_save.connect(add_mineral, sender=SubGrid)
