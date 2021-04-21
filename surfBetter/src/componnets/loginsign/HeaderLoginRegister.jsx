/* eslint-disable jsx-a11y/anchor-is-valid */
import React from 'react'
import logoSurfBetterHeader from "../../assets/img/common/logoSurfBetterHeader.png";

/**
 * Load Header Component only for login and signin
 * @returns {JSX.Element}
 */
const HeaderLoginRegister = () => {

    return(
        <header id="header-login-register">
            <img alt="SurfBetter logo" src={logoSurfBetterHeader}/>
            {/*modal buttons by css*/}
            <div role="button">
                <label htmlFor="btn-modal-sign-in">
                    <a title="Sign in the app">Sign up</a>
                </label>
                <label  htmlFor={"btn-modal-log-in"}>
                    <a title="Log in the app">Log in</a>
                </label>
            </div>
           
        </header>
    )
}
export default HeaderLoginRegister


