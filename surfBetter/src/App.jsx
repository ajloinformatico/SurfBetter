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
import Options from './componnets/Options.jsx'
import Contact from './componnets/Contact.jsx'
import Resources from './componnets/Resources.jsx'
import LegalNotices from './componnets/LegalNotices.jsx'
import HeaderMenu from "./componnets/HeaderMenu.jsx";

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
    const [user, setUser] = useState(null)
    
    //LOVE REACT RETURNS AUTH USER
    const [logged] = useAuth()

        /**
         * UsseEfect to get User Name
         */
        useEffect(() => {
                //fetch("/api").then(resp => resp.json()).then(resp => console.log(resp))
        authFetch("/api/protected").then(response => {
            if (response.status !== 401){
                setUser(response.user)
                console.log(response)
                console.log(user)
            }
            }).then(response => {
                    (response&&response.user)&&setUser(response.user)
            })
        }, [])
        
    return (
        <Router history>
            <Switch>
                <Route path="/login" exact>
                    <LoginRegister/>
                </Route>
                { //Check if user is loged to redirect or stay here
                    !logged&&<Redirect to="login"/>
                }
                
                {/*Protected royetes*/}
                <HeaderMenu/>
                <Route path="/" exact>      
                    <Beaches/>
                </Route>
                <Route path="/beaches" exact>
                    <Beaches/>
                </Route>
                <Route path="/contact" exact>
                    <Contact/>
                </Route>
                <Route path="/options" exact>
                    <Options/>
                </Route>
                <Route path="/profile" exact>
                    <Profile/>
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
