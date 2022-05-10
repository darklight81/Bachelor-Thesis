<template>
  <div id="app">
    <div id="nav"  v-if="user">
      <b-navbar variant="dark">
        <b-navbar-nav class="mx-auto">
          <b-nav-item>  <router-link to="/" >             <font-awesome-icon class="nav-icon" icon="fa-solid fa-house" size="xl" />  </router-link></b-nav-item>
          <b-nav-item>  <router-link to="/friends">       <font-awesome-icon class="nav-icon" icon="fa-solid fa-users" size="xl"/>  </router-link></b-nav-item>
          <b-nav-item>  <router-link to="/profile/">       <font-awesome-icon class="nav-icon" icon="fa-solid fa-user" size="xl"/>   </router-link></b-nav-item>
          <b-nav-item>  <router-link to="/notifications"> <font-awesome-icon class="nav-icon" icon="fa-solid fa-bell" size="xl"/>   </router-link></b-nav-item>
          <b-nav-item>  <a href="" v-on:click="logout">   <font-awesome-icon class="nav-icon" icon="fa-solid fa-power-off" size="xl" /> </a> </b-nav-item>
        </b-navbar-nav>
      </b-navbar>
      <router-view :token="token" :user="user"/>
    </div>
    <Login v-else/>
  </div>
</template>

<style>
#app {
  height: 100vh;
  background: darkslategray;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
.nav-icon{
  transition: 0.2s;
  color: darkolivegreen;
}
.nav-icon:hover{
  color: darkgreen;
}
</style>
<script>
import Login from "./views/Login";
import { login, logout, setupUser} from "./axios-api"
export default {
  components: {Login},
  data(){
    return{
      user: '',
      token: '',
      timer: null
    }
  },
  async mounted() {
    this.user = JSON.parse(localStorage.getItem('user'))
    this.token = localStorage.getItem('token')
    const urlParams = new URLSearchParams(window.location.search)
    if (!this.user){
      await this.$router.push('/')
    }
    //Means this is redirect from spotify
    if (urlParams.get('code') && !this.user){
      let config = {
        'code': urlParams.get('code'),
        'redirect_url': 'http://localhost:8080'
      }
      this.token = await login(config)
      localStorage.setItem('token', this.token)
      this.user = await setupUser({}, this.token)
      localStorage.setItem('user', JSON.stringify(this.user))
    }

  },
  beforeDestroy() {
    clearInterval(this.timer)
  },
  methods: {
    logout(){
      clearInterval(this.timer)
      logout(this.token)
      localStorage.removeItem('user')
      localStorage.removeItem('token')
      this.user = ''
      this.token = ''
      this.$router.push('/')
    }
  }
}
</script>
