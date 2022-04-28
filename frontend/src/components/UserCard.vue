<template>
  <b-card>
    <b-card-img class="rounded-circle" :src="user.profile_picture" img-width="10px" v-if="user.profile_picture"> </b-card-img>
    <b-card-img class="rounded-circle" :src="avatar" img-width="10px" v-else> </b-card-img>
    <b-card-text> <a :href="this.user.spotify_profile_url"> {{this.user.username}} </a></b-card-text>
    <b-card-text v-if="this.current_song_name"> <a :href="this.user.current_song_url"> {{this.user.current_song_name}} </a></b-card-text>
    <b-card-text v-else> Currently not listening </b-card-text>
  </b-card>
</template>

<script>
export default {
  name: "UserCard",
  props: {
    user: Object
  },
  data(){
    return{
      avatar: require('@/assets/avatar.png')
    }
  },
  mounted() {
    console.log(this.user)
  }
}
</script>

<style scoped>

</style>
