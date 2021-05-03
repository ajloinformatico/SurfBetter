import React  from "react";

import HeaderMenu from "./HeaderMenu.jsx";


/**
 * 
 * @param {Props} props:props.user => User Object 
 * @returns {JSXElement}: jsx react componnent
 */
const Profile = (props) => {

    


    return (
        <div>
            <HeaderMenu/>
            <h1>Profile</h1>

            {console.log(props.user)}
            <img alt="user Avatar" src={"http://localhost:5000/"+props.user.avatar}/>
            <h2>{props.user.name}</h2>
            <h2>{props.user.email}</h2>
        </div>
        
    )
}
export default Profile