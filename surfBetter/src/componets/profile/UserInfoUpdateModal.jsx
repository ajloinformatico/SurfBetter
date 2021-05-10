/* eslint-disable jsx-a11y/anchor-has-content */
/* eslint-disable jsx-a11y/anchor-is-valid */
import React,{useState} from 'react'
import logoSurfBetterHeader from '../../assets/img/common/logoSurfBetterHeader.png'
import { authFetch } from '../auth/auth'



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
    const [description, setDescription] = useState("")

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
     * set the error
     * @param {useState} state 
     * @param {target} input 
     * @param {min_max} min and max
     */
    const setError = (state, input, min_max) => {
        let error = false
        if (!state.trim()) {
            input.placeholder = input.id + " is empty";
            error = true
        } else if (!checkStrings(state, min_max[0], min_max[1])) {
            input.placeholder = input.id + " is not valid"
            error = true            
        }
        if (!error) 
            return false
        
        input.classList.add("errors")
        input.value = ""
        return true
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
                setError(name, input, [2, 64])&&setName("")
                break;
            case ("surname") :
                setError(surname, input, [2,64])&&setSurname("")
                break;
            case ("nick") :
                setError(nick, input, [2, 30])&&setNick("")
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
            case ("description") :
                if (description.length > 64) {
                    input.classList.add("errors");
                    input.value = "";
                    input.placeholder = input.id + " isn't valid";
                    setDescription("");
                }
                break;
            default :
                break;
        }
    }

    const updateUser =  async e => {
        e.preventDefault()
        const errorSpan = document.querySelector('.errorForms')
        errorSpan.innerHTML = " "
        
        const opts = {
            "name" : name,
            "surname" : surname,
            "nick" : nick,
            "email" : email,
            "description" : description
        }
        authFetch('/api/userupdate', {
            method: 'PUT',
            body: JSON.stringify(opts)
        }).then(response => response.json())
            //TODO: MODAL TO SHOW INFO
        .catch(errorSpan.innerHTML = "user or password is allready in use")
        .then(response => {
            console.log(response)
                alert("Your data has been updated succsses") 
                window.location.reload()
        })
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
                        action={'.'}
                        onSubmit={e => updateUser(e)}>
                        <h2>Update user info</h2>
                        <fieldset className={"modalInputs"}>
                            {/* eslint-disable-next-line jsx-a11y/aria-props*/}
                            <input type={"text"} id={"name"} name={"name"} aria-labe={"name"}
                                onChange={e => setName(e.target.value)} onBlur={e => checkInputs(e)}
                                size={30} title={"Please input a valid name"} placeholder={props.user.name}
                                required={true}/>
                                
                            <input type={"text"} id={"surname"} name={"surname"} aria-label={"surname"}
                               onChange={e => setSurname(e.target.value)} onBlur={e => checkInputs(e)}
                               size={30} title={"Please input a valid surname"} placeholder={props.user.surname} 
                               required={true}/>

                            <input type={"text"} id={"nick"} name={"nick"} aria-label={"nick"}
                               onChange={e => setNick(e.target.value)} onBlur={e => checkInputs(e)}
                               size={30} title={"Please input a valid nick"} placeholder={props.user.nick} 
                               required={true}/>

                            <input type={"email"} id={"email"} name={"email"} title={"Please enter a valid email *"}
                               onChange={e => setEmail(e.target.value)} onBlur={e => checkInputs(e)}
                               size={30} aria-label={"email"} placeholder={props.user.email} 
                               required={true}/>
                            
                            <textarea name="description" id="description" title="new description" placeholder={props.user.description}
                                onChange={e => setDescription(e.target.value)} onBlur={e => checkInputs(e)}
                            />
                            <span className="errorForms"></span>

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
