import React, {Suspense, lazy} from "react";
import Beaches from "./Beaches";
const HeaderMenu = lazy(() => import("../HeaderMenu.jsx"))
const AllBeaches = lazy(() => import("./Beaches"))



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
                <AllBeaches/>
            </Suspense>
        </div>
    )
}
export default BeachesHost;