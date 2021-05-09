/* eslint-disable jsx-a11y/anchor-has-content */
/* eslint-disable jsx-a11y/anchor-is-valid */
import React,{useState} from 'react'
import logoSurfBetterHeader from '../../assets/img/common/logoSurfBetterHeader.png'



//TODO: USER CURRENT INFO CHANGE
/* *
 * 
 * @param props: user state
 * @returns {JSX.Component}
 */
const UserCurrentInfoModal = (props) => {

    const [email, setEmail] = useState("")
    const [name, setName] = useState("")
    const [nick, setNick] = useState("")
    const [surname, setSurname] = useState("")

    /* *
     * Check if string is correct by checking legth and not numbers
     * @param cadena
     * @param min
     * @param max
     * @returns {boolean}
     */
       const checkStrings = (cadena,min,max) => {
        let flag = false
        if (cadena.length > min && cadena.length < max){
            cadena.split("").forEach(element => {
                if (!isNaN(element)) {
                    console.log("i have found a number");
                    flag = true;
                }
            })
        } else {
            flag = true
        }
        return !flag;
    }

    /**
     * Client check user update modal
     * @param {event} e 
     */
    const checkInputs = (e) => {
        const input = e.target;
        input.classList.remove("errors");
        const mailReg = new RegExp(/^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i);
        switch (input.id) {
            case ("name") : 
                if(!name.trim()){
                    input.classList.add("errors");
                    input.placeholder = input.id + " is empty";

                } else if (!checkStrings(name, 2, 64)) {
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " isn't valid";
                    setName("");
                }
                break;
            case ("surname") :
                if (!surname.trim()) {
                    input.classList.add("errors");
                    input.placeholder = input.id + " is empty";
                } else if (!checkStrings(surname, 2, 64)) {
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " isn't valid";
                    setSurname("");
                }
                break;
            case ("nick") :
                if (!nick.trim()) {
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " is empty";
                    setNick("");
                } else if (!checkStrings(nick, 2, 30)){
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " isn't valid";
                    setNick("");
                }
                break;
            case ("email") :
                if (!email.trim()) {
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " is empty";
                    setEmail("");
                }
                else if (email.length > 130 || email.length < 4 || !mailReg.test(email)) {
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " isn't valid";
                    setEmail("");
                }
                break;
            default :
                break;
        }
    }


    const updateUser = async e => {
        alert("Actualizte")
    }

    const closeUserInfoOptions = () => {
        document.getElementById('user-info-option-modal').checked = false 
        document.getElementById('user-options-modal').checked = true
    }

    return (
        <section className={"modalUserInfoUpdate"}>
            <div className={"container"}>
                {/*Header modal*/}
                <header>
                    <img srcSet={logoSurfBetterHeader} alt={"logo SurfBetter"}
                    title={"SurfBetter logo"}/>
                    <a title={"exit"}  onClick={() => closeUserInfoOptions()} className={"fas fa-arrow-left fa-2x"}/>
                </header>
                
                <div className={"contentModal"}>
                    <form id={"update-form"} 
                        onSubmit={e => updateUser(e)}
                        encType={"multipart/formdata"}>
                        <h2>Update user info</h2>
                        <fieldset className={"modalInputs"}>
                            {/* eslint-disable-next-line jsx-a11y/aria-props*/}
                            <input type={"text"} id={"name"} name={"name"} aria-labe={"name"}
                                onChange={e => setName(e.target.value)} onBlur={e => checkInputs(e)}
                                size={30} title={"Please input a valid name"} placeholder={"New user name *"}
                                required={true}/>
                                
                            <input type={"text"} id={"surname"} name={"surname"} aria-label={"surname"}
                               onChange={e => setSurname(e.target.value)} onBlur={e => checkInputs(e)}
                               size={30} title={"Please input a valid surname"} placeholder={"User Surname"} 
                               required={true}/>

                            <input type={"text"} id={"nick"} name={"nick"} aria-label={"nick"}
                               onChange={e => setNick(e.target.value)} onBlur={e => checkInputs(e)}
                               size={30} title={"Please input a valid nick"} placeholder={"User Nick *"} 
                               required={true}/>

                            <input type={"email"} id={"email"} name={"email"} title={"Please enter a valid email *"}
                               onChange={e => setEmail(e.target.value)} onBlur={e => checkInputs(e)}
                               size={30} aria-label={"email"} placeholder={"Email *"} 
                               required={true}/>
                        </fieldset>
                        <fieldset className={"modalButtonSingle"}>
                            <input className={"buttonBlue"} type={"submit"} value="Update"/>
                        </fieldset>
                    </form>
                </div>
            </div>
        </section>
    )
}

export default UserCurrentInfoModal
