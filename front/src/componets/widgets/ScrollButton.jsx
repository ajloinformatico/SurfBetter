import React, {useState} from "react";


const ScrollButton = () => {
    const [visible, setVisible] = useState(false);

    const toggleVisible = () => {

        const scrollTop = document.documentElement.scrollTop;
        if (scrollTop > 300){
            setVisible(true);
        } else if (scrollTop <= 300){
            setVisible(false);
        }
    };

    /**
     * Do scroll
     */
    const scrollToTop = () =>{
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    };

    window.addEventListener('scroll',toggleVisible);

    return (
        /*show if its visible*/
        visible&&(
            /*Set event listener on toggleVisible*/
            <span id={"scroll-button"} onClick={() => scrollToTop()}>
                <i className="fas fa-arrow-alt-circle-up fa-2x"/>
            </span>
        )
    )
}

export default ScrollButton;