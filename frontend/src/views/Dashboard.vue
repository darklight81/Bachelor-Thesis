<template>
  <div class="dashboard" style="background: darkslategray">

    <div v-if="!isLoading" class="container">
        <div class="row">
          <UserCard v-for="x in users" :key="x.id" :user="x" :token="token" :logged-user="user"/>
        </div>
    </div>

    <div v-else-if="isLoading && !declinedLocation" class="loading">
      <half-circle-spinner class="spinner"
                           :animation-duration="1000"
                           :size="100"
                           color="green"
      />
    </div>

    <div v-else class="loading"> <h2 class="spinner" style="color: darkolivegreen"> To see your homepage, you need to enable location services.</h2></div>
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
      isLoading: true,
      declinedLocation: false
    }
  },
  mounted() {
    navigator.geolocation.getCurrentPosition(async res => {
      const config = {
        "username": this.user.username,
        "latitude": res.coords.latitude,
        "longitude": res.coords.longitude
      }
      ;[, this.users] = await Promise.all([editUser(this.user.id, this.token, config), fetchUsers(this.token)])
      this.isLoading = false
    }, () => {
      this.declinedLocation = true
    })
  }
}
</script>

<style scoped>
.loading{
  height: 94.3vh;
  width: 100vw;
}
.spinner{
  position: absolute;
  justify-content: center;
  top:  50%;
  left: 50%;
  transform: translate(-50%,-50%);
}
</style>
