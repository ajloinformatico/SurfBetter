import React, {useEffect, useState} from "react";
import Map from "./Map";
import HeaderMenu from "../HeaderMenu";
import mapsKey from "../../credentials/credentials";
import {mapLight, mapDark} from "./mapStyle";
import swal from "sweetalert";


const  GOOGLE_MAP_URL=`https://www.google.com/maps/api/js?&key=${mapsKey.mapsKey}`;

/**
 * MapHost component
 * @returns {JSX.Element}
 * @constructor
 */
const MapHost = (props) => {
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
            .then(response => setBeaches(response))
    };

    /**
     * Set Map on JSX element if markers are diferent of defined
     * change style 
     * @returns {JSX.Element}
     */
    const setMap = () => {
        if (props.darkMode){
            return(
                <Map
                    mapStyle={mapDark}
                    markers={beaches}
                    googleMapURL={GOOGLE_MAP_URL}
                    containerElement={<div style={{height: '90vh'}}/>}
                    mapElement={<div style={{height: '100%'}}/>}
                    loadingElement={<i className={"fas fa-spinner fa-4x fa-rotate-90"}/>}
                />);
        } else {
            return(
                <Map
                    mapStyle={mapLight}
                    markers={beaches}
                    googleMapURL={GOOGLE_MAP_URL}
                    containerElement={<div style={{height: '90vh'}}/>}
                    mapElement={<div style={{height: '100%'}}/>}
                    loadingElement={<i className={"fas fa-spinner fa-4x fa-rotate-90"}/>}
                />);
        }
        
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