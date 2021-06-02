import React, {useEffect, useState} from "react";
import Map from "./Map";
import HeaderMenu from "../HeaderMenu";
import mapsKey from "../../credentials/credentials";
import swal from "sweetalert";


const  GOOGLE_MAP_URL=`https://www.google.com/maps/api/js?v=3.exp&key=${mapsKey.mapsKey}`;

/**
 * MapHost component
 * @returns {JSX.Element}
 * @constructor
 */
const MapHost = () => {

    const [markers, setMarkers] = useState([]);

    useEffect(() => {
        getBeachesCords().then(/*NO-LOOP*/);
    },[]);

    const getBeachesCords = async () => {
        fetch("/api/beaches/coords")
            .then(response => response.json())
            .catch(() => async () => {
                await swal("Error", "Markers not found", {icon: "warning"}).then(/*NO-LOOP*/)
            })
            .then(response => setMarkers(response));
    };

    /**
     * Ser Map on JSX element if markers are diferent of defined
     * @returns {JSX.Element}
     */
    const setMap = () => {
        return(<Map
            markers ={markers}
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
                markers[0]!==undefined&&(setMap())

            }
        </div>
    );
};

export default MapHost;