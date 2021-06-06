import React, {useEffect, useState} from "react";
import StarRatings from "react-star-ratings";

/**
 * Beaches Host
 * @returns {JSX.Element}
 * @constructor
 */
const StarComponent = (props) => {

    
    const [darkModeEnable, setDarkModeEnable] = useState(false)

    useEffect(() =>{
        setBackGround()
    })

    /**
     * TODO: TERMINAR con la kookie
     * Change back style color
     * @returns {string}
     */
    const setBackGround = async () => {
        const htmlTarget = document.querySelector('html');
        if (htmlTarget.classList.contains("darkMode")) {
            setDarkModeEnable(true)
        } else {
            setDarkModeEnable(false)
        }
    }

    return (
        <div>
            {
                darkModeEnable===true?(
                    <StarRatings
                        rating={props.rating}
                        starRatedColor={"#FFA62B"}
                        starEmptyColor={"#FFF"}
                        starDimension={"30px"}
                        starSpacing={"5px"}
                    />
                ):(
                    <StarRatings
                        rating={props.rating}
                        starRatedColor={"#FFA62B"}
                        starEmptyColor={"#000"}
                        starDimension={"30px"}
                        starSpacing={"5px"}
                    />
                )
            }
        </div>
    )
};
export default StarComponent;