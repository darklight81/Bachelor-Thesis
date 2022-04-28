import axios from "axios";

export async function login(config){
    let token
    await axios.post('api/login/social/token/spotify', config).then(
        res => token = res.data.token
    )
    return token
}

export async function setupUser(config, token){
    let user
    await axios.post('api/my-login/ ', config, {
        headers: {
            'Authorization': `Token ${token}`
        }
    }).then( res => user = res.data)
    return user
}

export async function fetchUsers(token){
    let users
    await axios.get('api/users/', {
        headers: {
            'Authorization': `Token ${token}`
        }
    }).then(res => users = res.data.users)
    return users
}

export async function editUser(token, config){
    let user
    await axios.put('api/user/', config, {
        headers: {
            'Authorization': `Token ${token}`
        }}).then(res => user = res.data)
    return user
}

export async function getUser(token){
    let user
    await axios.get('api/user/',{
        headers: {
            'Authorization': `Token ${token}`
        }}).then(res => user = res.data)
    return user
}

export async function logout(token){
    let ret
    await axios.post('api/logout/', {}, {
        headers: {
            'Authorization': `Token ${token}`
        }}).then( res => ret = res.data)
    return ret
}

export async function getLikes(token){
    let likes
    await axios.get('api/likes/',{
        headers: {
            'Authorization': `Token ${token}`
        }}).then( res => likes = res.data)
    return likes
}

export async function postLike(token, config){
    let ret
    await axios.post('api/likes', config, {
        headers: {
            'Authorization': `Token ${token}`
        }}).then( res => ret = res.data)
    return ret
}
