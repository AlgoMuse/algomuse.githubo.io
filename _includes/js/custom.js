
// Display the right image in the palette


function display (selected) {
  if(selected!='none'){
      var path = "<img src=\"/assets/images/pics/";
      var texttoshow = " ";
      texttoshow = path.concat(selected).concat(".png\" />");
      document.getElementById("thetext").innerHTML = texttoshow;
  }
}



function markdisplay (selected) {
  if(selected!='none'){
      var path = "<img src=\"/assets/images/mock_test/";
      var title = "<h2>Submission spotlight</h2><h4><large>";
      title = title.concat ( selected.replace("/",": ").replaceAll("_"," ").replace("/", "").replace(".jpg","").concat("</large></h4>") )
      title = title.replace("PartA","Part A")
      var texttoshow = " ";
      texttoshow = path.concat(selected).concat(".jpg\" />");
      document.getElementById("themarktext").innerHTML = title.concat(texttoshow);
  }
}



