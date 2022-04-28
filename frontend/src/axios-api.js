import axios from "axios";

export function test(){
    axios.get('/api/users').then( success => console.log(success))
}
