import React, {useEffect, useState} from "react";
import BeachBox from "./BeachCard";
import swal from "sweetalert";



const Beaches = () => {
    const [beaches, setBeaches] = useState([])

    /**
     * UsseEfect to get User Name
     */
    useEffect(() => {
        getBeaches()
        console.log(beaches)
    }, [])

    const getBeaches = async () => {
        fetch("/api/beaches")
            .then(response => response.json())
            .catch(error => async () => {
                await swal("Error", "Something was wrong",{icon:"warning"}).then(/*NO-LOOP*/)
            })
            .then(beachesInfo => setBeaches(beachesInfo))
    }

    return (
        <div>
            <h1>Beaches</h1>
            <section className={"contentBeaches"}>
                { /*Loop by map to set beaches*/
                    (beaches[0]!==undefined&&beaches[0]!==null)&&(
                        beaches.map(it => {
                            return(
                                <BeachBox beach={it}/>
                            )
                        })
                    )
                }
            </section>
        </div>
    )
}
export default Beaches;