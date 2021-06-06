import React from "react";
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
import Footer from "./componets/Footer";
import HeaderMenu from "./componets/HeaderMenu";
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
                <Route path="/legal" exact>
                    <LegalNotices/>
                    <Footer/>
                    <ScrollButton/>
                </Route>
                {
                    !logged&&
                        <Redirect to="login"/>
                }
                {/*Protected rouetes*/}
                <Route path="/" exact>
                    <BeachesHost/>
                    <Footer/>
                    <ScrollButton/>
                </Route>
                <Route path="/beaches" exact>
                    <BeachesHost/>
                    <Footer/>
                    <ScrollButton/>
                </Route>
                <Route path="/contact" exact>
                    <Contact/>
                    <ScrollButton/>
                </Route>
                <Route path="/profile" exact>
                    <Profile/>
                    <Footer/>
                    <ScrollButton/>
                </Route>
                <Route path="/map" exact>
                    <MapHost/>
                    <Footer/>
                    <ScrollButton/>
                </Route>
                <Route path="/beach/:id/:back" exact>
                    <BeachInfo/>
                    <Footer/>
                    <ScrollButton/>
                </Route>
                <Route path="/*">
                    <HeaderMenu/>
                    <h1>ERROR 404: NOT FOUND</h1>
                    <Footer/>
                    <ScrollButton/>
                </Route>
            </Switch>
        </Router>
    );
}



export default App;
