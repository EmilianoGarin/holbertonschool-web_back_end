import getResponseFromAPI from './0-promise';
/* eslint-disable */
const response = getResponseFromAPI();
console.log(response instanceof Promise);
