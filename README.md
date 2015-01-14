# nasa
Assignment-2

OOP problem:

NASA has developed a squad of robotic rovers that are meant to do a geological survey of landing sites on any planet. These landing sites are always rectangular and consist of various minerals in varying amounts. The rovers are meant to extract mineral samples for analysis and report their findings back to Earth.

A rover's position is given by its x and y coordinates along with its 'heading' which is a letter representing one of the four compass points (N, S, E, W). The landing site is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means that the rover is at the bottom left corner and facing North.

To control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' make the rover turn 90 degrees left or right respectively. 'M' makes the rover move forward one grid position and maintain its current heading.

Assume that the square directly North from (x, y) is (x, y+1)

Each grid location on the landing site can consist of 2 to 5 types of minerals, each in a certain quantity. Initially, a grid location can have 3 to 10 units of whichever mineral is present at that location. For example, initially location (0, 0) might have 3 units of mineral M1, 10 units of M3 and 5 units of M5; and location (5, 7) might have 6 units of M2 and 4 units of M5.

Assume that there are only 5 types of minerals present across a landing site.

Each rover is pre-designed to be able to identify and analyze up to 3 types of minerals. For example, a rover may have been designed to analyze minerals M1 and M4 only. To perform this analysis, a rover will consume 1 unit of the relevant mineral from a grid location. 

Whenever a rover moves into a new grid location, it automatically extracts and performs analysis on the minerals at that location if they match the minerals the rover is looking for. If a certain mineral is depleted to 0 units at a grid location, future rovers will not be able to detect the mineral at that location.


Input

The first line of the input is the dimensions of the grid. You may proceed to generate a random distribution of minerals for the grid based on the criteria described above.

The remaining input is information pertaining to the rovers that have been deployed. Each rover has three lines of input. The first line gives the rover's initial position in the grid, the second line describes the minerals that the rover is looking for, and the last line is a series of instructions telling the rover how to explore the landing site. 

Sample input:
10 12 
1 2 N 
2 4 5
MMRMLMRMM
4 6 W
1 2
LMMRM

Each rover will be finished sequentially, ie. the second rover won't begin its exploration until the first rover has finished moving.


Output 

The first output should be the initial mineral distribution for each grid position.
Then, the output for each rover should be:
1. Its final coordinates and its heading.
2. A report of its mineral analysis for each mineral it was designed to investigate. If a rover is designed to look for minerals M1 and M5, it should report all the grid positions in which it encountered these minerals during its exploration.

You may format the output as you see fit.
