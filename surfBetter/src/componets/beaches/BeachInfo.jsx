import React, {Suspense, useEffect, useState} from "react";
import { useParams, useHistory } from "react-router";
import HeaderMenu from "../HeaderMenu.jsx";
import {authFetch} from "../auth/auth.jsx";
import parse from 'html-react-parser';

/**
 * Beaches Host
 * @returns {JSX.Element}
 * @constructor
 */
const BeachInfo = () => {

    //GET PARAM FROM URL
    const params = useParams();
    const [user, setUser] = useState({})
    const [beach, setBeach] = useState({})
    const history = useHistory()

    /**
     * UsseEfect to get User Name
     */
    useEffect(() => {
        authFetch("/api/current_user")
            .then(response => response.json())
            .catch(error => console.log(error))
            .then(userInfo => setUser(userInfo))
        fetch("/api/beach/"+params.id)
            .then(response => response.json())
            .catch(error => console.log(error))
            .then(beachInfo => setBeach(beachInfo))
    }, [])



    const back = () => {
        history.push("/")
    }

    return (
        <div>
            <HeaderMenu/>
            <a className={"beachDetailBack"} onClick={() => back()}>
                <i className="fas fa-arrow-circle-left fa-3x"/>
            </a>

            <main className={"beachDetail"}>
                <section className={"beachDescription"}>
                    <img srcSet={'/api/beach/image/'+beach.id}  alt={"beach picture"}/>
                    <div>
                        <h1>{beach.name}</h1>
                        <p>{beach.description}</p>
                    </div>
                </section>
                <section className={"beachWaves"}>
                    {parse(""+beach.surf_fore_cast_link)}
                </section>
            </main>
        </div>
    )
}
export default BeachInfo;