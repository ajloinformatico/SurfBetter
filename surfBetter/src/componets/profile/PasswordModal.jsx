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


    const checkCommonsPassword = (input, state) =>{
        

    }

    /**
     * 
     * @param {Event} e: todo refator 
     */
    const checkInputs = (e) => {
        let input = e.target;
        input.classList.remove("errors");
        
        if (input.id === "old-password") {
            checkCommonsPassword(input, oldPassword)
        } else if (input.id === "new-password") {
            checkInputs(input, newPasword)
        }

        if (oldPassword === newPasword){
            input = e.target;
            input.classList.add("errors")
            input.value = ""
            input.placeholder = "Passwords cannot be the same"
            setOldPassword("") 
        }

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
                    <form id="updatePassword" onSubmit={e => updatePassword(e)} autoComplete={"on"}>
                        <fieldset className={"modalInputs"}>
                            <input type={"password"} id={"old-password"} name={"old-password"} title={"Please enter your old password"}
                                    onChange={e => setOldPassword(e.target.value)} onBlur={e => checkInputs(e)}
                                    aria-label={"old-password"} size={30}  placeholder={"Old password *"} required={true}/>

                            <input type={"password"} id={"new-password"} name={"new-password"} title={"Please enter your new password"}
                                onChange={e => setNewPassword(e.target.value)} onBlur={e => checkInputs(e)}
                                aria-label={"new-password"} size={30} placeholder={"New password *"} required={true}/>
                        </fieldset>
                        <fieldset className={"modalButtonSingle"}>
                            <input className={"buttonBlue"} type={"submit"} value="Update"/>
                        </fieldset>
                    </form>

                </div>
            </div>
            
        </section>
    )
}

export default PasswordModal
