/* eslint-disable jsx-a11y/anchor-is-valid */
import React from "react";
import {useHistory} from "react-router-dom";

/**
 * Common footer */
const Footer = () => {

    const history = useHistory()


    return (
        <footer className={"CommonFooter"}>
            <section>
            <div>
                <h2>SurfBetter</h2>
                <p>The best gadget for the surfers</p>
            </div>
            <div>
                <h3>Contact</h3>
                <p>Go to <a alt={"go contact"} rel={"noreferrer"} onClick={() => history.push("/contact")}>Contact page</a> and find out about us</p>
                <p>Send email or visit our social networks</p>
            </div>
            <div>
                <h3>Web Map</h3>
                <ul>
                    <li>
                        <a alt={"go to beaches"} rel={"noreferrer"} onClick={() => history.push("/beaches")}>Home</a>
                    </li>
                    <li>
                        <a alt={"go to contact"} rel={"noreferrer"} onClick={() => history.push("/contact")}>Contact</a>
                    </li>
                    <li>
                        <a alt={"go to profile"} rel={"noreferrer"} onClick={() => history.push("/profile")}>Profile</a>
                    </li>
                    <li>
                        <a alt={"go to map"} rel={"noreferrer"} onClick={() => history.push("/map")}>Maps</a>
                    </li>
                </ul>
            </div>
            <div>
                <h3>Legal</h3>
                <a alt={"go to legal notices"} rel={"noreferrer"} onClick={() => history.push("/legal")}>Legal Notices</a>
            </div>
            </section>
            <section className="footerInfo">
                <p>
                    {"⌨️ with ❤️ by © 2021"}
                    <a alt={"infolojo`s web"} rel={"noreferrer"} href={"https://www.infolojo.es"}
                       target={"_blank"}><b>{"INFOLOJO"}</b></a>{"🧑‍💻."}<br/>
                    {"I´m open source. Just ❤️ GitHub."}
                </p>
                <a href="https://github.com/ajloinformatico" rel={"noreferrer"} target="_blank" alt="go to my github">
                    <img src="https://img.icons8.com/doodle/48/000000/repository.png" alt={"github link"}/>
                </a>
            </section>
        </footer>
    );
};


export default Footer;