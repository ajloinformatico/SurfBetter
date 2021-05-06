import React, { useEffect } from "react";
import {useHistory} from "react-router";
import serverNotFound from "../assets/img/common/server_not_found.mp4"

const ServerError = (props) => {
    
    
    const history = useHistory()


    useEffect(() => {
        props.ServerError&&history.push('/')
    });
    
    return (
        <div>
            <h1>Server error</h1>
            <h2>Server not found please contact to: <br/>
                <a href={"mailto:ajloinformatico@gmail.com"} alt={"Send an email"} title={"Send an email"}>
                    ajloinformatico@gmail.com
                </a>     
            </h2>
            <main>
                <video  controls title="server error" autoPlay={true} loop={true}>
                    <source src={serverNotFound} type={"video/mp4"}/>
                </video>
            </main>
        
        </div>

    )
}
export default ServerError