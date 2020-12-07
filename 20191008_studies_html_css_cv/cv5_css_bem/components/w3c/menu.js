function switchMenu(evt, key) {
    var i, tab__content, tablinks;
    tab__content = document.getElementsByClassName("tab__content");
    for (i = 0; i < tab__content.length; i++) {
        tab__content[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(key).style.display = "block";
    evt.currentTarget.className += " active";
}