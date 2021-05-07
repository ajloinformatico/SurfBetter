/* eslint-disable jsx-a11y/anchor-is-valid */
import React ,{useState} from 'react'
import logoSurfBetterHeader from "../../assets/img/common/logoSurfBetterHeader.png"

//login
import {login} from "../auth/auth.jsx"


/**
 * Subcomponent of login
 * @param {props} props: pass history by props to do redirect after login
 * @returns {JSX.Element}: return login modal component
 */
const LoginModal = (props) => {
    //inputsd sataes
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    /**
     * check inputs by onBlur() event
     * @param {event} e 
     */
    const checkInputs = e => {
        const input = e.target;
        input.classList.remove("errors");
        const mailReg = new RegExp(/^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i);

        // eslint-disable-next-line default-case
        switch(input.id) {
            case ("email") :
                if (!email.trim()) {
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " is empty";
                    setEmail("");
                    
                } else if (email.length > 130 || email.length < 4 || !mailReg.test(email)){
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " isn't valid";
                    setEmail("");
                }
                break;
            case ("password") :
                if (!password.trim()) {
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " is empty";
                    setPassword("")
                } else if ( password.length > 64 || password.length < 8){
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " isn't valid";
                    setPassword("");
                }
                break;
        }

    }

    /**
     * Send flask server name and password only if the before function pass
     * If response.token exists save token
     * @param {event} e 
     */
    const logIng = e => {
        e.preventDefault()
        
        
        //error
        const errorSpan = document.querySelector('.loginError')
        errorSpan.innerHTML = ""
        //get values from useStates
        const opts = {
            'email' : email,
            'password' : password
        }
        //execute fetch to flask server
        fetch ('/api/login', {
            method: 'POST',
            body: JSON.stringify(opts)
        }).then(response => response.json())
        .then(token => {
            if (token.access_token){
                login(token)
                console.log(token)
                //Note load profile
                props.history.push("/profile")
            }else {
                console.log("Autentication Error:\nMail or password not correct")
                errorSpan.innerHTML = "Mail or password not correct"
            }
        })
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
                    {/*Used for simple style*/ }
                    <div role="button">
                        <label title="exit" htmlFor={"btn-modal-log-in"}>
                            <a title="exit">
                                <i className={"fas fa-arrow-left fa-2x"}></i>
                            </a>
                        </label>
                    </div>
                </header>

                <div className={"contentModal"}>

                    <form id={"log-in-form"} action={'.'} onSubmit={e => logIng(e)}>
                        <fieldset className={"modalInputs"}>
                            <legend>Log in</legend>

                            <input type={"email"} id={"email"} name={"email"} title={"Please enter a valid email *"}
                               onChange={e => setEmail(e.target.value)} onBlur={e => checkInputs(e)}
                               size={30} aria-label={"email"} placeholder={"Email *"} required={true}/>

                            <input type={"password"} id={"password"} name={"password"} title={"Please enter your password"}
                               onChange={e => setPassword(e.target.value)} onBlur={e => checkInputs(e)}
                               aria-label={"password"} size={30}  placeholder={"password *"} required={true}/>

                            <span className="loginError" ></span>

                        </fieldset>
                        <fieldset className={"modalButtons"}>
                            <input  type={"submit"} className={"buttonBlue"} id={"log-in-button"} name={"log-in-button"} value={"Log in"}
                                    title={"Log in"} />

                            <input type={"button"} className={"buttonBlue"} id={"go-to-sign-in-button"} name={"go-to-sign-in-button"}
                                   value={"Sign in"} onClick={e => changeToSign()}/>
                        </fieldset>
                    </form>
                </div>
            </div>
    
        </section>

    )
}
export default LoginModal