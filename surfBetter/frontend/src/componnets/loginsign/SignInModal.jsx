import React ,{useState} from 'react'
import logoSurfBetterHeader from "../../assets/img/common/logoSurfBetterHeader.png";

const SignInModal = () => {

    const [userNameValue, setUserNameValue] = useState("")



    const checkInput = (e) => {
        e.preventDefault()
        const form = document.getElementById("sign-in-form")
        alert(form['user_name'].value)
    }

    return (
        <div className={"container"}>

            <header>
                <img srcSet={logoSurfBetterHeader} alt="logo SurfBetter"
                 title="logo surfBetter"/>
                <label htmlFor={"btn_modal_sign_in"}>
                    <a href={""} title="exit modal" className={"btnExitModal"}>
                        <i className={"fas fa-arrow-left fa-2x"}></i>
                    </a>
                </label>
            </header>

            <div className={"contentModal"}>
                {/*TODO: ROUTE ON FLASK*/}
                {/*All inputs are checked on input and on js*/}
                <form id={"sign-in-form"} onSubmit={e => checkInput(e)} autoComplete={'on'}>
                    <input type={"text"} id={"user_name"} name={"user_name"} minLength={2} maxLength={64}
                           aria-label={"user_name"}
                           size={30} title={"Please input your name"} placeholder={"User Name"} required={true}
                           pattern={"[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]{2,64}"}/>

                    <input type={"email"} id={"email"} name={"email"} title={"Please enter your email *"} maxLength={60}
                           size={30} aria-label={"email"} placeholder={"Email *"} required={true}/>

                    <input type={"password"} id={"password"} name={"password"} title={"Please enter your password"}
                           aria-label={"password"} size={30} minLength={8} maxLength={15} placeholder={"password *"}
                           required={true}/>

                    <input type={"password"} id={"re-password"} name={"re-password"} title={"Please repeat your password"}
                           aria-label={"re-password"} size={30} minLength={8} maxLength={15} placeholder={"repeat password *"}
                           required={true}/>

                    <input type={"submit"} id={"sign-in-button"} name={"sign-in-button"}
                           title={"Sign in"}/>

                    <input type={"submit"} id={"log-in-button"} name={"log-in-button"}
                           title={"Log in"}/>
                </form>
            </div>
        </div>
    )
}

export default SignInModal