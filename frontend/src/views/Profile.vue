<template>
  <div class="container" style="background: darkslategray">
    <div class="main-body">
      <div class="row gutters-sm">
        <div class="col-md-4 mb-3">
          <div class="card">
            <div class="card-body">
              <div class="d-flex flex-column align-items-center text-center">
                <img v-if="this.profile_user.profile_picture" :src="this.profile_user.profile_picture" alt="Admin" class="rounded-circle" width="150">
                <img v-else src="https://bootdey.com/img/Content/avatar/avatar7.png" alt="Admin" class="rounded-circle" width="150">
                <div class="mt-3">
                  <h4>{{ this.profile_user.username }}</h4>
                  <span v-if="this.user.id === this.profile_user.id"></span>
                  <a v-else-if="!this.isFriend" class="btn btn-xs btn-white" v-on:click="followPerson(user.id, $event)"><font-awesome-icon icon="fa-solid fa-user-plus" /> Follow</a>
                  <a v-else class="btn btn-xs btn-white" v-on:click="unfollowPerson(user.id, $event)"><font-awesome-icon icon="fa-solid fa-user-minus" /> Unfollow</a>
                </div>
              </div>
            </div>
          </div>
          <div class="card mt-3">
            <ul class="list-group list-group-flush">
              <li class="list-group-item d-flex justify-content-center align-items-center flex-wrap">
                <a :href="this.profile_user.spotify_profile_url">
                <h6 class="mb-0 font-weight-bold"><font-awesome-icon icon="fa-brands fa-spotify" class="socials"/> Spotify</h6>
                </a>
              </li>
              <li class="list-group-item d-flex justify-content-center align-items-center flex-wrap">
                <a :href="this.profile_user.twitter_url">
                <h6 class="mb-0 font-weight-bold"><font-awesome-icon icon="fa-brands fa-twitter" class="socials"/>Twitter</h6>
                </a>
              </li>
              <li class="list-group-item d-flex justify-content-center align-items-center flex-wrap">
                <a :href="this.profile_user.instagram_url">
                <h6 class="mb-0 font-weight-bold"><font-awesome-icon icon="fa-brands fa-instagram" class="socials"/>Instagram</h6>
                </a>
              </li>
              <li class="list-group-item d-flex justify-content-center align-items-center flex-wrap">
                <a :href="this.profile_user.facebook_url">
                <h6 class="mb-0 font-weight-bold"><font-awesome-icon icon="fa-brands fa-facebook" class="socials"/>Facebook</h6>
                </a>
              </li>
            </ul>
          </div>
        </div>
        <div class="col-md-8">
          <div class="card mb-3">
            <div class="card-body">
              <div class="row">
                <div class="col-sm-3">
                  <h6 class="mb-0">Name</h6>
                </div>
                <div v-if="this.profile_user.first_name" class="col-sm-9 text-secondary">
                  {{this.profile_user.first_name + " " + this.profile_user.last_name}}
                </div>
                <div v-else class="col-sm-9 text-secondary">
                </div>
              </div>
              <hr>
              <div class="row">
                <div class="col-sm-3">
                  <h6 class="mb-0">City</h6>
                </div>
                <div class="col-sm-9 text-secondary">
                  {{ this.profile_user.city }}
                </div>
              </div>
              <hr>
              <div class="row">
                <div class="col-sm-3">
                  <h6 class="mb-0">Favorite artist</h6>
                </div>
                <div class="col-sm-9 text-secondary">
                  {{ this.profile_user.favorite_artist }}
                </div>
              </div>
              <hr>
              <div class="row">
                <div class="col-sm-3">
                  <h6 class="mb-0">Favorite song</h6>
                </div>
                <div class="col-sm-9 text-secondary">
                  {{ this.profile_user.favorite_song }}
                </div>
              </div>
              <hr>
              <div class="row">
                <div class="col-sm-3">
                  <h6 class="mb-0">Favorite podcast</h6>
                </div>
                <div class="col-sm-9 text-secondary">
                  {{ this.profile_user.favorite_podcast }}
                </div>
              </div>
              <hr>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import {addFriend, fetchFriends, getUser, removeFriend} from "../axios-api";

export default {
  name: "Profile",
  props: {
    id: [Number, String],
    user: Object,
    token: String
  },
  data(){
    return{
      friends: '',
      isFriend: false,
      profile_user: ''
    }
  },
  async mounted() {
    if (String(this.id) === String(this.user.id))
      this.profile_user = this.user
    else{
      this.profile_user= await getUser(this.id,this.token)
      this.profile_user = this.profile_user.user
      this.friends = await fetchFriends(this.token, this.user.id)
      this.friends.forEach(friendship => {
        if(String(this.id) === String(friendship.friend.id))
          this.isFriend = true
      })
    }
  },
  methods:{
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
a{
  text-decoration: none;
}
body{
  margin-top:20px;
  color: #1a202c;
  text-align: left;
  background-color: #e2e8f0;
}
.socials{
  margin-right: 5px;
  color: darkolivegreen;
}
.main-body {
  padding: 15px;
}
.card {
  box-shadow: 0 1px 3px 0 rgba(0,0,0,.1), 0 1px 2px 0 rgba(0,0,0,.06);
}

.card {
  position: relative;
  display: flex;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 0 solid rgba(0,0,0,.125);
  border-radius: .25rem;
}

.card-body {
  flex: 1 1 auto;
  min-height: 1px;
  padding: 1rem;
}

.gutters-sm {
  margin-right: -8px;
  margin-left: -8px;
}

.gutters-sm>.col, .gutters-sm>[class*=col-] {
  padding-right: 8px;
  padding-left: 8px;
}
.mb-3, .my-3 {
  margin-bottom: 1rem!important;
}

</style>
