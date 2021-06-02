import React, {useEffect, useState} from "react";
import {GoogleMap, withScriptjs, withGoogleMap, InfoWindow} from "react-google-maps";
import Marker from "react-google-maps/lib/components/Marker";
import swal from "sweetalert";
import {useHistory} from "react-router-dom";


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
        history.push(`/beach/${id}`)
    };

    return (

        <GoogleMap
            defaultZoom={7.8}
            defaultCenter={{lat: 37.3280626, lng: -5.6975306}}
        >
        {   //Set Markers
            markers!==undefined&&(
                markers.map(marker => {
                    return (
                        <Marker
                            key={marker.id}
                            position={{lat:marker.latitude,lng:marker.longitude}}
                            onMouseOver={() => {

                            }}
                            onClick={() => {
                                setSelectMarker(marker)
                            }}
                        />
                    )
                })
            )
        }
        {   //Set InfoWindow
            selectMarker!==null&&(
                <InfoWindow
                    position={{lat:selectMarker.latitude,lng:selectMarker.longitude}}
                    onCloseClick={() => {setSelectMarker(null)}}
                >
                    <div className={"infoWindow"}>
                        <h3>{selectMarker.name}</h3>
                        <span onClick={async () => {
                            await goToDetail(selectMarker.id)
                            }}>
                            <p>OpenDetail</p><i className={"fas fa-info-circle"}/>
                        </span>
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