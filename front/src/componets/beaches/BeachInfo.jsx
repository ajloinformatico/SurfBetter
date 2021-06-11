/* eslint-disable array-callback-return */
/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable jsx-a11y/anchor-is-valid */
import React, {useEffect, useState} from "react";
import { useParams, useHistory } from "react-router-dom";
import HeaderMenu from "../HeaderMenu.jsx";
import {authFetch} from "../auth/auth.jsx";
import parse from 'html-react-parser';
import StarComponent from "./StarComponent.jsx";
import swal from 'sweetalert'
import {calculateLikes, isLikeFromUser, setError} from "../../Utils";

/**
 * Beaches Host
 * @returns {JSX.Element}
 * @constructor
 */
const BeachInfo = () => {
    const history = useHistory()


    //Note: Get Params from url
    const params = useParams();
    //Note: Where come back
    const backPressed = params.back
    const [user, setUser] = useState({})
    const [beach, setBeach] = useState({})
    //Manage descriptions of each beach point
    const [pDescription, setPDescription] = useState([])
    // Manage message
    const [comment, setComment] = useState("")

    /**
     * UsseEfect to get User Name
     */
     useEffect(() => {
        getUser().then(/*NO-LOOP*/)
        getBeachData().then(/*NO-LOOP*/)
        getBeachPoints().then(/*NO-LOOP*/)
    },[])

    const getBeachData = async () => {
        fetch("http://localhost:5000/api/beach/"+params.id)
            .then(res => res.json())
            .then(res => setBeach(res))
    }

    const getUser = async () => {
        authFetch("http://localhost:5000/api/current_user")
            .then(response => response.json())
            .then(userInfo => setUser(userInfo))
    }

    const getBeachPoints = async () => {
        fetch("http://localhost:5000/api/beaches/points")
            .then(response => response.json())
            .catch(error => console.log(error))
            .then(pointsDescription => setPDescription(pointsDescription))
    }

    const back = () => {
        history.push("/"+backPressed)
    }

    /**
     * @param comments : comments
     */
    const checkCommentsEmpty = (comments) => {
        return comments !== undefined
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
            authFetch('http://localhost:5000/api/beach/comment', {
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
            swal("Error check your input", {icon: "success"}).then(/*NO-LOOP*/)
        }
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
                authFetch('http://localhost:5000/api/beach/comment/delete',{
                    method: 'DELETE',
                    body: JSON.stringify(opts)
                }).then(async () => {
                    await getBeachData()
                })
                    .catch(() => {
                        swal("Something was wrong", {icon:"warning"}).then(/*NO-LOOP*/)
                    })
            }
        })
    }


    /**
     * Check if comment exists to delete or add
     */
    const setUnsetCommentLike = (comment) => {
        let method = ''
        let commentExists = ''
        comment.likes_of_comments.map(it => {
            if (it.user_id === user.id) {
                commentExists = true
                method = 'DELETE'
            }
        })

        if (!commentExists) {
            method = 'POST'
        }

        const opts = {
            "comment_id":comment.id
        }

        authFetch('http://localhost:5000/api/beach/comment/like',{
            method: method,
            body: JSON.stringify(opts)
        }).then(async () => {
            await getBeachData()
        }).catch(() => {
                swal("Something was wrong", {icon:"danger"}).then(/*NO-LOOP*/)
            })
    }

    //Note: React say that vars are unresolved but they comes from my state
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
                    <img srcSet={'http://localhost:5000/api/beach/image/'+beach.id}  alt={"beach"}/>
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
                                <StarComponent rating={beach.quality_when_it_works} />
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
                <section className={"beachComments"} id={"beach-info-beach-coments"}>
                    <h2>Beach Comments</h2>
                    {
                        (checkCommentsEmpty(beach.comments) === true)&&(
                        beach.comments.map(comment => {
                            return (
                                <div key={comment.id} id={comment.id} className={"comment"}>
                                    <p>{comment.comment}</p>
                                    <div className={"commentLike"}>
                                        <span onClick={async () => {await setUnsetCommentLike(comment)}}
                                              className={isLikeFromUser(comment.likes_of_comments, user.id)}>
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
                        }))

                    }
                    <form action={"."} onSubmit={e => sendComment(e)}>
                        <textarea onChange={e => setComment(e.target.value)} onBlur={e => checkInputs(e)}
                                  name={"comment"}
                                  id={"comment"}
                                  title={"new Comment"}
                                  required={true}/>
                        <span className={"errorForms"}/>
                        <input className={"buttonYellow"} value={"Comment"} type={"submit"}/>
                    </form>
                </section>

            </main>
        </div>
    )
}
export default BeachInfo;