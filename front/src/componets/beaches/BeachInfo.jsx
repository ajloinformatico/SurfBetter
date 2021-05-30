import React, {Suspense, useEffect, useState} from "react";
import { useParams, useHistory } from "react-router";
import HeaderMenu from "../HeaderMenu.jsx";
import {authFetch} from "../auth/auth.jsx";
import parse from 'html-react-parser';
import StarComponent from "./StarComponent.jsx";
import swal from 'sweetalert'
import {calculateLikes, setError} from "../../Utils";

/**
 * Beaches Host
 * @returns {JSX.Element}
 * @constructor
 */
const BeachInfo = () => {

    const history = useHistory()


    //GET PARAM FROM URL
    const params = useParams();
    const [user, setUser] = useState({})
    const [beach, setBeach] = useState({})
    //Manage descriptions of each beach point
    const [pDescription, setPDescription] = useState([])
    // Manage message
    const [comment, setComment] = useState("")


    const getBeachData = async () => {
        fetch("/api/beach/"+params.id)
            .then(res => res.json())
            .then(res => setBeach(res))
    }

    const getUser = async () => {
        authFetch("/api/current_user")
            .then(response => response.json())
            .then(userInfo => setUser(userInfo))
    }

    const getBeachPoints = async () => {
        fetch("/api/beaches/points")
            .then(response => response.json())
            .catch(error => console.log(error))
            .then(pointsDescription => setPDescription(pointsDescription))
    }

    /**
     * UsseEfect to get User Name
     */
    useEffect(async () => {
        await getUser()
        await getBeachData()
        await getBeachPoints()
    },[])

    const back = () => {
        history.push("/")
    }

    /**
     * @param comments : comments
     */
    const checkCommentsEmpty = (comments) => {
        console.log(comments)
        return comments !== undefined && comments !== []
    }

    /**
     * Check text area send comment
     */
    const checkInputs = (e) => {
        const input = e.target;
        input.classList.remove("errors");
        setError(comment, input, [0, 400])&&setComment("")
    }

    /**
     * Send comments
     */
    const sendComment = (e) => {
        if (comment.trim()) {
            e.preventDefault();
            const opts = {
                "comment": comment,
                "beach_id": beach.id
            }
            authFetch('/api/beach/comment', {
                headers : {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                method: 'POST',
                body: JSON.stringify(opts)
            }).then(async () => {
                await getBeachData()
            })
        } else {
            swal("Error check your input", {icon: "success"})
        }
    }

    const isLikeFromUser = (likes_of_comments) => {
        let result = ""
        likes_of_comments.forEach(it => {
           (it.user_id===user.id)&&(result = "red-flag")
        })
        return result
    }

    const deleteComment = (comment_id) => {
        swal({
            text: "Are you shure you want to delete the comment",
            icon: "warning",
            buttons: true,
            dangerMode: true
        })
        .then((pleaseDelete) => {
            if (pleaseDelete) {
                const opts = {
                    "comment_id":comment_id
                }
                authFetch('/api/beach/comment/delete',{
                    method: 'DELETE',
                    body: JSON.stringify(opts)
                }).then(async () => {
                    await getBeachData()
                })
                    .catch(() => {
                        swal("Something was wrong", {icon:"danger"})
                    })
            }
        })




    }

    return (
        <div>
            <HeaderMenu/>
            <main className={"beachDetail"}>
                <section className={"beachInfoHeader"}>
                    <h1>{beach.name}</h1>
                    <a className={"beachDetailBack"} onClick={() => back()}>
                        <i className="fas fa-arrow-circle-left fa-2x"/>

                    </a>
                </section>

                <section className={"beachDescription"}>
                    <img srcSet={'/api/beach/image/'+beach.id}  alt={"beach picture"}/>
                    <div>

                        <p>{beach.description}</p>
                    </div>
                </section>
                <section className={"foreCastInfo"}>
                    <h2>Waves</h2>
                    <div className={"beachWaves"}>
                        {parse(""+beach.surf_fore_cast_link)}
                    </div>
                </section>
                <section className={"beachDetailPoints"}>
                { /** Ask why*/
                pDescription[0]!==undefined&&(
                    <dl>
                        <div>
                        <dt>
                            <h3>{pDescription[0].name}</h3>
                            <StarComponent rating={beach.quality_when_it_works}/>
                        </dt>
                        <dd>
                            <p>{pDescription[0].point_info}</p>
                        </dd>
                        </div>

                        <div>
                        <dt>
                            <h3>{pDescription[1].name}</h3>
                            <StarComponent rating={beach.wave_consistency}/>
                        </dt>
                        <dd>
                            <p>{pDescription[1].point_info}</p>
                        </dd>
                        </div>

                        <div>
                        <dt>
                            <h3>{pDescription[2].name}</h3>
                            <StarComponent rating={beach.difficulty}/>
                        </dt>
                        <dd>
                            <p>{pDescription[2].point_info}</p>
                        </dd>
                        </div>

                        <div>
                        <dt>
                            <h3>{pDescription[3].name}</h3>
                            <StarComponent rating={beach.windsurf_y_kitesurf}/>
                        </dt>
                        <dd>
                            <p>{pDescription[3].point_info}</p>
                        </dd>
                        </div>

                        <div>
                        <dt>
                            <h3>{pDescription[4].name}</h3>
                            <StarComponent rating={beach.people_to_water}/>
                        </dt>
                        <dd>
                            <p>{pDescription[4].point_info}</p>
                        </dd>
                        </div>

                        <div>
                        <dt>
                            <h3>{pDescription[5].name}</h3>
                            <StarComponent ratitng={beach.sea_weends?beach.sea_weends:0}/>
                        </dt>
                        <dd>
                            <p>{pDescription[5].point_info}</p>
                        </dd>
                        </div>

                        <div>
                        <dt>
                            <h3>{pDescription[6].name}</h3>
                            <StarComponent rating={beach.other_options?beach.other_options:0}/>
                        </dt>
                        <dd>
                            <p>{pDescription[6].point_info}</p>
                        </dd>
                        </div>

                        <div>
                        <dt>
                            <h3>{pDescription[7].name}</h3>
                            <StarComponent rating={beach.water_quality?beach.water_quality:0}/>
                        </dt>
                        <dd>
                            <p>{pDescription[7].point_info}</p>
                        </dd>
                        </div>

                        <div>
                        <dt>
                            <h3>{pDescription[8].name}</h3>
                            <StarComponent rating={beach.access?beach.access:0}/>
                        </dt>
                        <dd>
                            <p>{pDescription[8].point_info}</p>
                        </dd>
                        </div>

                        <div>
                        <dt>
                            <h3>{pDescription[9].name}</h3>
                            <StarComponent rating={beach.scenery?beach.scenery:0}/>
                        </dt>
                        <dd>
                            <p>{pDescription[9].point_info}</p>
                        </dd>
                        </div>

                        <div>
                        <dt>
                            <h3>{pDescription[10].name}</h3>
                            <StarComponent rating={beach.local_attitude?beach.local_attitude:0}/>
                        </dt>
                        <dd>
                            <p>{pDescription[10].point_info}</p>
                        </dd>
                        </div>

                        <div>
                        <dt>
                            <h3>{pDescription[11].name}</h3>
                            <StarComponent rating={beach.accommodation?beach.accommodation:0}/>
                        </dt>
                        <dd>
                            <p>{pDescription[11].point_info}</p>
                        </dd>
                        </div>

                        <div>
                        <dt>
                            <h3>{pDescription[12].name}</h3>
                            <StarComponent rating={beach.camping?beach.camping:0}/>
                        </dt>
                        <dd>
                            <p>{pDescription[12].point_info}</p>
                        </dd>
                        </div>

                        <div>
                        <dt>
                            <h3>{pDescription[13].name}</h3>
                            <StarComponent rating={beach.entertainment?beach.entertainment:0}/>
                        </dt>
                        <dd>
                            <p>{pDescription[13].point_info}</p>
                        </dd>
                        </div>

                        <div>
                        <dt>
                            <h3>{pDescription[14].name}</h3>
                            <StarComponent rating={beach.equipment_and_repairs?beach.equipment_and_repairs:0}/>
                        </dt>
                        <dd>
                            <p>{pDescription[14].point_info}</p>
                        </dd>
                        </div>

                        <div>
                        <dt>
                            <h3>{pDescription[15].name}</h3>
                            <StarComponent rating={beach.restaurants?beach.restaurants:0}/>
                        </dt>
                        <dd>
                            <p>{pDescription[15].point_info}</p>
                        </dd>
                        </div>

                        <div>
                            <dt>
                                <h3>{pDescription[16].name}</h3>
                                <StarComponent rating={beach.pubs?beach.pubs:0}/>
                            </dt>
                            <dd>
                                <p>{pDescription[16].point_info}</p>
                            </dd>
                        </div>
                    </dl>
                )}
                </section>
                <section className={"beachComments"}>
                    <h2>Beach Comments</h2>
                    {
                        (checkCommentsEmpty(beach.comments) === true)?(
                        beach.comments.map(comment => {
                            return (
                                <div id={comment.id} className={"comment"}>
                                    <p>{comment.comment}</p>
                                    <div className={"commentLike"}>
                                        <span className={isLikeFromUser(comment.likes_of_comments)}>
                                            <i className={"fas fa-heart"}/>
                                        </span>
                                        <p>{(comment.likes_of_comments)?calculateLikes(comment.likes_of_comments):0}</p>
                                    </div>
                                    {
                                        (comment.user_id===user.id)&&(
                                            <span  onClick={async () => {await deleteComment(comment.id)}} className={"deleteComment"}>
                                                <i className={"fa fa-trash"}/>
                                            </span>
                                        )
                                    }

                                    {/*Trash*/}
                                </div>
                            )
                        })):(<h3>No existen comentarios !</h3>)

                    }
                    <form action={"."} onSubmit={e => sendComment(e)}>
                        <textarea onChange={e => setComment(e.target.value)} onBlur={e => checkInputs(e)}
                                  name={"comment"}
                                  id={"comment"}
                                  title={"new Comment"}/>
                        <span className={"errorForms"}/>
                        <input className={"buttonYellow"}  type={"submit"}/>
                    </form>
                </section>

            </main>
        </div>
    )
}
export default BeachInfo;