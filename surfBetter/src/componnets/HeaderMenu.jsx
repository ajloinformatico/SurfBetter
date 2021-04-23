/* eslint-disable jsx-a11y/anchor-is-valid */
import React, { useState } from "react";
import logoSurfBetterHeader from "../assets/img/common/logoSurfBetterHeader.png";
import {
    Link, useHistory,
} from 'react-router-dom'



/**
 * returns the common menu of the rest of the pages as a component
 * @returns {JSX.Element}: Main header of the app componnent
 * @constructor
 */
const HeaderMenu = () => {

    //Note: State used to display and hidde menu 
    const [menuNavState, setMenuNavState] = useState(false)
    //Note: DarkMode val TODO: SAVE ON MY API SERVICE
    const [darkModeState, setDarkModeState] = useState(false)

    const history = useHistory()

    /**
     * Change between darkMode and light mode
     * @param {event} e: Event
     */
    const changeToDark = (e) => {
        const htmlTarget = document.querySelector('html')
        darkModeState?htmlTarget.style.backgroundColor = '#00333d'
        :htmlTarget.style.backgroundColor = "white"
        setDarkModeState(!darkModeState)
    }
    
    /**
     * by menuNavState check if is displayed or not to change style
     * @param {Event} e: Event 
     */
    const showHideMenu = (e) => {
        const navMobileMenu = document.querySelector('#menu-mobile')
            if (!menuNavState) {
                navMobileMenu.classList.remove('menuMobileHidden')
                navMobileMenu.classList.add('menuMobileVisible')
                console.log('Show menu')
            } else {
                navMobileMenu.classList.remove('menuMobileVisible')
                navMobileMenu.classList.add('menuMobileHidden')
                console.log('Hidde menu')
            }
            //Note finally change state
            setMenuNavState(!menuNavState)
    }

    /**
     * search token on localstorage. Delete it and push history to home
     */
    const logOut = (e) => {
        localStorage.removeItem('REACT_TOKEN_AUTH_KEY');
        history.push("login");
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
                        <Link to="/options" title="go to Options" alt="link to login">
                            Options
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
                        <Link to="/resources" title="go to resources" alt="link to resources">
                            Resources
                        </Link>
                    </li>
                    <li>
                        <a  onClick={e => changeToDark(e)} title="Dark Mode bottom">
                            <i id="darkModeButton" className="fas fa-moon fa-2x"></i>
                        </a>
                    </li>
                    <li>
                        {/*TODO: FUNCTION TO DROP TOKEN AND THEN BACK MAIN*/}
                        <a onClick={e => logOut(e)}  title="Exit app" alt="link to login">
                            <i id="exitButtonHeader" className="fas fa-door-open fa-2x"></i>
                        </a>
                    </li>
                </ul>
            </nav>

            {/*Trigger burger menu by sass*/}
            <label id="trigger-mobile" className="trigger-mobile">
                <a  onClick={e => showHideMenu(e)}  title="Open menu" >
                    <i className="fas fa-bars fa-2x"></i>
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
                    <Link to="/options" title="go to Options" alt="link to login">
                        Options
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
                    <Link to="/resources" title="go to resources" alt="link to resources">
                        Resources
                    </Link>
                </li>

                <li>
                    <a onClick={e => changeToDark(e)} title="Dark Mode bottom">
                        Dark mode  <i id="darkModeButton" className="fas fa-moon"></i>
                    </a>
                </li>
                <li>
                    {/*TODO: FUNCTION TO DROP TOKEN AND THEN BACK MAIN*/}
                    <a onClick={e => logOut(e)} title="Exit app" alt="link to login">
                        Log out  <i id="exitButtonHeader" className="fas fa-door-open"></i>
                    </a>
                </li>
            </ul>
        </nav>
        </div>
    );
}


export default HeaderMenu;