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

export async function editUser(id, token, config){
    let user

    await axios.put(`api/users/${id}/`, config, {
        headers: {
            'Authorization': `Token ${token}`
        }}).then(res => user = res.data)
    return user
}

export async function getUser(id, token){
    let user
    await axios.get(`api/users/${id}/`,{
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

export async function getLikes(token, user_id){
    let likes
    await axios.get(`api/users/${user_id}/likes`,{
        headers: {
            'Authorization': `Token ${token}`
        }}).then( res => likes = res.data)
    return likes.likes
}

export async function postLike(token, given_to, config){
    let ret
    await axios.post(`api/users/${given_to}/likes/`, config, {
        headers: {
            'Authorization': `Token ${token}`
        }}).then( res => ret = res.data)
    console.log(ret)
    return ret
}
export async function deleteLike(token, given_to, config){
    let ret
    await axios.delete(`api/users/${given_to}/likes/`, {
        headers: {
            'Authorization': `Token ${token}`
        },
        data: config}).then( res => ret = res.data)
    return ret
}

export async function addFriend(token, config, user_id){
    let ret
    await axios.post(`/api/users/${user_id}/friends/`, config, {
        headers: {
            'Authorization': `Token ${token}`
        }}).then( res => ret = res.data, () => ret = false)
    return ret
}

export async function fetchFriends(token, user_id){
    let users
    await axios.get(`api/users/${user_id}/friends/`, {
        headers: {
            'Authorization': `Token ${token}`
        }
    }).then(res => {
        users = res.data.friends
    },  )
    return users
}

export async function removeFriend(token, user_id, config){
    let ret
    await axios.delete(`api/users/${user_id}/friends/`, {
        headers: {
            'Authorization': `Token ${token}`
        },
        data: config}).then( res => ret = res.data)
    return ret
}
