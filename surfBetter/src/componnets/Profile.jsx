/* eslint-disable jsx-a11y/anchor-is-valid */
/* eslint-disable jsx-a11y/anchor-has-content */
import React, {useEffect, useState} from "react";

//Auth
import {authFetch} from "./auth/auth.jsx"

import HeaderMenu from "./HeaderMenu.jsx";
import logoSurfBetterHeader from "../assets/img/common/logoSurfBetterHeader.png";

/**
 * 
 * @param {Props} props:props.user => User Object 
 * @returns {JSXElement}: jsx react componnent
 */
const Profile = (props) => {


    //States for modal 
    const [email, setEmail] = useState("")
    const [name, setName] = useState("")
    const [surname, setSurname] = useState("")
    const [avatar, setAvatar] = useState("")
    const [nick, setNick] = useState("")
    const [password, setPassword] = useState("")
    const [description, setDescription] = useState("")


     //Set user image by useEffect abd authFetc
     useEffect(() => {
         getAvatar()
    },[])
    
    
    


    const getAvatar = async () => {
        debugger
        authFetch("/api/avatar")
        .then(
            setAvatar('/api/avatar')
        )
    }
   
    /**
     * Put update user avatar
     * @param {event} e 
     */
    const updateAvatar = async e => {
        e.preventDefault()
        const formData = new FormData();
        formData.append("file", document.getElementById("file").files[0])  
        authFetch('/api/avatar',{
            method: 'PUT',
            body: formData
        }).then(getAvatar())
    }
    
    return (
        <div>
        <HeaderMenu/>
        <main>
            <div className={"headerProfile"}>
                <h1>Profile</h1>
                <label id={"optionsButton"} htmlFor={"btn-modal-user-options"}>
                    <a className={"buttonYellow"} title="User options">Options</a>
                </label>
            </div>    
            <section className="profilesUserDescription">
            {console.log(props.user)}            
                <div>
                    {/*Upload avatar image*/}
                    <label class={"profileAvatarImage"}htmlFor={"file"}>
                        <img className={"avatarImage"} alt="userIcon" src={avatar}/>
                        <input onChange={e => updateAvatar(e)} type={"file"} name="file" id="file" required={true}/>
                    </label>
                    <p>{props.user.nick}</p>
                    
                    <p>{props.user.name} {props.user.surname}</p>
                </div>
                <div>
                    <h2>User Description</h2>
                    <p>{props.user.description}</p>
                </div>
            </section>
            <section className="ProfileBeaches">
                <div>
                    <h2>Favorite Beaches</h2>
                </div>
                <div>
                    <h2>Commented Beaches</h2>
                </div>
            </section>
            <input type={"checkbox"} id={"btn-modal-user-options"}/>
            
            {/*Options modal*/}
            <section className={"modealOptions"}>
            <div className={"container"}>
                <header>
                    <img srcSet={logoSurfBetterHeader} alt={"logo SurfBetter"}
                    title={"SurfBetter logo"}/>
                    <div role={"button"}>
                        <label htmlFor={"btn-modal-user-options"}>
                            <a title={"exit"}>
                                <i className={"fas fa-arrow-left fa-2x"}></i>
                            </a>
                        </label>
                    </div>
                </header>
                
                <div className={"contentModal"}>
                    <form id={"update-avatar"} 
                        onSubmit={e => updateAvatar(e)}
                        encType={"multipart/formdata"}>

                        
                       
                    
                        <input type={"submit"} value="update"/>
                    </form>
                </div>
            </div>
        </section>
        </main>
        </div>
        
    )
}
export default Profile