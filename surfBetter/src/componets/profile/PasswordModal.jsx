/* eslint-disable jsx-a11y/anchor-has-content */
/* eslint-disable react/jsx-no-duplicate-props */
/* eslint-disable jsx-a11y/anchor-is-valid */
import React, {useState} from 'react'
import logoSurfBetterHeader from "../../assets/img/common/logoSurfBetterHeader.png"



//TODO MODAL TO CHANGE PASSWORD
/* *
 * 
 * @param props: user state
 * @returns {JSX.Component}
 */
const PasswordModal = (props) => {




    /*Fields states*/
    const [oldPassword, setOldPassword] = useState("")
    const [newPasword, setNewPassword] = useState("")

    /**
     * Check password inputs
     * @param {State} state 
     * @param {target} input 
     * @returns 
     */
    const checkCommonsPassword = (state, input) =>{
        let errors = false
        if (!state.trim()) {
            input.placeholder = input.id + " is empty"
            errors = true
        } else if (state.length > 64 || state.length < 8){
            input.placeholder = input.id + " is not valid"
            errors = true
        }
        if (!errors) 
            return false

        input.classList.add("erros")
        input.value = ""
        return true
    }
    /**
     * 
     * @param {Event} e: todo refator 
     */
    const checkInputs = (e) => {
        const input = e.target;
        console.log(input)
        input.classList.remove("errors");
        switch (input.id){
            case  "old-password":
                checkCommonsPassword(oldPassword, input)&&setOldPassword("")
                return true;
            case "new-password":
                checkInputs(newPasword, input)&&setNewPassword("")
                return true;
            default :
                break;
        }
        if (oldPassword !== newPasword)
                return true;
                
        input.classList.add("errors")
        input.value = ""
        input.placeholder = "Passwords can not be the same"
        setOldPassword("")
        setNewPassword("")
        return true;
    }


    /**
    * Execute update
    * @param {evenet} e 
    */
    const putUpdatePassword = async e => {
        alert("update")
    }

    const updatePassword = (e) => {
        e.preventDefault()
        window.confirm("Are yo shure you want update\nYour current password")&&
        putUpdatePassword(e)
    }

    const closePasswordResset = () => {
        document.getElementById('password-update-modal').checked = false
        document.getElementById('user-options-modal').checked = true    
    
    }

    return (
        <section className={"modalPassword"}>
            <div className={"container"}>
                <header>
                    <img srcSet={logoSurfBetterHeader} alt={"surfbetter logo"}/>
                    <a onClick={() => closePasswordResset()} title="exit" className={"fas fa-arrow-left fa-2x"} alt="exit" title="exit"/>        
                </header>
                <div className={"contentModal"}>
                    <h2>Update password</h2>
                    <form id="updatePassword" action={"."} onSubmit={e => updatePassword(e)} autoComplete={"on"}>
                        <fieldset className={"modalInputs"}>
                            <input type={"password"} id={"old-password"} name={"old-password"} title={"Please enter your old password"}
                                onChange={e => setOldPassword(e.target.value)} onBlur={e => checkInputs(e)}
                                aria-label={"old-password"} size={30}  placeholder={"Old password *"} required={true}/>

                            <input type={"password"} id={"new-password"} name={"new-password"} title={"Please enter your new password"}
                                onChange={e => setNewPassword(e.target.value)} onBlur={e => checkInputs(e)}
                                aria-label={"new-password"} size={30} placeholder={"New password *"} required={true}/>
                        </fieldset>
                        <fieldset className={"modalButtonSingle"}>
                            <input className={"buttonBlue"} type={"submit"} value={"Update"}/>
                        </fieldset>
                    </form>
                </div>
            </div>
        </section>
    )
}

export default PasswordModal
