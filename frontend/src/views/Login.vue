<template>
  <div class="demo-3">
  <main>
    <div class="frame">
      <div class="frame__title-wrap">
        <h1 class="frame__title">Ambient Canvas Backgrounds</h1>
      </div>
    </div>
    content__title
    <div class="content content--canvas" style="z-index: 1000">
        <a href="https://accounts.spotify.com/authorize?scope=user-read-private&scope=user-read-playback-state&scope=user-read-email&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2F&client_id=00e9b37f36304c169d1bd8c77f50923a"
           class="content__title btn btn-primary vertical-center" style="z-index: 1000;">Log in with Spotify</a>
    </div>
  </main>
  </div>
</template>

<script>
import {setup} from '@/assets/js/shift.js'
export default {
  name: "Login",
  mounted() {
    setup()
  },
  methods: {
    login: function(e){
      e.preventDefault()
      console.log('test')
    }
  }
}
</script>

<style scoped>
#login{
  height: 100vh;
  width: 100vw;
  background: #2c3e50;
}
.vertical-center {
  margin: 0;
  position: absolute;
  top: 50%;
}
</style>
