var Nasa = angular.module("Nasa", [], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    }
);

Nasa.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';    }
]);

Nasa.controller('NasaCtrl', function($scope, $http, $sce) {
    $scope.data = {
        user_id : '',
        rover_name : ''
    };
    $scope.whatever = ""
    tempstr = ""
    temp = angular.copy($scope.data)
    $scope.roversave = function() {
        console.log('User clicked post', this.data);
        $http.post('/rover/', this.data).success(function(){
            $scope.data = angular.copy(temp);
            $scope.roverForm.$setPristine();
        }) 
    };
    $scope.allrover = function(){
        $http.get('/rover/').
        success(function(data, status, headers, config) {
            angular.forEach(data, function(value,key){
                tempstr+="<p> User :   "+value.user_id+"  Rover name : "+ value.rover_name +"</p></br>"
            });
             $scope.whatever = $sce.trustAsHtml(tempstr);
        });
    };
});