import React from "react";
import StarRatings from "react-star-ratings";

/**
 * Beaches Host
 * @returns {JSX.Element}
 * @constructor
 */
const StarComponent = (props) => {
    return (
        <div>
            <StarRatings
                rating={props.rating}
                starRatedColor={"#FFA62B"}
                starEmptyColor={"#000"}
                starDimension={"30px"}
                starSpacing={"5px"}
            />
        </div>
    )
};
export default StarComponent;