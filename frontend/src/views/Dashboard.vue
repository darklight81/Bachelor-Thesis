<template>
  <div class="dashboard" style="background: darkcyan">
    <h1>Dashboard</h1>
    <div class="container">
      <div class="row justify-content-center">
        <UserCard class="col-4" v-for="user in users" :key="user.id" :user="user"/>
      </div>
    </div>
  </div>
</template>

<script>
import {fetchUsers, editUser, getUser} from "../axios-api";
import UserCard from "../components/UserCard";

export default {
  name: "Dashboard",
  components: {UserCard},
  props: {
    user: Object,
    token: String
  },
  data(){
    return{
      users: ''
    }
  },
  async mounted() {
    let self = this
    navigator.geolocation.getCurrentPosition( function (res){
      const config = {
        "username": self.user.username,
        "latitude": res.coords.latitude,
        "longitude": res.coords.longitude
      }
      editUser(self.token, config)
    })
    self.users = await fetchUsers(this.token)
    await getUser(this.token)
  }
}
</script>

<style scoped>

</style>
