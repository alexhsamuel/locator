/**
 * app.js
 *
 * This is the entry file for the application, only setup and boilerplate
 * code.
 */

// Needed for redux-saga es6 generator support
import 'babel-polyfill';

// Import all the third party stuff
import React from 'react';
import ReactDOM from 'react-dom';

// Import root app
import TestApp from 'containers/TestApp';

// Create redux store with history
const MOUNT_NODE = document.getElementById('app');

console.log('defining render');
const render = () => {
  ReactDOM.render(
    <TestApp />,
    MOUNT_NODE
  );
};
console.log('render defined');
render();
