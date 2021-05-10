/* eslint-disable jsx-a11y/anchor-is-valid */
/* eslint-disable jsx-a11y/anchor-has-content */
import React, {useEffect, useState} from "react";

//Auth
import {authFetch} from "../auth/auth.jsx"
import HeaderMenu from "../HeaderMenu.jsx";

//Updates modals
import OptionsModal from "./OptionsModal.jsx";
import PasswordModal from './PasswordModal.jsx';
import UserInfoUpdateModal from './UserInfoUpdateModal.jsx';
/**
 * 
 * @param {Props} props:props.user => User Object 
 * @returns {JSXElement}: jsx react componnent
 */
const Profile = (props) => {


    //States for modal 
    const [avatar, setAvatar] = useState("")
    
    let user = props.user
     //Set user image by useEffect abd authFetc
    useEffect(() => {
        authFetch("/api/avatar").then(setAvatar("/api/avatar"))
    },[])
    


    const getAvatar = async () => {
        authFetch("/api/avatar").then(setAvatar("/api/avatar"))
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
        }).then(e => getAvatar(e))
    }


  



    return (
        <div>
        <HeaderMenu/>
        <main>
            <div className={"headerProfile"}>
                <h1>Profile</h1>
                {/*Label for btn options menu to open user options screem*/}
                <label htmlFor={"user-options-modal"}>
                    <a className={"buttonYellow"} title="User options">Options</a>
                </label>
                {/*Secret flag checkbox input to open options*/}
            </div>    
            <section className="profilesUserDescription">
            {console.log(props.user)}            
                <div>
                    {/*Upload avatar image*/}
                    <label className={"profileAvatarImage"}htmlFor={"file"}>
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
            {/*Options modal componnent*/}
            <input type={"checkbox"} id={"user-options-modal"}/>
            <OptionsModal user={props.user}/>
            {/*Password update modal*/}
            <input type={"checkbox"} id={"password-update-modal"}/>
            <PasswordModal user={props.user}/>
            {/*User info update modal*/}
            <input type={"checkbox"} id={"user-info-option-modal"}/>
            <UserInfoUpdateModal user={props.user}/>
        </main>
        </div>
        
    )
}
export default Profile;