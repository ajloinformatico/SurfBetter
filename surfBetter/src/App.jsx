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
import LoginRegister from './componets/loginsign/LoginRegister.jsx'
import Profile from './componets/profile/Profile.jsx'
import Beaches from './componets/Beaches.jsx'
import Contact from './componets/Contact.jsx'
import Resources from './componets/Resources.jsx'
import LegalNotices from './componets/LegalNotices.jsx'

//Auth
import {authFetch,  useAuth} from "./componets/auth/auth.jsx"
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

    //const [serverStatus, setServerStatus] = useState(null)

        /**
         * UsseEfect to get User Name
         */
        useEffect(() => {
            authFetch("/api/current_user")
                .then(response => response.json())
                .catch(error => console.log(error))
                .then(userInfo => setUser(userInfo))
        }, [])

        
    return (
        <Router history>
            <Switch>
                {/*Public route*/}
                <Route path="/login" exact>
                    <LoginRegister/>
                </Route>
                {
                    !logged&&
                        <Redirect to="login"/>
                }
                {/*Protected rouetes*/}
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
