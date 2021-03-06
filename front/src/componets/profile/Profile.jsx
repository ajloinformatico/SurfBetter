/* eslint-disable jsx-a11y/anchor-is-valid */
/* eslint-disable jsx-a11y/anchor-has-content */
import React, {useEffect, useState} from "react";
import swal from "sweetalert";

//Auth
import {authFetch} from "../auth/auth.jsx";
import HeaderMenu from "../HeaderMenu.jsx";

//Updates modals
import OptionsModal from "./OptionsModal.jsx";
import PasswordModal from './PasswordModal.jsx';
import UserInfoUpdateModal from './UserInfoUpdateModal.jsx';
import BeachBox from "../beaches/BeachCard";

/**
 * Profile Host component
 * @returns {JSX.Element}: jsx react componnent
 */
const Profile = () => {

    /**
     * UsseEfect to get User Name
     */
    useEffect(() => {
        getUser().then(/*NO-LOOP*/);
        getAvatar().then(/*NO-LOOP*/);
        getFavoritesAndComments().then(/*NO-LOOP*/);
    },[]);

    //States for modal 
    const [avatar, setAvatar] = useState("");
    const [user, setUser] = useState({});
    const [favorites, setFavorites] = useState([]);
    const [beachComments, setBeachComments] = useState([]);

    const getUser = async () => {
        authFetch("http://localhost:5000/api/current_user")
            .then(response => response.json())
            .catch(async () => await swal("Error","Something was wrong",{icon:"warning"})).then(/*NO-LOOP*/)
            .then(userInfo => setUser(userInfo));
    };

    const getFavoritesAndComments = async () => {
        authFetch("http://localhost:5000/api/user/fav_comments_beches/0")
            .then(response => response.json())
            .catch(error => console.log(error))
            .then(favoritesInfo => setFavorites(favoritesInfo));

        authFetch("http://localhost:5000/api/user/fav_comments_beches/1")
            .then(response => response.json())
            .catch(error => console.log(error))
            .then(beachesCommentsInfo => setBeachComments(beachesCommentsInfo));
    };

    const getAvatar = async () => {
        authFetch("/api/avatar")
            .then(response => setAvatar(response.url));

    };

    const setEmptyAvatar = async () => {
        setAvatar("");
    };

    /**
     * Put update user avatar
     */
    const updateAvatar = () => {
        const formData = new FormData();
        formData.append("file", document.getElementById("file").files[0])  
        authFetch('/api/avatar',{
            method: 'PUT',
            body: formData
        })
        .then(swal("Your image has been updated success",{icon:"success"})
            .then(async () => {
                await setEmptyAvatar()
                await getAvatar()
            }));
    };

    return (
        <div>
        <HeaderMenu/>
        {
        user.name!==undefined&&(
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
                        <label className={"profileAvatarImage"} htmlFor={"file"}>
                            <img className={"avatarImage"} alt="user avatar" srcSet={avatar}/>
                            <input onChange={async () => {await updateAvatar()}} type={"file"} name="file" id="file" required={true}/>
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
                    <h2>Favorite Beaches</h2>
                    <section className={"contentBeaches"}>
                        { /*Loop by map to set beaches*/
                            favorites!==undefined&&(
                                favorites.map(it => {
                                    return(
                                        <BeachBox beach={it} from={"profile"}/>
                                    )
                                }))
                        }
                    </section>
                    <h2>Commented Beaches</h2>
                    <section className={"contentBeaches"}>
                        {
                            beachComments!==undefined&&(
                                beachComments.map(it => {
                                    return (
                                        <BeachBox beach={it} key={it.id} from={"profile"}/>
                                    )
                                })
                            )
                        }
                    </section>
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
        )
        }
        </div>

    )
}
export default Profile;