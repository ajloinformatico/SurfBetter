import React, { useState } from "react";
import logoSurfBetterHeader from "../assets/img/common/logoSurfBetterHeader.png";
import {
    Link,
} from 'react-router-dom'



/**
 * returns the common menu of the rest of the pages as a component
 * @returns {JSX.Element}: Main header of the app componnent
 * @constructor
 */
const HeaderMenu = () => {

    //Note: State used to display and hidde menu 
    const [menuNavState, setMenuNavState] = useState(true)


    const changeToDark = () => {
        //TODO: MAKE FUNCTION
    }
    
    /**
     * by menuNavState check if is displayed or not to change style
     * @param {Event} e: Event 
     */
    const showHideMenu = (e) => {
        const navMobileMenu = document.querySelector('#menu-mobile')
            menuNavState?
                navMobileMenu.style.display = "none":navMobileMenu.style.display = "block"
    
            //Note finally change state
            setMenuNavState(!menuNavState)
    }


    return (
        <div>
            {/*div or section required because all must be under any parent target*/}
        <header>
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
                        <button onClick={changeToDark()} title="Dark Mode bottom">
                            <i className="fas fa-moon fa-2x"></i>
                        </button>
                    </li>
                    <li>
                        {/*TODO: FUNCTION TO DROP TOKEN AND THEN BACK MAIN*/}
                        <Link id="exitButtonHeader" to="/login" title="Exit app" alt="link to login">
                            <i class="fas fa-door-open fa-2x"></i>
                        </Link>
                    </li>
                </ul>
            </nav>

            {/*Trigger burger menu by sass*/}
            <label>
                <button className="trigger-mobile" onClick={e => showHideMenu(e)}  title="Open menu" >
                    <i class="fas fa-bars fa-2x"></i>
                </button>
            </label>
        </header>
        <nav id="menu-mobile" className="menuMobile">
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
                    <button onClick={changeToDark()} title="Dark Mode bottom">
                        <i class="fas fa-moon fa-2x"></i>
                    </button>
                </li>
                <li>
                    {/*TODO: FUNCTION TO DROP TOKEN AND THEN BACK MAIN*/}
                    <Link id="exitButtonHeader" to="/login" title="Exit app" alt="link to login">
                        <i class="fas fa-door-open fa-2x"></i>
                    </Link>
                </li>
            </ul>
        </nav>
        </div>
    );
}


export default HeaderMenu;