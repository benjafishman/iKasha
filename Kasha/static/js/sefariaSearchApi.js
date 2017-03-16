var app = angular.module('sefariaSearchApp', []);
app.controller('sefariaSearchApiCtrl', function($scope, $http) {

  $scope.chumash = [
        {en_book : "Genesis", chapters : 51},
        {en_book : "Exodus", chapters : 41},
        {en_book : "Leviticus", chapters :28 },
        {en_book : "Numbers", chapters : 37},
        {en_book : "Deuteronomy", chapters : 35},
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
              };
                        
            document.getElementById("select-chapter").innerHTML = chapters;
            $("#select-chapter").val("1");
            $scope.selectedChapter = 1;

      }
    
  $scope.searchSefariaApi = function(){
    $scope.selectedChapter = $('#select-chapter').find(":selected").text();
    var url = $scope.selectedChumash + "/" + $scope.selectedChapter;

    console.log(url);
    $http.get(url)
    .then(function (response) {$scope.pasukim = response.data;});
    console.log($scope.pasukim);
  };
  
});