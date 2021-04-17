import  React, {useState, useEffect} from "react";
//img must because import here
import slider1 from '../../assets/img/slider/slider1.jpg'
import slider2 from '../../assets/img/slider/slider2.jpg'
import slider3 from '../../assets/img/slider/slider3.jpg'

import HeaderLoginRegister from "./HeaderLoginRegister.jsx"

//Sign in and Login Modals
import SignInModal from "./SignInModal.jsx";
import LoginModal from "./LoginModal.jsx";



/**
 * Load login component
 * @returns {JSX.Element}
 * @constructor
 */
const LoginRegister = () => {



    /**
     * Use state for snackbar state (img being show)
     */
    const [slideBarState, setSlideBarState] = useState(1)

    useEffect(() => {
        showSlide(0)
    })

    /**
     * Change slideBar image byh an index
     * if the state of the slide is less than the number that 1 leaves
     * the state in the number of divs so that it jumps to the first
     * if the state of the slide is less than the number that 1 leaves
     * the state in the number of divs so that it jumps to the first
     *
     * Before that set display none or block and set correct index
     *
     * @param {number} n : index 1 right, -1 left
     */
    const showSlide = (n) => {
        let index = slideBarState
        index += n
        const x = document.getElementsByClassName('slide');
        // Note: if state of slide is bigger thant slides divs set one
        index > x.length?index = 1:console.log("go one")
        // Note: if the state of the slide is less than the number that 1 leaves
        // the state in the number of divs so that it jumps to the first
        index < 1?index = x.length:console.log("go last")
        // Note: Load styles none and block
        for(let i = 0; i < x.length;i++){
            x[i].style.display = "none";
        }
        x[index-1].style.display = "block";
        setSlideBarState(index)
    }

    return (
        <div>
            <HeaderLoginRegister/>
        <main className={"logSignMain"}>
            {/*SlideBar*/}
            <section className={"slideBar"}>
                <div className={"slide"}>
                    <p>
                        A tool for the soul<br/>
                        for any surfer
                    </p>
                    <img srcSet={slider1} alt={"slider first item"}/>
                 </div>
                <div className={"slide"}>
                    <p>
                        Find the best waves<br/>
                        of our bay
                    </p>
                    <img srcSet={slider2} alt={"slider second item"}/>
                </div>
                <div className={"slide"}>
                    <p>
                        Meet, compete and become<br/>
                        the best surfer in your area
                    </p>
                    <img srcSet={slider3} alt={"slider third item"}/>
                </div>
                {/*syle in line to cover the design point*/}
                <div className={"sliderButtons"}>
                    <a style={{color: 'black'}} onClick={e => showSlide(-1)}>&#10094;</a>
                    <a style={{color: 'black'}} onClick={e => showSlide(1)}>&#10095;</a>
                </div>
            </section>
            <section className={"containMain"}>
                <h2>Tired of not having a chance to enjoy your favorite sport?</h2>
                <p>
                    We are also SURFERS developers and we have the pleasure of presenting you our service.
                    Here you will find comprehensive and detailed information about our beaches of our bay.
                    Being able to know their status in real time, In order to choose the correct
                    option whenever you want to surf. Click Sign in and configure your profile. <strong>A social network
                    of beaches is waiting for you !!!</strong>
                </p>
            </section>
            {/*Modal log in by label for on header*/}
            <input type={"checkbox"} id={"btn-modal-sign-in"}/>
            <SignInModal/>
            <input type={"checkbox"} id={"btn-modal-log-in"}/>
            <LoginModal/>
        </main>
        </div>
    )
}

export default LoginRegister