

var chumashPerakim = {
  Genesis: [51],
  Exodus: [41],
  Leviticus: [28],
  Numbers: [37],
  Deuteronomy: [35]
}

var torahCategory = {
    Chumash: ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy"],
    Gemara: ["Juice", "Water", "Others"]
}

$(document).ready(function(){
	sefers = torahCategory.Chumash;
	for (s in sefers ) {
		var x = document.getElementById("select-sefer");
		var option = document.createElement("option");
		console.log(sefers[s]);
		option.text = sefers[s];
		x.add(option)
            }
            updateSefer('Genesis');
            $("#select-sefer").change(function(){
	        s = document.getElementById("select-sefer").value;
	        updateSefer(s);
	    });
});

function updateSefer(sefer) {
	var chapters = "";
	for (i = 1; i < chumashPerakim[sefer]; i++) {
	        	chapters += "<option>" + i + "</option>";
	        }
	        document.getElementById("select-chapter").innerHTML = chapters;
}

function call_sefaria(name, chapter) {
            var text = "";
            var base_url = "http://www.sefaria.org/api/texts/";
            var fullUrl = base_url + name + "." + chapter
            console.log(fullUrl);
            $.ajax({
              //url: "http://www.sefaria.org/api/texts/Genesis.1",
              url: fullUrl,
           
              // The name of the callback parameter, as specified by the YQL service
              jsonp: "callback",
           
              // Tell jQuery we're expecting JSONP
              dataType: "jsonp",
           
              // Work with the response
              success: function( response) {

                  console.log( response ); // server response  
                    
                  var str = JSON.stringify(response['he'], null, 2); // spacing level = 

                  var hebrew_text = JSON.stringify(response['he'], null, 2); 

                  var english_text = JSON.stringify(response['text'], null, 2); 

                  console.log( hebrew_text ); // server response

                  console.log( english_text ); // server response

                  //var commentary = JSON.stringify(response['commentary'], null, 2); 

                  //console.log( commentary ); // server response
                  /*
                  $scope.$apply(function () {
                  $scope.lastname = hebrew_text;
                });


                  $.grep( response, function( n, i ) {
                    //console.log(n.commentary.commentator==='Rashi');
                     });
                      */
                }

            });
};

$(document).ready(function(){
    $('#search').click(function() {
      console.log("hello");
      var textName = document.getElementById("select-sefer").value;
      var chapterName = document.getElementById("select-chapter").value;

      console.log(textName);
      console.log(chapterName);

      call_sefaria(textName, chapterName);
    });
  });