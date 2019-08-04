
function validateForm(e){
    var title=document.forms["addTitleForm"]["title"].value;
    if(title.length<5){
        alert("Com'on buddy you got to type more");
        return false;
    }
}