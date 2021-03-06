
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



/**
 * because the style is already done
 */
function hiddeFooter(){
    const footer = document.querySelector('footer');
    footer.classList.add('visible');
    footer.classList.remove('visible');
    footer.classList.add('oculto');
    //footer.style.display = 'none';
}



function changeToDark(){
    /*
    var cuerpo = document.getElementsByTagName('html');
    documnet.html.classList.toggle("darkmode");
    */
   var fondo = document.querySelector("html");
   fondo.classList.toggle('darkMode');

   var inputBUsqueda = document.getElementById('beachSearch');
   inputBUsqueda.classList.toggle('darkModeInput');

}



var showHidden = 0;
function showHiddeMenu(){
    const menuDesktop = document.getElementById('menu-mobile');
        if(showHidden === 0){
            menuDesktop.classList.remove('menu-empty');
            menuDesktop.classList.add('menu-mobile');
            showHidden = 1;
            console.log(showHiddeMenu)
            
        }else if(showHidden === 1){
            menuDesktop.classList.remove('menu-mobile');
            menuDesktop.classList.add('menu-empty');
            showHidden = 0;
            console.log(showHiddeMenu)
        }
    console.log(showHidden);
}

/*slideBar*/

var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  
  x[slideIndex-1].style.display = "block";  
 
}
