// used to close all cards
function box_resume_onload_close(resume) {
    var elements = document.getElementsByClassName(resume);
    for (i = 0; i < elements.length; i++) {
        if (elements[i].id > 'explanation') {
            box_resume_onclick(elements[i].id);
        }
    }
}


// used to open/close the card with a click
function box_resume_onclick(resume) {
    var display = document.getElementById(resume).style.display;
    if (display == "none") {
        document.getElementById(resume).style.display = 'block';
    } else {
        document.getElementById(resume).style.display = 'none';
    }
}