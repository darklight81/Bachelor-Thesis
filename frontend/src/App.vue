<template>
  <div id="app">
    <div id="nav"  v-if="user">
        <b-navbar variant="dark">
        <b-navbar-nav class="mx-auto">
        <b-nav-item> <router-link to="/" ><b-icon class="nav-icon" icon="house-door-fill"></b-icon></router-link></b-nav-item>
        <b-nav-item> <router-link to="/profile"><b-icon-person-fill class="nav-icon"/> </router-link></b-nav-item>
        <b-nav-item> <router-link to="/notifications"><b-icon-bell-fill class="nav-icon"/> </router-link></b-nav-item>
        <b-nav-item> <a href="" v-on:click="logout"> <b-icon-power class="nav-icon"/></a> </b-nav-item>
      </b-navbar-nav>
    </b-navbar>
      <router-view :token="token" :user="user"/>
    </div>
    <Login v-else/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
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
import {login, logout, setupUser} from "./axios-api"
export default {
  components: {Login},
  data(){
    return{
      user: '',
      token: ''
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
  methods: {
    logout(){
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
