/* eslint-disable jsx-a11y/anchor-is-valid */
/* eslint-disable array-callback-return */
/* eslint-disable react-hooks/exhaustive-deps */
import React, {useEffect, useState} from "react";
import {useHistory} from "react-router-dom";
import {authFetch} from "../auth/auth";
import OneStar from "../../assets/img/stars/1star.png";
import TwoStar from "../../assets/img/stars/2star.png";
import ThreeStar from "../../assets/img/stars/3star.png";
import FourStar from "../../assets/img/stars/4star.png";
import FiveStar from "../../assets/img/stars/5star.png";
import {calculateLikes, isLikeFromUser, setError} from "../../Utils";
import swal from "sweetalert";
import parse from "html-react-parser";


/**
 * Beaches Host
 * @returns {JSX.Element}
 * @constructor
 */
const BeachBox = (props) => {
    const history = useHistory()
    const [it , setIt] = useState(props.beach)
    const [user, setUser] = useState({})
    const [isComment, setIsComment] = useState(true)
    const [comment, setComment] = useState("")


    /**
     * UsseEfect to get User Name
     */
    useEffect(() => {
        getUser().then(/*NO-LOOP*/)
        getBeachData().then(/*NO-LOOP*/)
    },[])


    const getUser = async () => {
        authFetch("/api/current_user")
            .then(response => response.json())
            .catch(error => console.log(error))
            .then(userInfo => setUser(userInfo))
    }

    const getBeachData = async () => {
        fetch("/api/beach/"+it.id)
            .then(res =>  res.json())
            .then(res =>  setIt(res))
    }



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


    const openBeachInfo = (id) => {
        history.push("/beach/"+id+"/"+props.from)
    }

    const setOrDeleteFav = () => {
        let method = ''
        let likeExists = false
        it.likes.map(like => {
            if (like.user_id === user.id) {
                likeExists = true
                method = 'DELETE'
            }
        })

        if (!likeExists) {
            method = 'POST'
        }

        authFetch('api/beach/like',{
            method: method,
            body: JSON.stringify({"beach_id":it.id})
        }).then(async () => {
            await getBeachData()
        }).catch(() => {
            swal("Error","Something was wrong", {icon:"danger"}).then(/*NO-LOOP*/)
        })

    }


    const openCommentsOnTarget = (id) => {
        const target = document.getElementById("comments-container"+id)
        if (isComment) {
            target.classList.remove('beachBoxUnShow')
            target.classList.add('beachBoxShow')
            setIsComment(!isComment)
        } else {
            target.classList.remove('beachBoxShow')
            target.classList.add('beachBoxUnShow')
            setIsComment(!isComment)
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
                    authFetch('/api/beach/comment/delete',{
                        method: 'DELETE',
                        body: JSON.stringify(opts)
                    }).then(async () => {
                        await getBeachData()
                    })
                        .catch(() => {
                            swal("Error","Something was wrong", {icon:"danger"}).then(/*NO-LOOP*/)
                        })
                }
            })
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
    const sendComment = (e, beach_id) => {
        if (comment.trim()) {
            e.preventDefault();
            const opts = {
                "comment": comment,
                "beach_id": beach_id
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
            swal("Error check your input", {icon: "success"}).then(/*NO-LOOP*/)
        }
    }


    /** Check if comment exists to delete or add */
    const setUnsetCommentLike = (comment) => {
        let method = ''
        let commentExists = false
        //map not return nothing beacuse i use it only to find
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

        authFetch('/api/beach/comment/like',{
            method: method,
            body: JSON.stringify(opts)
        }).then(async () => {
            await getBeachData()
        }).catch(() => {
            swal("Something was wrong", {icon:"danger"}).then(/*NO-LOOP*/)
        })
    }

    return (
        <section id={it.id} className={"beachBox"}>
            <div className={"beachImage"} style={{backgroundImage : 'url(api/beach/image/'+it.id+')'}}>
                <span className={setFlag(it.falg)}>
                    <i className={"fas fa-flag fa-2x"}/>
                </span>
            </div>
            <div className={"beachInfo"}>
                <div className={"beachHeader"}>
                    <h2>{it.name}</h2>
                    <div>
                        <img className={"star"} src={calculateMedia(it)}  width={"30"} height={"30"} title={"Total Points"} alt={"points"}/>
                        {/*No href because i use history to to open beach info */}
                        <a className={"seeMore"} onClick={() => openBeachInfo(it.id)}>
                            <i className="fas fa-info-circle fa-2x"/>
                        </a>
                    </div>

                </div>
                <div className={"beachPoints"}>
                    <ul>
                        <li>
                            <img srcSet={"https://img.icons8.com/ios-filled/30/000000/warranty-card.png"}
                                 alt={"Quality when it works"} title={"Quality when it works"}/>
                            <p>Quality when it work</p>
                            <span>{it.quality_when_it_works}</span>
                        </li>
                        <li>
                            <img srcSet={"https://img.icons8.com/ios-filled/30/000000/wave-lines.png"}
                                 alt={"Wave consistency"} title={"Wave consistency"}/>
                            <p>Wave Consistency</p>
                            <span>{it.wave_consistency}</span>
                        </li>
                        <li>
                            <img srcSet={"https://img.icons8.com/ios-filled/30/000000/surfing.png"}
                                 alt={"Difficulty"} title={"Difficulty"}/>
                            <p>Difficulty</p>
                            <span>{it.difficulty}</span>
                        </li>
                        <li>
                            <img alt={"WindSurf and kySurf"} srcSet={"https://img.icons8.com/ios-filled/30/000000/windsurfing--v1.png"}/>
                            <p>Windsurf and kitesurf</p>
                            <span>{it.windsurf_y_kitesurf}</span>
                        </li>
                        <li>
                            <img srcSet={"https://img.icons8.com/ios-glyphs/30/000000/beach-volleyball.png"}
                                 alt={"people to water"} title={"people to water"}/>
                            <p>People to water</p>
                            <span>{it.people_to_water}</span>
                        </li>
                    </ul>
                </div>

                <div id={"comments-container"+it.id} className={"beachBoxUnShow"}>

                    {
                        it.comments.map(comment => {
                            return (
                                <div id={comment.id} key={comment.id} className={"comment"}>
                                    <p>{comment.comment}</p>
                                    <div className={"commentLike"}>
                                        <span onClick={async () => {await setUnsetCommentLike(comment)}} className={isLikeFromUser(comment.likes_of_comments, user.id)}>
                                            <i className={"fas fa-heart fa"}/>
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
                                    <p className={"beachTime"}>{parse(comment.created_date)}</p>
                                    {/*Trash*/}
                                </div>
                            )
                        })
                    }

                </div>
                {
                    isComment?(
                        <div className={"beachFooter"}>
                            <span onClick={() => openCommentsOnTarget(it.id)}>
                                <h3>Comments</h3>
                            </span>
                            <div className={"beachLikes"}>
                                <span onClick={async () => {await setOrDeleteFav()}} className={isLikeFromUser(it.likes, user.id)}>
                                    <i className="fas fa-heart"/>
                                </span>
                                <p>{(it.likes)?calculateLikes(it.likes):0}</p>
                            </div>
                        </div>
                    ):(
                        <div className={"beachBoxForm"}>
                            <form onSubmit={e => sendComment(e, it.id)}>
                                <textarea onChange={e => setComment(e.target.value)} onBlur={e => checkInputs(e)}
                                    name={"comment"}
                                    id={"comment"}
                                    title={"new Comment"}
                                    required={true}/>
                                <input className={"buttonBlue"} type={"submit"} value={"Comment"}/>
                            </form>
                            <span className={"seeMore"} onClick={() => openCommentsOnTarget(it.id)}>
                                <i className="fas fa-times-circle fa-2x"/>
                            </span>
                        </div>
                    )
                }

            </div>
        </section>
    )
}
export default BeachBox;