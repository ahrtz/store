import axios from "axios";
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'

export default axios.create({
  baseURL: "http://localhost:8000/",
  headers: {
    "Content-type": "application/json",
  }

});
