import React, {useEffect, useState} from "react";
import './assets/css/style.scss';
// Font awesome
// routes import
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Redirect,
} from "react-router-dom";

//Componnets
import LoginRegister from './componnets/loginsign/LoginRegister.jsx'
import Profile from './componnets/Profile.jsx'
import Beaches from './componnets/Beaches.jsx'
import Contact from './componnets/Contact.jsx'
import Resources from './componnets/Resources.jsx'
import LegalNotices from './componnets/LegalNotices.jsx'
import ServerError from './componnets/ServerError.jsx'

//Auth
import {authFetch,  useAuth} from "./componnets/auth/auth.jsx"
// Note: Just to check if i can do fetch






/**
 * 
 * @returns {jsx commponent with routes and user}
 */
function App() {


    //TODO: Maybe i might need it
    // eslint-disable-next-line no-unused-vars
    const [user, setUser] = useState({})
     
    //LOVE REACT RETURNS AUTH USER
    const [logged] = useAuth()

    const [serverStatus, setServerStatus] = useState(true)

        useEffect(() => {
            fetch("/api/")
            .catch(setServerStatus(false))
        })

        /**
         * UsseEfect to get User Name
         */
        useEffect(() => {
                //fetch("/api").then(resp => resp.json()).then(resp => console.log(resp))
            authFetch("/api/current_user")
                .then(response => response.json())
                .catch(error => console.log(error))
                .then(userInfo => setUser(userInfo))
        }, [])
        
    return (
        <Router history>
            <Switch>
                {/*Route for not runing server*/}
                <Route path="/server_error" exact>
                    <ServerError serverStatus={serverStatus}/>
                </Route>
                {
                    !serverStatus&&<Redirect to="server_error"/>
                }

                <Route path="/login" exact>
                    <LoginRegister/>
                </Route>
                { //Check if user is loged to redirect or stay here
                    !logged&&<Redirect to="login"/>
                }
                
                {/*Protected royetes*/}
                <Route path="/" exact>      
                    <Beaches/>
                </Route>
                <Route path="/beaches" exact>
                    <Beaches/>
                </Route>
                <Route path="/contact" exact>
                    <Contact/>
                </Route>
                <Route path="/profile" exact>
                    <Profile user={user}/>
                </Route>
                <Route path="/resources" exact>
                    <Resources/>
                </Route>
             
                <Route path="/legal" exact>
                    <LegalNotices/>        
                </Route>
                <Route path="/*">
                    <h1>ERROR 404: NOT FOUND</h1>
                </Route>
            </Switch>
        </Router>
    );
}



export default App;
