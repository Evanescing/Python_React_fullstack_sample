import React from 'react';
import { Route, BrowserRouter as Router, Switch } from 'react-router-dom';


import AdminDashboard from './Components/AdminDashboard';
import AdminPage from "./Pages/AdminPage";
import AdminPageInner from './Components/AdminPageInner';
import ModeratorDashboard from './Components/ModeratorDashboard';
import ModeratorPage from "./Pages/ModeratorPage";
import ModeratorPageInner from './Components/ModeratorPageInner';
import NotFoundPage from './Pages/NotFoundPage';

import { createBrowserHistory } from "history";

const customHistory = createBrowserHistory()

export default class Routes extends React.Component {
    render() {
        return (
            <div>
                <Router>
                    <Switch>
                        <Route exact path='/admin'
                            render={() => <AdminPage><AdminDashboard /></AdminPage>}
                        />                        
                        <Route exact path={'/admin/:option'}
                            render={() => <AdminPage><AdminPageInner /></AdminPage>} />
                        <Route exact path='/moderator'
                            render={() => <ModeratorPage><ModeratorDashboard /></ModeratorPage>} />
                        <Route exact path={'/moderator/:option'}
                            render={() => <ModeratorPage><ModeratorPageInner /></ModeratorPage>} />                        
                        <Route path="*" component={NotFoundPage} />
                    </Switch>
                </Router>
            </div>
        );
    }
};
