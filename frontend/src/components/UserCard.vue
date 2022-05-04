<template>
      <div class="col-md-4">
        <div class="contact-box center-version">
          <router-link :to="{ name: 'Profile', params: { id: this.user.id }}">
            <img alt="image" class="rounded-circle" v-if="!this.user.profile_picture" src="https://bootdey.com/img/Content/avatar/avatar1.png">
            <img alt="image" class="rounded-circle" v-else :src="this.user.profile_picture">
          </router-link>
            <h3 class="m-b-xs"><strong>{{ this.user.username }}</strong>
              <a v-if="this.user.spotify_profile_url" :href="this.user.spotify_profile_url"><font-awesome-icon icon="fa-brands fa-spotify" style="color: darkolivegreen"/></a>
            </h3>


            <div class="font-weight-bold" v-if="this.user.current_song_name"> <a :href="this.user.current_song_url"> {{this.user.current_song_name}} </a>  </div>
            <div class="font-weight-bold" v-else> Currently not listening  </div>
            <div class="font-weight-normal" v-if="this.user.distance < 3">{{ this.distance }} m away </div>
            <div class="font-weight-normal" v-else-if="this.user.distance < 300">{{ this.user.distance }} km away </div>
            <div class="font-weight-normal" v-else>Very far away </div>
          <div class="contact-box-footer">
            <div class="m-t-xs btn-group">
              <div class="likeSongButton" v-if="this.user.current_song_name">
                <a v-if="!this.songLiked"
                   v-on:click="likeSong(user.id, user.current_song_name, user.current_song_url, $event)"
                   class="btn btn-xs btn-white"><font-awesome-icon icon="fa-regular fa-heart" /> Like Song</a>
                <a v-else class="btn btn-xs btn-white"
                   v-on:click="unlikeSong(user.id, user.current_song_name, user.current_song_url, $event)">
                  <font-awesome-icon icon="fa-solid fa-heart" /> Liked</a>
              </div>
              <a v-if="!this.userFollowed" class="btn btn-xs btn-white" v-on:click="followPerson(user.id, $event)"><font-awesome-icon icon="fa-solid fa-user-plus" /> Follow</a>
              <a v-else class="btn btn-xs btn-white" v-on:click="unfollowPerson(user.id, $event)"><font-awesome-icon icon="fa-solid fa-user-minus" /> Unfollow</a>
            </div>
          </div>
        </div>
      </div>
</template>

<script>
import {addFriend, deleteLike, postLike, removeFriend} from "../axios-api";

export default {
  name: "UserCard",
  props: {
    user: Object,
    token: String,
    loggedUser: Object
  },
  data(){
    return{
      userFollowed: false,
      songLiked: false,
      avatar: require('@/assets/avatar.png'),
      distance: 0
    }
  },
  mounted() {
    this.user.distance = Math.round(this.user.distance * 100) / 100
    if (this.user.distance < 3)
      this.distance = this.user.distance * 1000 // into meters
  },
  methods: {
    likeSong: function (given_to, song_name, song_url, event){
      event.preventDefault()
      this.songLiked = true
      let config = {
        'given_by': this.loggedUser.id,
        'song_name': song_name,
        'song_url': song_url
      }
      console.log('liked')
      postLike(this.token, given_to, config)
    },
    unlikeSong: function (given_to, song_name, song_url, event){
      event.preventDefault()
      this.songLiked = false
      let config = {
        'given_by': this.loggedUser.id,
        'song_name': song_name,
        'song_url': song_url
      }
      deleteLike(this.token, given_to, config)
    },
    followPerson: function (friend_id, event){
      event.preventDefault()
      this.userFollowed = true
      let config = {
        'friend_id': friend_id
      }
      addFriend(this.token, config, this.loggedUser.id)
    },
    unfollowPerson: function (friend_id, event){
      event.preventDefault()
      this.userFollowed = false
      let config = {
        'user_id': this.loggedUser.id,
        'friend_id': friend_id
      }
      removeFriend(this.token, this.loggedUser.id, config)
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
