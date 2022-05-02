<template>
  <b-card>
    <b-card-img class="rounded-circle" :src="user.profile_picture" img-width="10px" v-if="user.profile_picture"> </b-card-img>
    <b-card-img class="rounded-circle" :src="avatar" img-width="10px" v-else> </b-card-img>
    <b-card-text> <a :href="this.user.spotify_profile_url"> {{this.user.username}} </a></b-card-text>
    <b-card-text v-if="this.user.current_song_name">
          <a :href="this.user.current_song_url"> {{this.user.current_song_name}} </a>
          <a href="" v-if="!songLiked" v-on:click="likeSong(user.id, user.current_song_name, user.current_song_url, $event)"> <b-icon-suit-heart/></a>
          <a href="" v-else v-on:click="unlikeSong(user.id, user.current_song_name, user.current_song_url, $event)"> <b-icon-suit-heart-fill/></a>
    </b-card-text>
    <b-card-text v-else> Currently not listening</b-card-text>
  </b-card>
</template>

<script>
import {deleteLike, postLike} from "../axios-api";

export default {
  name: "UserCard",
  props: {
    user: Object,
    token: String,
    loggedUser: Object
  },
  data(){
    return{
      songLiked: false,
      avatar: require('@/assets/avatar.png')
    }
  },
  mounted() {
  },
  methods: {
    likeSong: function (given_to, song_name, song_url, event){
      event.preventDefault()
      this.songLiked = true
      let config = {
        'given_to': given_to,
        'given_by': this.loggedUser.id,
        'song_name': song_name,
        'song_url': song_url
      }
      postLike(this.token, config)
    },
    unlikeSong: function (given_to, song_name, song_url, event){
      event.preventDefault()
      this.songLiked = false
      let config = {
        'given_to': given_to,
        'given_by': this.loggedUser.id,
        'song_name': song_name,
        'song_url': song_url
      }
      deleteLike(this.token, config)
    }
  }
}
</script>

<style scoped>

</style>
