import React, {useEffect, useState, Suspense, lazy} from "react";
import {useHistory} from "react-router";
import {authFetch} from "../auth/auth";
import OneStar from '../../assets/img/stars/1star.png'
import TwoStar from '../../assets/img/stars/2star.png'
import ThreeStar from '../../assets/img/stars/3star.png'
import FourStar from '../../assets/img/stars/4star.png'
import FiveStar from '../../assets/img/stars/5star.png'
import Contact from "../Contact";
import {Redirect} from "react-router-dom";
import BeachesHost from "./BeachesHost";



const Beaches = () => {

    const [user, setUser] = useState({})
    const [beaches, setBeaches] = useState([])
    const history = useHistory()

    /**
     * UsseEfect to get User Name
     */
    useEffect(() => {
        authFetch("/api/current_user")
            .then(response => response.json())
            .catch(error => console.log(error))
            .then(userInfo => setUser(userInfo))
        fetch("/api/beaches")
            .then(response => response.json())
            .catch(error => console.log(error))
            .then(beacheInfo => setBeaches(beacheInfo))
    }, [])

    /**
     * Change flag color by changing style
     * @param flagCode: code of the flag (0 = red,
     * 1 = yellow,
     * 2 = orange,
     * 3 = red)
     * @returns {string}
     */
    const setFlag = (flagCode) => {
        if (flagCode === 0){
            return "red-flag"
        } else if (flagCode === 1){
            return "orange-flag"
        } else if (flagCode === 2){
            return "yellow-flag"
        } else if (flagCode === 3){
            return "green-flag"
        }
    }

    /**
     * Calculate the mean. I have decided to do it like this to follow Javi's
     * advice not to leave all the work to the server
     * @param it: Beach
     * @returns {int}
     */
    const calculateMedia = (it) => {
        let sum = 0
        let len = 0
        for (const property in it) {
            if (it[property] in [0,1,2,3,4,5] && it[property].toString.length === 1){
                sum += it[property]
                len++
            }
        }
        return setMedia(sum/len);
    }

    const setMedia = (media) => {
        if (media >= 0 && media < 1.5) {
            return OneStar
        } else if (media >= 1.5 && media < 2.5) {
            return TwoStar
        } else if (media >= 2.5 && media < 3.5) {
            return ThreeStar
        } else if (media >= 3.5 && media < 4.5) {
            return FourStar
        } else {
            return FiveStar
        }
    }

    const calculateLikes = (likes) => {
        let counter = 0
        likes.forEach( it => {
            counter++;
        })
        return counter
    }

    const openBeachInfo = (id) => {
        history.push("/beach/"+id)
    }


    return (
        <div>
            <h1>Beaches</h1>
            <section className={"contentBeaches"}>
                { /*Loop by map to set beaches*/
                    beaches.map(it => {
                        return(
                            <section id={it.id} className={"beachBox"}>
                                {/*TODO check why dont load image*/}
                                <div className={"beachHeader"} style={{backgroundImage : 'url(api/beach/image/'+it.id+')'}}>
                                    <span className={setFlag(it.falg)}>
                                        <i className={"fas fa-flag fa-2x"}/>
                                    </span>
                                </div>
                                <div className={"beachInfo"}>
                                    <div className={"beachInfoHeader"}>
                                        <h2>{it.name}</h2>
                                        <img className={"star"} src={calculateMedia(it)}  width={"30"} height={"30"} title={"Total Points"} alt={"points"}/>
                                        <div>
                                            <span className={(calculateLikes(it.likes)>0)?"red-flag":""}>
                                                <i className="fas fa-heart"/>
                                            </span>
                                            <p>{(it.likes)?calculateLikes(it.likes):0}</p>
                                        </div>
                                    </div>
                                    <div className={"beachInfoBody"}>
                                        <div>
                                            {it.description.slice(0,90) + " ..."}
                                        </div>
                                        <a className={"seeMore"} onClick={() => openBeachInfo(it.id)}>
                                            <i className="fas fa-info-circle fa-2x"/>
                                        </a>
                                        <div className={"comments"}>

                                            {
                                                //If comments is > 2 only show 2 else show all
                                                (it.comments>=2)?it.comments.splice(0,2).map:it.comments.map(comment => {
                                                    return (
                                                        <div id={comment.id} className={"comment"}>
                                                            <p>{comment.comment}</p>
                                                            <span>
                                                                <i className={"far fa-heart"}/>
                                                                {/*TODO MAKE METHOD FOR LIKES*/}
                                                            </span>
                                                        </div>
                                                    )
                                                })
                                            }
                                        </div>

                                    </div>
                                </div>
                            </section>
                        )
                    },[])
                }
            </section>
        </div>
    )
}
export default Beaches;