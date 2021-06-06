import React, {useState} from "react";
import {GoogleMap, withScriptjs, withGoogleMap, InfoWindow} from "react-google-maps";
import Marker from "react-google-maps/lib/components/Marker";
import {useHistory} from "react-router-dom";
import MapStyle from "./mapStyle";
import StarComponent from "../beaches/StarComponent";


/**
 * Map Component
 * @param props
 * @returns {JSX.Element}
 * @constructor
 */
const Map = (props) => {

    const markers = props.markers
    const [selectMarker, setSelectMarker] = useState(null);
    const history = useHistory();


    const goToDetail = (id) => {
        history.push(`/beach/${id}/map`)
    };

    /**
     * Calculate the mean. I have decided to do it like this to follow Javi's
     * advice not to leave all the work to the server
     * @param it: Beach
     * @returns {int}
     */
    const calculateMedia = (it) => {
        let sum = 0
        let len = 0
        for (const property in it) {
            if (it[property] in [0,1,2,3,4,5] && it[property].toString.length === 1){
                sum += it[property]
                len++
            }
        }
        return sum/len;
    }


    return (
        <GoogleMap
            defaultZoom={7.8}
            defaultCenter={{lat: 37.3280626, lng: -5.6975306}}
            defaultOptions={{ styles: MapStyle }}
        >
        {
            //Set Markers
            markers[0]!==undefined&&(
                markers.map(marker => (
                        <Marker
                            key={marker.id}
                            icon={{url:"http://maps.google.com/mapfiles/ms/icons/blue-dot.png"}}
                            position={{lat:marker.latitude,lng:marker.longitud}}
                            onClick={() => {
                               setSelectMarker(marker)
                            }}
                            onMouseOver={() => {
                               setSelectMarker(marker)
                            }}
                        />
                    )
                )
            )
        }
        {   //Note: Set InfoWindows
            selectMarker&&(
                <InfoWindow
                    position={{lat:selectMarker.latitude,lng:selectMarker.longitud}}
                    onCloseClick={() => {setSelectMarker(null)}}
                >
                    <div className={"infoWindow"} onClick={async () => {
                        await goToDetail(selectMarker.id)
                    }}>
                        <h3>{selectMarker.name}</h3>
                        <StarComponent rating={calculateMedia(selectMarker)}/>
                            <p>OpenDetail</p><i className={"fas fa-info-circle fa-2x"}/>
                    </div>
                </InfoWindow>
            )
        }
        </GoogleMap>
    )
}

/** Inject needed props*/
export default withScriptjs(
    withGoogleMap(Map)
);