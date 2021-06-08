/* eslint-disable jsx-a11y/anchor-is-valid */
import React, {useState} from "react";
import logoSurfBetterHeader from "../assets/img/common/logoSurfBetterHeader.png";

//Link for menu
import {Link} from 'react-router-dom';

//Sweet Alert to custom alert
import swal from 'sweetalert';
import {changeDarkMode} from "../Utils";


/**
 * returns the common menu of the rest of the pages as a component
 * @returns {JSX.Element}: Main header of the app componnent
 */
const HeaderMenu = () => {


    //Note: State used to display and hidde menu
    const [menuNavState, setMenuNavState] = useState(false);
    //Note: DarkMode val TODO: SAVE ON MY API SERVICE
    const [darkModeState, setDarkModeState] = useState(null);


    /**
     * Change between darkMode and light mode
     * @param {event} e: Event
     */
    const changeToDark = () => {
        const htmlTarget = document.querySelector('html');
        //Set localStorageItem
        darkModeState?localStorage.setItem("theme","darkMode"):localStorage.setItem("theme","lightMode")
        //ChangeTheme
        changeDarkMode(htmlTarget,darkModeState)
        //Set State
        setDarkModeState(!darkModeState)
    }
    
    /**
     * by menuNavState check if is displayed or not to change style
     * @param {Event} e: Event 
     */
    const showHideMenu = (e) => {
        const navMobileMenu = document.querySelector('#menu-mobile')
            if (!menuNavState) {
                navMobileMenu.classList.remove('menuMobileHidden');
                navMobileMenu.classList.add('menuMobileVisible');
            } else {
                navMobileMenu.classList.remove('menuMobileVisible')
                navMobileMenu.classList.add('menuMobileHidden')
            }
            //Note finally change state
            setMenuNavState(!menuNavState)
    }

    /** search token on localstorage. Delete it and push history to home */
    const logOut = () => {
        swal({
            title: "Log out",
            text: "Are you shure you want to log out?",
            icon: "warning",
            buttons: true,
            dangerMode: true,
        })
        .then((logout) => {
            if (logout) {
                swal("See you next time surfer",{
                        icon: "success",
                })
                .then( async () => {
                    localStorage.removeItem('REACT_TOKEN_AUTH_KEY')
                    window.location.replace("/login")
                })
            } else  {
                swal("You will not regret 😄")
            }
        })
    }

    return (
        <div>
            {/*div or section required because all must be under any parent target*/}
        <header id="header-common-app">
            <img src={logoSurfBetterHeader} alt="surfbetter logo" title="surf better logo" width="330" height="120"/>
            <nav className="navDesk">
                <ul>
                    <li>
                        <Link to="/contact" title="Go to contact" alt="Link to contact">
                            Contact
                        </Link>
                    </li>
                    <li>
                        <Link to="/" title="go to Beaches" alt="link to beaches">
                            Beaches
                        </Link>
                    </li>
                    <li>
                        <Link to="profile" title="go to Profile" alt="link to profile">
                            Profile
                        </Link>
                    </li>
                    <li>
                        <Link to="/map" title="go to resources" alt="link to resources">
                            Map
                        </Link>
                    </li>
                    <li>
                        <a  onClick={() => changeToDark()} title="Dark Mode bottom">
                            <i id="darkModeButton" className={
                                //Change icon in fun of the darkMode
                                darkModeState!==false?("fas fa-moon fa-2x"):("fas fa-sun fa-2x")
                            }/>      
                        </a>
                    </li>
                    <li>
                        <a onClick={() => logOut()}  title="Exit app" alt="link to login">
                            <i id="exitButtonHeader" className="fas fa-door-open fa-2x"/>
                        </a>
                    </li>
                </ul>
            </nav>

            {/*Trigger burger menu by sass*/}
            <label id="trigger-mobile" className="trigger-mobile">
                <a  onClick={e => showHideMenu(e)}  title="Open menu" >
                    <i className="fas fa-bars fa-2x"/>
                </a>
            </label>
        </header>
        <nav id="menu-mobile" className="menuMobileHidden">
            <ul>
                <li>
                    <Link to="/contact" alt="link to contact" title="go to Contact">
                        Contact
                    </Link>
                </li>
                <li>
                    <Link to="/" title="go to Beaches" alt="link to beaches">
                        Beaches
                    </Link>
                </li>
                <li>
                    <Link to="/profile" title="go to Profile" alt="link to profile">
                        Profile
                    </Link>
                </li>
                <li>
                    <Link to="/map" title="go to resources" alt="link to resources">
                        Maps
                    </Link>
                </li>

                <li>
                    <a onClick={() => changeToDark()} title="Dark Mode bottom">
                        {!darkModeState?("Light Mode"):("Dark Mode")}
                        <i id="darkModeButton" className={
                            darkModeState?("fas fa-moon"):("fas fa-sun")
                        }/>
                    </a>
                </li>
                <li>
                    {/*TODO: FUNCTION TO DROP TOKEN AND THEN BACK MAIN*/}
                    <a onClick={e => logOut(e)} title="Exit app" alt="link to login">
                        Log out  <i id="exitButtonHeader" className="fas fa-door-open"/>
                    </a>
                </li>
            </ul>
        </nav>
        </div>
    );
}


export default HeaderMenu;