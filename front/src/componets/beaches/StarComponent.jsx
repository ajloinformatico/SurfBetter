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
        (localStorage.getItem("theme") === "darkMode")?(
            setDarkModeEnable(true)
        ):(
            setDarkModeEnable(false)
        )
    },[darkModeEnable])

    return (
        <div>
            {
                darkModeEnable?(
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