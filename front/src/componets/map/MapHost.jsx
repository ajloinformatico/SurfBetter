import React, {useEffect, useState} from "react";
import Map from "./Map";
import HeaderMenu from "../HeaderMenu";
import mapsKey from "../../credentials/credentials";
import swal from "sweetalert";


const  GOOGLE_MAP_URL=`https://www.google.com/maps/api/js?&key=${mapsKey.mapsKey}`;

/**
 * MapHost component
 * @returns {JSX.Element}
 * @constructor
 */
const MapHost = () => {
    const [beaches, setBeaches] = useState([]);

    useEffect(() => {
        getBeaches().then(/*NO-LOOP*/);
    },[]);

    const getBeaches = async () => {
        fetch("/api/beaches")
            .then(response => response.json())
            .catch(() => async () => {
                await swal("Error", "Markers not found", {icon: "warning"}).then(/*NO-LOOP*/)
            })
            .then(async response => await setBeaches(response))
    };

    /**
     * Ser Map on JSX element if markers are diferent of defined
     * @returns {JSX.Element}
     */
    const setMap = () => {
        return(<Map
            markers={beaches}
            googleMapURL={GOOGLE_MAP_URL}
            containerElement={<div style={{height: '90vh'}}/>}
            mapElement={<div style={{height: '100%'}}/>}
            loadingElement={<i className={"fas fa-spinner fa-4x fa-rotate-90"}/>}
        />);
    };

    return (
        <div>
            <HeaderMenu/>
            {
                (beaches[0]!==undefined&&beaches[0]!==null)&&(setMap())
            }
        </div>
    );
};
export default MapHost;