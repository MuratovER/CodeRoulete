import React from "react";
import {BrowserRouter as Router, Route, Routes} from "react-router-dom";

import Home from './containers/Home'
import Login from './containers/Login'
import Signup from './containers/Signup'
import Activate from './containers/Activate'
import ResetPassword from './containers/ResetPassword'
import ResetPasswordConfirm from './containers/ResetPasswordConfirm'
import Layout from "./hocs/Layout";

const App = () => (
    <Router>
        <Layout>
            <Routes>
                <Route exact path="/" component={Home} />
                <Route exact path="/login" component={Login} />
                <Route exact path="/signup" component={Signup} />
                <Route exact path="/reset_password" component={ResetPassword} />
                <Route exact path="/password/reset/confirm/:uid/:token" component={ResetPasswordConfirm} />
                <Route exact path="/activate/:uid/:token" component={Activate} />
            </Routes>
        </Layout>
    </Router>
)

export default App;