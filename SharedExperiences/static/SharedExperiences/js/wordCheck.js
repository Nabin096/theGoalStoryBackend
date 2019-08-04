function wordCheck(e){
    var submitbtn=document.getElementById('submit')
    if(e.id=='headerbox'){
        if(e.value.length==3){
            submitbtn.disabled=false;
        }
    }
    else if(e.id=='paragraphbox'){
        if(e.value.split(' ').length>3){
           submitbtn.disabled=false;
        }
    }

}
