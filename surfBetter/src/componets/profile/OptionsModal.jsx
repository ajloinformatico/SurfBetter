/* eslint-disable jsx-a11y/anchor-has-content */
/* eslint-disable jsx-a11y/anchor-is-valid */
import React from 'react';
import logoSurfBetterHeader from '../../assets/img/common/logoSurfBetterHeader.png';

import PasswordModal from './PasswordModal.jsx';
import UserInfoUpdateModal from './UserInfoUpdateModal.jsx'





/* *
 * 
 * @param props: user state
 * @returns {JSX.Component}
 */
const OptionsModal = (props) => {

    /**
     * By checkbox ids close user options modal and open password resset modal
     */
    const openPasswordResset =  () => {
        document.getElementById('user-options-modal').checked = false
        document.getElementById('password-update-modal').checked = true
    }

    const openUserInfoOptionModa = () => {
        document.getElementById('user-options-modal').checked = false
        document.getElementById('user-info-option-modal').checked = true
    } 

    const closeOptionModal = () => {
        document.getElementById('user-options-modal').checked = false
    }



    return (
        <section className={"optionsModal"}>
        <div className={"container"}>
            <header>
                <img src={logoSurfBetterHeader} alt={"logo surfBetter"}/>
                <a title={"exit"} onClick={() => closeOptionModal()} className={"fas fa-arrow-left fa-2x"}a/>
            </header>
            <div className={"contentModal"}>
                <div className={"header-options-menu"}>
                    <h2>User Options</h2>
                    <p>
                        hello <b>{props.user.nick} </b> 
                        please choose options section
                    </p>
                </div>
                
                <div className={"modalOptionsButtons"} role={"main"}>
                        <a className={"buttonBlue"} title={"Go to user options"}
                        onClick={() => openUserInfoOptionModa()}>
                            User info
                        </a>
                        <a className={"buttonBlue"} title={"Go to user password update"}
                            onClick={() => openPasswordResset()}>
                            Password
                        </a>
                </div>
            </div>
        </div>
        </section>
    )
}

export default OptionsModal
