import React, { Component, Fragment } from 'react';
import { render } from 'react-dom';
// Components
import HomePage from './HomePage';

export default class App extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <Fragment>
        <HomePage/>
      </Fragment>
    )
  }
}

const appDiv = document.getElementById('app');
render(<App />, appDiv);