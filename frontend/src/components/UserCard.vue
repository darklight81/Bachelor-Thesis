<template>
      <div>
        <div class="contact-box center-version">
          <a :href="user.spotify_profile_url">
            <img alt="image" class="rounded-circle" v-if="!this.user.profile_picture" src="https://bootdey.com/img/Content/avatar/avatar1.png">
            <img alt="image" class="rounded-circle" v-else :src="this.user.profile_picture">
          </a>
            <h3 class="m-b-xs"><strong>{{ this.user.username }}</strong>
              <a v-if="this.user.spotify" :href="this.user.spotify_profile_url">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-spotify" viewBox="0 0 16 16">
              <path d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0zm3.669 11.538a.498.498 0 0 1-.686.165c-1.879-1.147-4.243-1.407-7.028-.77a.499.499 0 0 1-.222-.973c3.048-.696 5.662-.397 7.77.892a.5.5 0 0 1 .166.686zm.979-2.178a.624.624 0 0 1-.858.205c-2.15-1.321-5.428-1.704-7.972-.932a.625.625 0 0 1-.362-1.194c2.905-.881 6.517-.454 8.986 1.063a.624.624 0 0 1 .206.858zm.084-2.268C10.154 5.56 5.9 5.419 3.438 6.166a.748.748 0 1 1-.434-1.432c2.825-.857 7.523-.692 10.492 1.07a.747.747 0 1 1-.764 1.288z"/>
            </svg> </a> </h3>
            <h3>{{ this.user.distance }} km away</h3>
            <div class="font-weight-bold" v-if="this.user.current_song_name"> <a :href="this.user.current_song_url"> {{this.user.current_song_name}} </a>  <b-icon-heart/>  </div>
            <div class="font-weight-bold" v-else> Currently not listening  </div>

          <div class="contact-box-footer">
            <div class="m-t-xs btn-group">
              <a class="btn btn-xs btn-white"><i class="fa fa-phone"></i> Call </a>
              <a class="btn btn-xs btn-white"><i class="fa fa-envelope"></i> Email</a>
              <a class="btn btn-xs btn-white"><i class="fa fa-user-plus"></i> Follow</a>
            </div>
          </div>
        </div>
      </div>
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
    this.user.distance = Math.round(this.user.distance * 100) / 100
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

/* CONTACTS */
.contact-box {
  margin-top: 20px;
  background-color: #ffffff;
  border: 1px solid #e7eaec;
  padding: 20px;
  margin-bottom: 20px;
}
.contact-box > a {
  color: inherit;
}
.contact-box.center-version {
  border: 1px solid #e7eaec;
  padding: 0;
}
.contact-box.center-version > a {
  display: block;
  background-color: #ffffff;
  padding: 20px;
  text-align: center;
}
.contact-box.center-version > a img {
  width: 150px;
  height: 150px;
  margin-top: 10px;
  margin-bottom: 10px;
}
.contact-box.center-version address {
  margin-bottom: 0;
}
.contact-box .contact-box-footer {
  text-align: center;
  background-color: #ffffff;
  border-top: 1px solid #e7eaec;
  padding: 15px 20px;
}
a{
  text-decoration:none !important;
}
</style>
