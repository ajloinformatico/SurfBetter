import React ,{useState} from 'react'
import logoSurfBetterHeader from "../../assets/img/common/logoSurfBetterHeader.png"

const LoginModal = () => {

    //TODO: useState elements
    const checkInputs = e => {
        alert("if all correct send to flask")
    }

    const changeToSign = () => {
        document.querySelector('#btn-modal-log-in').checked = false;
        document.querySelector('#btn-modal-sign-in').checked = true;
    }

    return (
        <section className={"modalLogin"}>
            <div className={"container"}>
                <header>
                    <img srcSet={logoSurfBetterHeader} alt={"logo SurfBetter"} title={"SurfBetter logo"}/>
                    <label htmlFor={"btn-modal-log-in"}>
                        <a title="exit modal">
                            <i className={"fas fa-arrow-left fa-2x"}></i>
                        </a>
                    </label>
                </header>

                <div className={"contentModal"}>

                    <form id={"log-in-form"} action={'.'} onSubmit={e => checkInputs(e)}>
                        <fieldset className={"modalInputs"}>
                            <legend>Log in</legend>

                            <input type={"email"} id={"email"} name={"email"} title={"Please enter your email *"} maxLength={60}
                                   size={30} aria-label={"email"} placeholder={"Email *"} required={true}/>

                            <input type={"password"} id={"password"} name={"password"} title={"Please enter your password"}
                                   aria-label={"password"} size={30} minLength={8} maxLength={15} placeholder={"password *"}
                                   required={true}/>
                        </fieldset>
                        <fieldset className={"modalButtons"}>
                            <input className={"buttonBlue"} type={"submit"} id={"log-in-button"} name={"log-in-button"} value={"Log in"}
                                    title={"Log in"} />

                            <input className={"buttonBlue"} type={"button"} id={"go-to-sign-in-button"} name={"go-to-sign-in-button"}
                                   value={"Sign in"} onClick={e => changeToSign()}/>
                        </fieldset>
                    </form>
                </div>
            </div>
        </section>

    )
}
export default LoginModal