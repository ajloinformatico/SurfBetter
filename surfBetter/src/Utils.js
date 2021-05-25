import {useEffect, useState} from "react";
import {authFetch} from "./componets/auth/auth";

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

