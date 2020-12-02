function box_resume_explanation_show(explanation) {
    var display = document.getElementById(explanation).style.display;
    if (display == "none") {
        document.getElementById(explanation).style.display = 'block';
    } else {
        document.getElementById(explanation).style.display = 'none';
    }
}