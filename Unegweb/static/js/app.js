/*
* vanilla JS
**/
/*
const el = document.createElement('h1');
el.setAttribute('id','title');
el.textContent = "Hola Mundo";

document.getElementById("app").appendChild(el);
*/
/*
const el= React.createElement(
	'h1',
	{id:'title'},
	'Hola',
	React.createElement('span',null," mundo"));
ReactDOM.render(el,document.getElementById('app'))
*/
import React from 'react';
import ReactDOM from 'react-dom';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import MyAwesomeReactComponent from './MyAwesomeReactComponent';

const App = () => (
  <MuiThemeProvider>
    <MyAwesomeReactComponent />
  </MuiThemeProvider>
);

ReactDOM.render(
  <App />,
  document.getElementById('app')
);
