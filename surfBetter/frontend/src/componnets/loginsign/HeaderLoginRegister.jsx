import React from 'react'
import logoSurfBetterHeader from "../../assets/img/common/logoSurfBetterHeader.png";


const HeaderLoginRegister = () => {

    return(
        <header>
            <img alt="SurfBetter logo" src={logoSurfBetterHeader}/>
            {/*modals buttons*/}
            <label htmlFor="btn_modal_sign_in">
                <a href="" title="Sign in the app">Sign up</a>
            </label>
            <label htmlFor={"btn_modal_log_in"}>
                <a href="" title="Log in the app">Log in</a>
            </label>
        </header>
    )
}
export default HeaderLoginRegister


