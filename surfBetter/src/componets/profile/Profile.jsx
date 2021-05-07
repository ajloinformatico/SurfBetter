/* eslint-disable jsx-a11y/anchor-is-valid */
/* eslint-disable jsx-a11y/anchor-has-content */
import React, {useEffect, useState} from "react";

//Auth
import {authFetch} from "../auth/auth.jsx"
import HeaderMenu from "../HeaderMenu.jsx";
import logoSurfBetterHeader from "../../assets/img/common/logoSurfBetterHeader.png";
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
    const [oldPassword, setOldPassword] = useState("")
    const [newPassword, setNewPassword] = useState("")
    const [description, setDescription] = useState("")

    

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
            case ("email") :
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
            case ("old_password") :
                if (!oldPassword.trim()) {
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " is empty";
                    setOldPassword("")
                } else if ( oldPassword.length > 64 || oldPassword.length < 8){
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " isn't valid";
                    setOldPassword("");
                }
                break;
            case ("new_password") :
                if (!newPassword.trim()) {
                    input.classList.add('errors');
                    input.value = "";
                    input.placeholder = input.id + " isn't valid";
                    setNewPassword("");
                } else if (newPassword > 64 || newPassword.length < 8){
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " isn't valid";  
                    setNewPassword("");

                } else if (newPassword === oldPassword) {
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " is the same as your current password";
                    setNewPassword("");
                }
                break;
            default :
                break;
        }
    }



    const updateUser = async e => {
        alert("Actualizte")
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
                {/*Header modal*/}
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
                    <form id={"update-form"} 
                        onSubmit={e => updateUser(e)}
                        encType={"multipart/formdata"}>

                        <fieldset className={"modalInputs"}>
                            <legend>Update User info</legend>
                            <input type={"text"} id={"name"} name={"name"} aria-labe={"name"}
                                onChange={e => setName(e.target.value)} onBlur={e => checkInputs(e)}
                                size={30} title={"Please input a valid name"} placeholder={"New user name *"}
                                required={true}/>
                                
                            <input type={"text"} id={"surname"} name={"surname"} aria-label={"surname"}
                               onChange={e => setSurname(e.target.value)} onBlur={e => checkInputs(e)}
                               size={30} title={"Please input a valid surname"} placeholder={"User Surname"} 
                               required={true}/>

                            <input type={"text"} id={"nick"} name={"nick"} aria-label={"nick"}
                               onChange={e => setNick(e.target.value)} onBlur={e => checkInputs(e)}
                               size={30} title={"Please input a valid nick"} placeholder={"User Nick *"} 
                               required={true}/>

                            <input type={"email"} id={"email"} name={"email"} title={"Please enter a valid email *"}
                               onChange={e => setEmail(e.target.value)} onBlur={e => checkInputs(e)}
                               size={30} aria-label={"email"} placeholder={"Email *"} 
                               required={true}/>
                        </fieldset>
                        <fieldset className={"modalButtons"}>
                            <input type={"submit"} value="update"/>
                        </fieldset>
                    </form>
                </div>
            </div>
        </section>
        </main>
        </div>
        
    )
}
export default Profile