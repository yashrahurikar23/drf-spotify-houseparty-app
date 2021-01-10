import React, { Component, Fragment } from 'react';
import { render } from 'react-dom';

export default class App extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <Fragment>
        <h1>Testing react!!</h1>
      </Fragment>
    )
  }
}

const appDiv = document.getElementById('app');
render(<App />, appDiv);