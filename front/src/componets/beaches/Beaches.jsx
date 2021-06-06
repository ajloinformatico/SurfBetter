import React, {useEffect, useState} from "react";
import BeachBox from "./BeachCard";
import swal from "sweetalert";


const Beaches = () => {
    const [beaches, setBeaches] = useState([]);
    const [searchText, setSearchText] = useState("")
    /**
     * UsseEfect to get User Name
     */
    useEffect(() => {
        getBeaches().then(/*NO-LOOP*/);
    }, []);

    const getBeaches = async () => {
        fetch("/api/beaches")
            .then(response => response.json())
            .catch(error => async () => {
                await swal("Error", "Something was wrong",{icon:"warning"}).then(/*NO-LOOP*/)
            })
            .then(beachesInfo => setBeaches(beachesInfo));
    };


    const searchBeaches = async (e) => {
        e.preventDefault()
        if (!searchText.trim()) {
            await getBeaches()
        } else {
            setBeaches([])
            fetch(`http://localhost:5000/api/beach/filter/${searchText}`)
                .then(response => response.json())
                .catch(() => async () => {
                    await swal("Error", "Something was wrong", {icon: "warning"}).then(/*NO--LOP*/)
                })
                .then(beachesInfo => setBeaches(beachesInfo));
        }
    };


    return (
        <div>
            <h1>Beaches</h1>

            <form className={"beachSearch"} action={"."} onSubmit={( e) =>  searchBeaches(e)}>
                <input type={"text"} onChange={(e) => setSearchText(e.target.value)} name={"text"}
                id={"text"} aria-label={"text"} placeholder={"Search beach"}/>
                <input className={"buttonBlue"} type={"submit"} value={"Search"}/>
            </form>

            <section className={"contentBeaches"}>
                { /*Loop by map to set beaches*/
                    (beaches[0]!==undefined&&beaches[0]!==null)&&(
                        beaches.map(it => {
                            return(
                                //Note: pass id and where is from by props
                                <BeachBox key={it.id} beach={it} from={"beaches"}/>
                            )
                        })
                    )
                }
            </section>
        </div>
    )
}
export default Beaches;