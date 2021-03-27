import './css/style.scss';
// routes import
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";

import LoginRegister from './componnets/LoginRegister.jsx'
import Profile from './componnets/Profile.jsx'
import Beaches from './componnets/Beaches.jsx'
import Option from './componnets/Options.jsx'
import Contact from './componnets/Contact.jsx'
import Resources from './componnets/Resources.jsx'
import LegalNotices from './componnets/LegalNotices.jsx'


function App() {
  return (
      <Router>
          <Switch>
              {
                  /*App routes*/
                  /*Exact is not necessary but I use it just in case it fails*/
              }
              <Router path="/" exact>
                  <Beaches/>
              </Router>
              <Route path="/login" exact>
                  <LoginRegister/>
              </Route>
              <Route path="/contact" exact>
                  <Contact/>
              </Route>
              <Route path="/option" exact>
                  <Option/>
              </Route>
              <Route path="/profile" exact>
                  <Profile/>
              </Route>
              <Route path="/resources" exact>
                  <Resources/>
              </Route>
          </Switch>

      </Router>
  );
}

export default App;
