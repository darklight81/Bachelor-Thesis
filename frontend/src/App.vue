<template>
  <div id="app">
    <div id="nav"  v-if="user">
      <b-navbar variant="dark">
      <b-navbar-nav class="mx-auto">
        <b-nav-item> <router-link to="/about"><b-icon icon="house-door"></b-icon></router-link></b-nav-item>
        <b-nav-item> <router-link to="/about"><b-icon-house-door/> </router-link></b-nav-item>
        <b-nav-item> <router-link to="/about"><b-icon-house-door/> </router-link></b-nav-item>
      </b-navbar-nav>
    </b-navbar>
      <router-view/>
    </div>
    <Login/>
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
</style>
<script>
import Login from "./views/Login";
import { test } from "./axios-api"
export default {
  components: {Login},
  data(){
    return{
      user: '',
      token: ''
    }
  },
  mounted() {
    const urlParams = new URLSearchParams(window.location.search)
    test()
  }
}
</script>
