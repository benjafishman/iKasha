var app = angular.module('sefariaSearchApp', []);
app.controller('sefariaSearchApiCtrl', function($scope, $http) {

  $scope.chumash = [
        {book : "Genesis", chapters : 51},
        {book : "Exodus", chapters : 41},
        {book : "Leviticus", chapters :28 },
        {book : "Numbers", chapters : 37},
        {book : "Deuteronomy", chapters : 35},
    ];

 $scope.chumashPerakim = {
  'Genesis': 51,
  'Exodus': 41,
  'Leviticus': 28,
  'Numbers': 37,
  'Deuteronomy': 35
}


    $scope.selectedChumash = ""

    $scope.showSelectValue = function(mySelect) {
              console.log(mySelect);
              $scope.selectedChumash = mySelect;
              console.log($scope.chumashPerakim[mySelect]);
              var chapters = "";
                for (i = 1; i < $scope.chumashPerakim[mySelect]; i++) {
                          chapters += "<option>" + i + "</option>";
                        }
                        document.getElementById("select-chapter").innerHTML = chapters;
      }
    
  $scope.searchSefariaApi = function(){
    var selectedChapter= $('#select-chapter').find(":selected").text();
    var url = $scope.selectedChumash + "/" + selectedChapter;

    console.log(url);
    $http.get(url)
    .then(function (response) {$scope.pasukim = response.data;});
    console.log($scope.pasukim);
  };
  
});