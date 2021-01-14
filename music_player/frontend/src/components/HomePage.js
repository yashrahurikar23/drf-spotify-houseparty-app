import React, { Fragment } from 'react';
// router imports
import { BrowserRouter as Router, Switch, Link, Redirect, Route } from 'react-router-dom';
// Components
import CreateRoomPage from './CreateRoomPage';
import JoinRoomPage from './JoinRoomPage';

function HomePage(props) {
  return (
    <Fragment>
      <Router>
        <Switch>
          <Route exact path='/' ><p>This is the home page.</p></Route>
          <Route path='/join' component={JoinRoomPage} />
          <Route path='/create' component={CreateRoomPage} />
        </Switch>
      </Router>
    </Fragment>
  )
}

export default HomePage;
