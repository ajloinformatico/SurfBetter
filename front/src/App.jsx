import React, {lazy, Suspense} from "react";
import {useHistory} from "react-router-dom";
import './assets/css/style.scss';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Redirect,
} from "react-router-dom";
import LoginRegister from './componets/loginsign/LoginRegister.jsx';
import Profile from './componets/profile/Profile.jsx';
import BeachesHost from "./componets/beaches/BeachesHost";
import Contact from './componets/Contact.jsx';
import LegalNotices from './componets/LegalNotices.jsx';
import BeachInfo from "./componets/beaches/BeachInfo";
import {useAuth} from "./componets/auth/auth.jsx";
import ScrollButton from "./componets/widgets/ScrollButton";
import MapHost from "./componets/map/MapHost";
// Note: Just to check if i can do fetch


/**
 * 
 * @returns {jsx commponent with routes and user}
 */
function App() {
    //LOVE REACT RETURNS AUTH USER
    const [logged] = useAuth();

    //History
    const history = useHistory();

    return (
        <Router history>
            <Switch>
                {/*Public route*/}
                <Route path="/login" exact>
                    <LoginRegister history={history} />
                    <ScrollButton/>
                </Route>
                {
                    !logged&&
                        <Redirect to="login"/>
                }
                {/*Protected rouetes*/}
                <Route path="/" exact>
                    <BeachesHost/>
                    <ScrollButton/>
                </Route>
                <Route path="/beaches" exact>
                    <BeachesHost/>
                    <ScrollButton/>
                </Route>
                <Route path="/contact" exact>
                    <Contact/>
                    <ScrollButton/>
                </Route>
                <Route path="/profile" exact>
                    <Profile/>
                    <ScrollButton/>
                </Route>
                <Route path="/map" exact>
                    <MapHost/>
                    <ScrollButton/>
                </Route>
                <Route path="/legal" exact>
                    <LegalNotices/>
                    <ScrollButton/>
                </Route>
                <Route path="/beach/:id" exact>
                    <BeachInfo/>
                    <ScrollButton/>
                </Route>
                <Route path="/*">
                    <h1>ERROR 404: NOT FOUND</h1>
                    <ScrollButton/>
                </Route>
            </Switch>
        </Router>
    );
}



export default App;
