/* eslint-disable jsx-a11y/anchor-is-valid */
import React ,{useState} from 'react'
import logoSurfBetterHeader from "../../assets/img/common/logoSurfBetterHeader.png";
import { login } from '../auth/auth';

/**
 * 
 * @param {props} props: pass history by props to do redirect after signin
 * @returns {JSX.Element}; signin modal
 */
const SignInModal = (props) => {

    //Note: inputs states
    const [name, setName] = useState("")
    const [surname, setSurname] = useState("")
    const [nick, setNick] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [repeatPassword, setRepeatPassword] = useState("")

    //Note: history get history by the props
    const history = props.history

    /**
     * Check if string is correct by checking legth and not numbers
     * @param cadena
     * @param min
     * @param max
     * @returns {boolean}
     */
    const checkStrings = (cadena,min,max) => {
        let flag = false
        if (cadena.length > min && cadena.length < max){
            cadena.split("").forEach(element => {
                if (!isNaN(element)) {
                    console.log("i have found a number");
                    flag = true;
                }
            })
        } else {
            flag = true
        }
        return !flag;
    }
    /**
     * By getting event in each onBlur event checks that the inputs are ok
     * @param {event} e: input event
     */
    const checkInputs = (e) => {
        const input = e.target;
        input.classList.remove("errors");
        const mailReg = new RegExp(/^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i);
        
        switch (input.id) {
            case ("name") : 
                if(!name.trim()){
                    input.classList.add("errors");
                    input.placeholder = input.id + " is empty";

                } else if (!checkStrings(name, 2, 64)) {
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " isn't valid";
                    setName("");
                }
                break;
            case ("surname") :
                if (!surname.trim()) {
                    input.classList.add("errors");
                    input.placeholder = input.id + " is empty";
                } else if (!checkStrings(surname, 2, 64)) {
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " isn't valid";
                    setSurname("");
                }
                break;
            case ("nick") :
                if (!nick.trim()) {
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " is empty";
                    setNick("");
                } else if (!checkStrings(nick, 2, 30)){
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " isn't valid";
                    setNick("");
                }
                break;
            case ("email_login") :
                if (!email.trim()) {
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " is empty";
                    setEmail("");
                }
                else if (email.length > 130 || email.length < 4 || !mailReg.test(email)) {
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " isn't valid";
                    setEmail("");
                }
                break;
            case ("password_login") : 
                if (!password.trim()) {
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " is empty";
                    setPassword("")
                } else if ( password.length > 64 || password.length < 8){
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " isn't valid";
                    setPassword("")
                }
                break;
            case ("re-password") : 
                if (!repeatPassword.trim()) {
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " is empty";
                    setRepeatPassword("")
                } else if (repeatPassword !== document.getElementById("password_login").value) {
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = "Passwords do not match";
                    setRepeatPassword("")
                }
                break;
            default :
                break;
        }
    }

    /**
     * Send flask server new user data only if the before function pass
     * If response.token exists save token
     * @param {event} e 
     */
    const signUp = e => {
        e.preventDefault();
        const errorSpan = document.querySelector('.errorForms')
        errorSpan.innerHTML = ""
        //get values from useStates
        const opts = {
            'email' : email,
            'name' : name,
            'surname' : surname,
            // Need eslint-disabled because need key for login and register
            // eslint-disable-next-line no-dupe-keys
            'email' : email,
            'nick' : nick,
            'password' : password
        }
        console.log(opts)
        //execute fetch to flask server
        fetch('/api/signin', {
            method: 'POST',
            body: JSON.stringify(opts)
        }).then(response => response.json())
        .then(token => {
            if (token.access_token) {
                login(token)
                history.replace("/profile")
            } else {
                console.log(token.signin_error)
                errorSpan.innerHTML = token.signin_error
            }
        })
    }

    /**
     * Change to Log in form
     */
    const changeToLogin = () => {
        document.querySelector('#btn-modal-sign-in').checked = false;
        document.querySelector('#btn-modal-log-in').checked = true;
    }

    return (
        <section className={"modalSignIn"}>
        <div className={"container"}>
            <header>
                <img srcSet={logoSurfBetterHeader} alt="logo SurfBetter"
                 title="SurfBetter logo"/>
                <label htmlFor={"btn-modal-sign-in"}>
                    <a title="exit">
                        <i className={"fas fa-arrow-left fa-2x"}></i>
                    </a>
                </label>
            </header>

            <div className={"contentModal"}>
                {/*All inputs are checked on js checkinputs()*/}
                <form id={"sign-in-form"} action={'.'} onSubmit={e => signUp(e)} autoComplete={'on'}>
                    <fieldset className={"modalInputs"}>
                        <legend>Sign in</legend>
                        <input type={"text"} id={"name"} name={"name"} aria-label={"name"}
                               onChange={e => setName(e.target.value)} onBlur={e => checkInputs(e)}
                               size={30} title={"Please input a valid name"} placeholder={"User Name *"} required={true}/>

                        <input type={"text"} id={"surname"} name={"surname"} aria-label={"surname"}
                               onChange={e => setSurname(e.target.value)} onBlur={e => checkInputs(e)}
                               size={30} title={"Please input a valid surname"} placeholder={"User Surname"} required={true}/>

                        <input type={"text"} id={"nick"} name={"nick"} aria-label={"nick"}
                               onChange={e => setNick(e.target.value)} onBlur={e => checkInputs(e)}
                               size={30} title={"Please input a valid nick"} placeholder={"User Nick *"} required={true}/>

                        <input type={"email"} id={"email_login"} name={"email"} title={"Please enter a valid email *"}
                               onChange={e => setEmail(e.target.value)} onBlur={e => checkInputs(e)}
                               size={30} aria-label={"email"} placeholder={"Email *"} required={true}/>

                        <input type={"password"} id={"password_login"} name={"password"} title={"Please enter your password"}
                               onChange={e => setPassword(e.target.value)} onBlur={e => checkInputs(e)}
                               aria-label={"password"} size={30}  placeholder={"password *"} required={true}/>

                        <input type={"password"} id={"re-password"} name={"re-password"} title={"Please repeat your password"}
                               onChange={e => setRepeatPassword(e.target.value)} onBlur={e => checkInputs(e)}
                               aria-label={"re-password"} size={30} placeholder={"repeat password *"} required={true}/>

                        <label>
                            <input type={"checkbox"} id={"check"} name={"check"} required={true}/>
                            I allow the storage of my data
                        </label>
                        
                        <span className="errorForms"></span>

                    </fieldset>
                    <fieldset className={"modalButtons"}>
                        <input type={"submit"} className={"buttonBlue"} id={"sign-in-button"} name={"sign-in-button"}
                               title={"Sign in"} value={"Sign in"}/>

                        <input type={"button"} className={"buttonBlue"} id={"go-to-log-in-button"} name={"go-to-log-in-button"}
                               title={"Log in"} onClick={e => changeToLogin()} value={"Log in"}/>
                    </fieldset>

                </form>
            </div>
        </div>
        </section>
    )
}

export default SignInModal