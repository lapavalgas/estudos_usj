/*******************************************************************
    F U N C T I O N S
********************************************************************
/*******************************************************************
    Desktop: switchMenu() 
********************************************************************/

// this change the main content

function switchMenu(key) {
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
    closeMenu(); // used to close mobile menu anyway
}

/*******************************************************************
    Mobile: openMenu() / closeMenu()
********************************************************************/

// this open/close the mobile menu

function openMenu() {
    document.getElementById("mobile__menu").style.width = "100%";
    //document.getElementById("main").style.marginLeft = "650px";
}

function closeMenu() {
    document.getElementById("mobile__menu").style.width = "0";
    //document.getElementById("main").style.marginLeft = "0";
}

/*******************************************************************
    Any: academic and professional *detail collapse
********************************************************************/

// this open/close the academic and professional card 
function openCloseCard(cardId) {
    var display = document.getElementById(cardId).style.display;
    if (display == "none") {
        document.getElementById(cardId).style.display = 'block';
    } else {
        document.getElementById(cardId).style.display = 'none';
    }
}

// used to close all cards
function onloadCloseCard(cardClass) {
    var elements = document.getElementsByClassName('detail');
    for (i = 0; i < elements.length; i++) {
        if (elements[i].id > '0') {
            openCloseCard(elements[i].id);
        }
    }
}