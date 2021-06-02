import {useEffect, useState} from "react";
import {authFetch} from "./componets/auth/auth";
import swal from "sweetalert";

/**
 * Get user
 * @returns {{}: Object return user object}
 */
export const getUser = () => {
    let user = {}
        authFetch("/api/current_user")
            .then(response => response.json())
            .catch(error => console.log(error))
            .then(userInfo => {
                user = userInfo
            })
    return user
}

/**
 * Util method chacke string by min, max and not numbers inside it
 * @param cadena char where search for errors
 * @param min min size
 * @param max max size
 * @returns {boolean} valid or invalid
 */
export const checkStrings = (cadena, min, max) => {
    let flag = false
    if (cadena.length > min && cadena.length < max){
        cadena.split("").forEach(element => {
            if (element !== " " &&  !isNaN(element)) {
                console.log("i have found a number");
                flag = true;
            }
        })
    } else {
        flag = true
    }
    return !flag;
}

export const isLikeFromUser = (likes, user_id) => {
    let result = ""
    likes.forEach(it => {
        (it.user_id===user_id)&&(result = "red-flag")
    })
    return result
}

/**
 * set the error
 * @param {string} state
 * @param {target} input
 * @param {min_max} min and max
 */
export const setError = (state, input, min_max) => {
    let error = false
    if (!state.trim()) {
        input.placeholder = input.id + " is empty";
        error = true
    } else if (!checkStrings(state, min_max[0], min_max[1])) {
        input.placeholder = input.id + " is not valid"
        error = true
    }
    if (!error)
        return false

    input.classList.add("errors")
    input.value = ""
    return true
}


/**
 * Calculate likes of a beach or comment
 * @param likes
 * @returns {number}
 */
export const calculateLikes = (likes) => {
    let counter = 0
    likes.forEach(() => {
        counter++;
    })
    return counter
}


