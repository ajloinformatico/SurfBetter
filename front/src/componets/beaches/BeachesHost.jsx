import React, {Suspense, lazy} from "react";
//import Beaches from "./Beaches";
const HeaderMenu = lazy(() => import("../HeaderMenu.jsx"))
const Beaches = lazy(() => import("./Beaches"))



/**
 * Beaches Host
 * @returns {JSX.Element}
 * @constructor
 */
const BeachesHost = () => {
    return (
        <div>
            <Suspense fallback={<i className="fas fa-spinner fa-4x fa-rotate-90"/>}>
                <HeaderMenu/>
                <Beaches/>
            </Suspense>
        </div>
    )
}
export default BeachesHost;