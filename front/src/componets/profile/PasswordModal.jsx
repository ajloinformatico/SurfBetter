/* eslint-disable jsx-a11y/anchor-has-content */
/* eslint-disable react/jsx-no-duplicate-props */
/* eslint-disable jsx-a11y/anchor-is-valid */
import React, {useState} from 'react';
import swal from 'sweetalert';
import logoSurfBetterHeader from "../../assets/img/common/logoSurfBetterHeader.png";
import { authFetch, login } from '../auth/auth';

/**
 * Password modal component
 * @returns {JSX.Element}
 */
const PasswordModal = () => {

    const [oldPassword, setOldPassword] = useState("");
    const [newPassword, setNewPassword] = useState("");

    /** Check password valid*/
    const checkCommonsPassword = (state, input) =>{
        let errors = false;
        if (!state.trim()) {
            input.placeholder = `${input.id} is empty`;
            errors = true;
        } else if (state.length > 64 || state.length < 8){
            input.placeholder = `${input.id} is not valid`;
            errors = true;
        }
        if (!errors) 
            return false;

        input.classList.add("erros");
        input.value = "";
        return true;
    }

    /** Check forms inputs*/
    const checkInputs = (e) => {
        const input = e.target;
        input.classList.remove("errors");
        switch (input.id){
            case  "old-password":
                checkCommonsPassword(oldPassword, input)&&setOldPassword("")
                return true;
            case "new-password":
                checkCommonsPassword(newPassword, input)&&setNewPassword("")
                return true;
            default :
                break;
        }
        if (oldPassword !== newPassword)
                return true;
                
        input.classList.add("errors")
        input.value = "";
        input.placeholder = "Passwords can not be the same";
        setOldPassword("");
        setNewPassword("");
        return true;
    }

    /** Close password modal*/
    const closePasswordModal = () => {
        document.getElementById('password-update-modal').checked = false;
    };

    /** fetch update password*/
    const updatePassword = (e) => {
        e.preventDefault();
        const opts = {
            "old-password":oldPassword,
            "new-password":newPassword,
        }
        authFetch('/api/passwordreset',{
            method: 'PUT',
            body: JSON.stringify(opts)
        }).then(response => response.json())
        .catch(swal("Error","Is it your old password ?"), {icon: "error"})
        .then(async () => await swal("Your password has been updated",{icon:"success"}))
            .then(async () => {
                await closePasswordModal();
       });
    };

    /** Close password modal and open user optional modal*/
    const closePasswordReset = () => {
        closePasswordModal();
        document.getElementById('user-options-modal').checked = true;
    };

    return (
        <section className={"modalPassword"}>
            <div className={"container"}>
                <header>
                    <img srcSet={logoSurfBetterHeader} alt={"surfbetter logo"}/>
                    <a onClick={() => closePasswordReset()} title="exit" className={"fas fa-arrow-left fa-2x"} alt="exit"/>
                </header>
                <div className={"contentModal"}>
                    <h2>Update password</h2>
                    <form id="updatePassword" action={"."} onSubmit={async (e) => {await updatePassword(e)}} autoComplete={"on"}>
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
    );
};

export default PasswordModal;
