import React, {Suspense, useEffect, useState} from "react";
import { useParams, useHistory } from "react-router";
import HeaderMenu from "../HeaderMenu.jsx";
import {authFetch} from "../auth/auth.jsx";
import parse from 'html-react-parser';
import StarComponent from "./StarComponent.jsx";

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
    const [pDescription, setPDescription] = useState([])
    const history = useHistory()

    /**
     * UsseEfect to get User Name
     */
    useEffect(() => {
        //Note: Get user by auth
        authFetch("/api/current_user")
            .then(response => response.json())
            .catch(error => console.log(error))
            .then(userInfo => setUser(userInfo))
        //Note: Get beach by id url param
        fetch("/api/beach/"+params.id)
            .then(response => response.json())
            .catch(error => console.log(error))
            .then(beachInfo => setBeach(beachInfo))
        //Note: Get beach info
        fetch("/api/beaches/points")
            .then(response => response.json())
            .catch(error => console.log(error))
            .then(pointsDescription => setPDescription(pointsDescription))
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
                <section className={"beachDetailPoints"}>
                { /** Ask why*/
                pDescription[0]!==undefined&&(
                    <dl>
                        <dt>
                            <h3>{pDescription[0].name}</h3>
                            <StarComponent rating={beach.quality_when_it_works}/>
                        </dt>
                        <dd>
                            <p>{pDescription[0].point_info}</p>
                        </dd>

                    </dl>
                )}
                </section>
                <section>
                    <h2>Waves</h2>
                    <div className={"beachWaves"}>
                        {parse(""+beach.surf_fore_cast_link)}
                    </div>
                </section>
            </main>
        </div>
    )
}
export default BeachInfo;