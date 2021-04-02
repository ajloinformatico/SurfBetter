import './assets/css/style.scss';
// Font awesome
// routes import
import {
    BrowserRouter as Router,
    Switch,
    Route,
} from "react-router-dom";

import LoginRegister from './componnets/loginsign/LoginRegister.jsx'
import Profile from './componnets/Profile.jsx'
import Beaches from './componnets/Beaches.jsx'
import Options from './componnets/Options.jsx'
import Contact from './componnets/Contact.jsx'
import Resources from './componnets/Resources.jsx'
import LegalNotices from './componnets/LegalNotices.jsx'
import HeaderMenu from "./componnets/HeaderMenu.jsx";
import HeaderLoginRegister from "./componnets/loginsign/HeaderLoginRegister.jsx";
import React from "react";


function App() {
  return (
      <Router>
          <Switch>
              {
                  /*App routes*/
                  /*Exact is not necessary but I use it just in case it fails*/
              }
              <Route path="/" exact>
                  <HeaderMenu/>
                  <Beaches/>
              </Route>
              <Route path="/beaches" exact>
                  <HeaderMenu/>
                  <Beaches/>
              </Route>

              <Route path="/contact" exact>
                  <HeaderMenu/>
                  <Contact/>
              </Route>
              <Route path="/options" exact>
                  <HeaderMenu/>
                  <Options/>
              </Route>
              <Route path="/profile" exact>
                  <HeaderMenu/>
                  <Profile/>
              </Route>
              <Route path="/resources" exact>
                  <HeaderMenu/>
                  <Resources/>
              </Route>
              <Route path="/legal" exact>
                  <LegalNotices/>
              </Route>
              <Route path="/login" exact>
                  <HeaderLoginRegister/>
                  <LoginRegister/>
              </Route>
          </Switch>

      </Router>
  );
}

export default App;
