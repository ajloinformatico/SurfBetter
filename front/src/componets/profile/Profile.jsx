/* eslint-disable jsx-a11y/anchor-is-valid */
/* eslint-disable jsx-a11y/anchor-has-content */
import React, {useEffect, useState} from "react";
import swal from "sweetalert";

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

    const [user, setUser] = useState({})
    /**
     * UsseEfect to get User Name
     */
    useEffect(() => {
        authFetch("/api/current_user")
            .then(response => response.json())
            .catch(error => console.log(error))
            .then(userInfo => setUser(userInfo))
    }, [])


     //Set user image by useEffect abd authFetc
    useEffect(() => {
        authFetch("/api/avatar").then(setAvatar("/api/avatar"))
    },[])
    
   
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
        }).then(response => response.json())
        .catch(swal("Error, Something was wrong",{icon:"error"}))
        .then(swal("Your image has been updated success",{icon:"success"})
            .then(async () => {
                authFetch("/api/avatar").then(setAvatar("/api/avatar"))
                window.location.reload()
            })
        );
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
                <div>
                    {/*Upload avatar image*/}
                    <label className={"profileAvatarImage"}htmlFor={"file"}>
                        <img className={"avatarImage"} alt="userIcon" src={avatar}/>
                        <input onChange={e => updateAvatar(e)} type={"file"} name="file" id="file" required={true}/>
                    </label>
                    <p>{user.nick}</p>
                    
                    <p>{user.name} {user.surname}</p>
                </div>
                <div>
                    <h2>User Description</h2>
                    <p>{user.description}</p>
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
            <OptionsModal user={user}/>
            {/*Password update modal*/}
            <input type={"checkbox"} id={"password-update-modal"}/>
            <PasswordModal user={user}/>
            {/*User info update modal*/}
            <input type={"checkbox"} id={"user-info-option-modal"}/>
            <UserInfoUpdateModal user={user}/>
        </main>
        </div>

    )
}
export default Profile;