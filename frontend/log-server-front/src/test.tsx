import axios from "axios";
// import {API_URL} from "./env";


function ApiTest(){
    const response = axios.get('http://logs.dvirlabs.com:8001/fw_logs');
    return <h1>response</h1>
}

export default ApiTest