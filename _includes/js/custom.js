
// Display the right image in the palette

function display (selected) {
  if(selected!='none'){
      var path = "<img src=\"/assets/images/pics/";
      var texttoshow = " ";
      texttoshow = path.concat(selected).concat(".png\" />");
      document.getElementById("thetext").innerHTML = texttoshow;
  }
}


