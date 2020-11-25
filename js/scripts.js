
/**
 * Open a window by passing it an url
 * @param {String} url url to open 
 * @param {String} nombre name of the page
 * @param {String} tipo type of the page to open (its used to respect proportions)
 */
function openSecondWindow(url, nombre, tipo){
    debugger
    //Si el tipo es avisos legales
    if(tipo === "legalNoticesDesk"){
        var specs = "width=800,height=600,scrollbars=NO";    //XD specs    
    }else if(tipo === "signInDesk"){
        var specs = "width=653,height=722,scrollbars=NO";
    }
    window.open(url, nombre, specs);

}

/**
 * Just close a windows
 */
function closeWindow(){
    window.close();
}

/**
 * open singn up pop up and close the other
 * @param {String} url 
 */
function changeInUp(url){
    window.open(url, "Sign up", "width=653,height=831,scrollbars=NO");
    closeWindow();
}

/**
 * open sign in pop up and close the other
 * @param {String} url 
 */
function changeUpIn(url){
    window.open(url, "Sign in", "width=653,height=722,scrollbars=NO");
    //closeWindow();
}




function openSignIn(){
    //TODO onclick label button
}