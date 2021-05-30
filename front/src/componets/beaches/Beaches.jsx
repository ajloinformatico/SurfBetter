import React, {useEffect, useState} from "react";
import BeachBox from "./BeachCard";



const Beaches = () => {
    const [beaches, setBeaches] = useState([])


    const getBeaches = async () => {
        fetch("/api/beaches")
            .then(response => response.json())
            .catch(error => console.log(error))
            .then(beacheInfo => setBeaches(beacheInfo))
    }


    /**
     * UsseEfect to get User Name
     */
    useEffect(async () => {
        await getBeaches()
    }, [])

    return (
        <div>
            <h1>Beaches</h1>
            <section className={"contentBeaches"}>
                { /*Loop by map to set beaches*/
                    beaches!==undefined&&(
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
//
// <div>
//     {it.description.slice(0,90) + " ..."}
// </div>