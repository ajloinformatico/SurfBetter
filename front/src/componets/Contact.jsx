import React, {useEffect, useState} from "react";
import HeaderMenu from "./HeaderMenu.jsx"
import {authFetch} from "./auth/auth";
import InfolojoImage from "../assets/img/infolojo.png"
import meSmallerImage from '../assets/img/me_smaller.png'
import designerSmaller from '../assets/img/designer.png'
import swal from "sweetalert";
const Contact = () => {


    useEffect(() => {
        getUser().then(/*NO-LOOP*/)
    }, [])

    const getUser = async () => {
        authFetch("/api/current_user")
            .then(response => response.json())
            .catch(error => console.log(error))
            .then(userInfo => setUser(userInfo))
    }

    /**States for email and subject*/
    const [text, setText] = useState("")
    const [subject, setSubject] = useState("")
    const [user, setUser] = useState({})

    const checkAndSendEmail = (e) => {
        e.preventDefault()
        const opts = {
            "user_email": user.email,
            "subject": subject,
            "message": text
        }
        authFetch("/api/send_email", {
            method: "POST",
            body: JSON.stringify(opts)
        }).then(response => response.json())
            .then(async () => await swal("Message has been send success", {icon: "success"}))
            .catch(async () => swal("Error", "Something was wrong with email", {icon: "warning"}))
    }

    return (
        <div>
        <HeaderMenu/>
        <main>
            <h1>Contact</h1>
            <section className={"infolojo"}>
                <figure>
                    <img srcSet={InfolojoImage} alt={"infolojo icon"} title={"INFOLOJO"}/>
                    <figcaption>
                        <h1>INFOLOJO</h1>
                        <h2>Abaout</h2>
                        <p>We are a group of developers passionate about everything that
                            surround computing. We develop web and mobile projects for
                            individuals and companies
                        </p>
                        <a className={"buttonYellow"} href={"https://www.infolojo.es"} target={"_blank"}
                           alt={"Link to infolojo"} rel={"noreferrer"}>infolojo.es</a>
                    </figcaption>
                </figure>
            </section>
            <section className={"infolojoMembers"}>
                <header>
                    <h2>Our team</h2>
                </header>
                <section className={"members"}>
                    <div>
                        <img srcSet={meSmallerImage} alt={"infolojo developer"} title={"Antonio José Lojo Ojeda"}/>
                        <div>
                            <p>Hello My name is Antonio José Lojo Ojeda 😁
                                I represent the logical part of
                                the INFOLOJO projects. Im a micro systems
                                and network technician and web developer
                            </p>
                            <ul>
                                <li><a title={"Antonio´s Instagram"} href={"https://www.instagram.com/antoniojose_lo98/?hl=es"}
                                       target={"_blank"} alt={"Antonio´s Instagram"} rel={"noreferrer"}>
                                    <i className="fab fa-instagram-square fa-3x"/>
                                    </a>
                                </li>
                                <li>
                                    <a title={"Antoni´s Git Hub"} href={"https://github.com/ajloinformatico"}
                                       target={"_blank"} alt={"Antoni´s Git Hub"} rel={"noreferrer"}>
                                        <i className="fab fa-github-square fa-3x"/>
                                    </a>
                                </li>
                                <li>
                                    <a title={"Antonio´s Twitter"} href={"https://twitter.com/antoniojose_lo9"}
                                       target={"_blank"} alt={"Antonio´s Twitter"} rel={"noreferrer"}>
                                        <i className="fab fa-twitter-square fa-3x"/>
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div>
                        <img srcSet={designerSmaller} alt={"Elena designer"} title={"Elena Rodriguez Lancho"}/>
                        <div>
                            <p>
                                Hello im Elena Rodriguez Lancho 😄
                                I am the one who does magic to make our projects
                                looks so good. I am a photographer, editor and designer
                            </p>
                            <ul>
                                <li><a title={"Elena´s Instagram"} href={"https://www.instagram.com/elenalancho_/?hl=es"}
                                       target={"_blank"} alt={"Elenás Instagram"} rel={"noreferrer"}>
                                    <i className={"fab fa-instagram-square fa-3x"}/>
                                </a>
                                </li>
                                <li>
                                    <a title={"Elena´s Twitter"} alt={"Elena´s Twitter"} href={"https://twitter.com/elenalancho?lang=es"}
                                       target={"_blank"} rel={"noreferrer"}>
                                        <i className={"fab fa-twitter-square fa-3x"}/>
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </section>
            </section>
        </main>
            <footer id={"contact-me"}>
                <section className={"footer-content"}>
                    <form action={"."} onSubmit={(e) => checkAndSendEmail(e)}>
                        <fieldset>
                            <legend title={"Send us and email"}>Email ?</legend>
                            <input type={"text"} name={"subject"} id={"subject"} aria-label={"subject"}
                                onChange={(e) => setSubject(e.target.value)}
                                   placeholder="Subject"  required={true}/>
                            <textarea name="message" id="message" title="Your message"
                                onChange={(e) => setText(e.target.value)}
                                      placeholder={"Hello SurfBetter 🖖"} required={true}/>
                            <input className={"buttonBlue"} type={"submit"} value={"Send"}/>
                        </fieldset>
                    </form>
                    <div className="footerInfo">
                        <p>
                            {"⌨️ with ❤️ by © 2021"}
                                <a alt={"infolojo`s web"} href={"https://www.infolojo.es"}
                                   target={"_blank"} rel={"noreferrer"}><b>{"INFOLOJO"}</b></a>{"🧑‍💻."}<br/>
                            {"I´m open source. Just ❤️ GitHub."}
                        </p>
                        <a href={"https://github.com/ajloinformatico"} rel={"noreferrer"} target="_blank" alt="go to my github">
                            <img src={"https://img.icons8.com/doodle/48/000000/repository.png"} alt={"github link"}/>
                        </a>


                    </div>
                </section>
            </footer>
        </div>
    )
}
export default Contact