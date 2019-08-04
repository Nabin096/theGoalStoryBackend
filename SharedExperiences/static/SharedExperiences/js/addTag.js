
function createTag(e){

    var tag=e.options[e.selectedIndex].value
    var header=document.getElementById('headerbox');
    var imagebox=document.getElementById('imagebox');
    var paragraphbox=document.getElementById('paragraphbox')
    if(tag=='Header'){
        header.style.visibility = "visible";
        imagebox.style.visibility = "hidden";
        paragraphbox.style.visibility = "hidden";

    }
    else if(tag=='Image'){
        header.style.visibility = "hidden";
        imagebox.style.visibility = "visible";
        paragraphbox.style.visibility = "hidden";
    }
    else if(tag=='Textarea'){
        header.style.visibility = "hidden";
        imagebox.style.visibility = "hidden";
        paragraphbox.style.visibility = "visible";
    }

    e.style.visibility="hidden";
}