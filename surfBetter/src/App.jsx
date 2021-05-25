import React, {lazy, Suspense} from "react";
import {useHistory} from "react-router";
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
import BeachesHost from "./componets/beaches/BeachesHost";
import Contact from './componets/Contact.jsx'
import Resources from './componets/Resources.jsx'
import LegalNotices from './componets/LegalNotices.jsx'
import BeachInfo from "./componets/beaches/BeachInfo";



//Auth
import {useAuth} from "./componets/auth/auth.jsx"
// Note: Just to check if i can do fetch





/**
 * 
 * @returns {jsx commponent with routes and user}
 */
function App() {
    //LOVE REACT RETURNS AUTH USER
    const [logged] = useAuth()

    //History
        //Note: React route const to change page
    const history = useHistory()
    


        
    return (
        <Router history>
            <Switch>
                {/*Public route*/}
                <Route path="/login" exact>
                    <LoginRegister history={history} />
                </Route>
                {
                    !logged&&
                        <Redirect to="login"/>
                }
                {/*Protected rouetes*/}
                <Route path="/" exact>
                    <BeachesHost/>
                </Route>
                <Route path="/beaches" exact>
                    <BeachesHost/>
                </Route>
                <Route path="/contact" exact>
                    <Contact/>
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
                <Route path="/beach/:id" exact>
                    <BeachInfo/>
                </Route>
                <Route path="/*">
                    <h1>ERROR 404: NOT FOUND</h1>
                </Route>
            </Switch>
        </Router>
    );
}



export default App;
