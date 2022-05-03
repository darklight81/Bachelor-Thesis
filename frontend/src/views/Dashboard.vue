<template>
  <div class="dashboard" style="background: darkslategray">
    <div v-if="!isLoading" class="container">
      <div class="row justify-content-center">
        <UserCard class="col-4" v-for="x in users" :key="x.id" :user="x" :token="token" :logged-user="user"/>
      </div>
    </div>
    <h2 v-else>Loading</h2>
  </div>
</template>

<script>
import {fetchUsers, editUser} from "../axios-api";
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
      users: '',
      isLoading: true
    }
  },
  mounted() {
    navigator.geolocation.getCurrentPosition(async res => {
      const config = {
        "username": this.user.username,
        "latitude": res.coords.latitude,
        "longitude": res.coords.longitude
      }
      console.log("test")
      ;[, this.users] = await Promise.all([editUser(this.user.id, this.token, config), fetchUsers(this.token)])
      this.isLoading = false
    })
  }
}
</script>

<style scoped>

</style>
