<template>
  <div class="profile" style="background: darkslategray">
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css" rel="stylesheet">
    <div class="container">
      <div class="row flex-lg-nowrap">

        <div class="col">
          <div class="row">
            <div class="col mb-3">
              <div class="card">
                <div class="card-body">
                  <div class="e-profile">
                    <div class="row">
                      <div class="col-12 col-sm-auto mb-3">
                        <div class="mx-auto" style="width: 140px;">
                          <div class="d-flex justify-content-center align-items-center rounded" style="height: 140px; background-color: rgb(233, 236, 239);">
                            <span style="color: rgb(166, 168, 170); font: bold 8pt Arial;"><img :src="this.user.profile_picture" height="140px" class="rounded-circle"></span>
                          </div>
                        </div>
                      </div>
                      <div class="col d-flex flex-column flex-sm-row justify-content-between mb-3">
                        <div class="text-center text-sm-left mb-2 mb-sm-0">
                          <h4 class="pt-sm-2 pb-1 mb-0 text-nowrap">{{this.user.username}}</h4>
                        </div>
                      </div>
                    </div>
                    <div class="tab-content pt-3">
                      <div class="tab-pane active">
                        <form class="form" novalidate="">
                          <div class="row">
                            <div class="col">
                              <div class="row">
                                <div class="col">
                                  <div class="form-group">
                                    <label>First name</label>
                                    <input class="form-control" type="text" name="name" placeholder="John" v-model="editedUser.firstName">
                                  </div>
                                </div>
                                <div class="col">
                                  <div class="form-group">
                                    <label>Last name</label>
                                    <input class="form-control" type="text" name="lastname" placeholder="Smith" v-model="editedUser.lastName">
                                  </div>
                                </div>
                              </div>
                              <div class="row">
                                <div class="col">
                                  <div class="form-group">
                                    <label>City</label>
                                    <input class="form-control" type="text" placeholder="City..." v-model="editedUser.city">
                                  </div>
                                </div>
                              </div>
                              <div class="row">
                                <div class="col">
                                  <div class="form-group">
                                    <label>Favorite artist</label>
                                    <input class="form-control" type="text" placeholder="Favorite artist..." v-model="editedUser.favoriteArtist">
                                  </div>
                                </div>
                              </div>
                              <div class="row">
                                <div class="col">
                                  <div class="form-group">
                                    <label>Favorite Song</label>
                                    <input class="form-control" type="text" placeholder="Favorite song..." v-model="editedUser.favoriteSong">
                                  </div>
                                </div>
                              </div>
                              <div class="row">
                                <div class="col">
                                  <div class="form-group">
                                    <label>Favorite podcast</label>
                                    <input class="form-control" type="text" placeholder="Favorite podcast..." v-model="editedUser.favoritePodcast">
                                  </div>
                                </div>
                              </div>
                              <div class="row">
                                <div class="col">
                                  <div class="form-group">
                                    <label>Facebook link</label>
                                    <input class="form-control" type="url" placeholder="Facebook profile..." v-model="editedUser.facebook">
                                  </div>
                                </div>
                              </div>
                              <div class="row">
                                <div class="col">
                                  <div class="form-group">
                                    <label>Twitter profile link</label>
                                    <input class="form-control" type="url" placeholder="Twitter profile..." v-model="editedUser.twitter">
                                  </div>
                                </div>
                              </div>
                              <div class="row">
                                <div class="col">
                                  <div class="form-group">
                                    <label>Instagram profile link</label>
                                    <input class="form-control" type="url" placeholder="Instagram profile..." v-model="editedUser.instagram">
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                          <div class="row">
                            <div class="col d-flex justify-content-end">
                              <input type="submit" value="Publish" v-on:click="sendForm($event)">
                              <button class="btn btn-success" type="submit" v-on:click="sendForm($event)">Save Changes</button>
                            </div>
                          </div>
                        </form>

                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>

import {editUser} from "../axios-api";

let EditedUser = {
  firstName: '',
  lastName:  '',
  favoriteArtist: '',
  favoriteSong:  '',
  favoritePodcast:  '',
  instagram: '',
  facebook: '',
  twitter: '',
  city: ''

}


export default {
  name: "ProfileEdit",
  props: {
    user: Object,
    token: String
  },
  data(){
    return{
      editedUser: EditedUser,
    }
  },
  methods:{
    sendForm: function (event){
      event.preventDefault()
      let config = {}
      if (this.editedUser.firstName)
        config['first_name'] = this.editedUser.firstName
      if (this.editedUser.lastName)
        config['last_name'] = this.editedUser.lastName
      if (this.editedUser.favoriteArtist)
        config['favorite_artist'] = this.editedUser.favoriteArtist
      if (this.editedUser.favoritePodcast)
        config['favorite_podcast'] = this.editedUser.favoritePodcast
      if (this.editedUser.favoriteSong)
        config['favorite_song'] = this.editedUser.favoriteSong
      if (this.editedUser.city)
        config['city'] = this.editedUser.city
      if (this.editedUser.twitter)
        config['twitter_url'] = this.editedUser.twitter
      if (this.editedUser.instagram)
        config['instagram_url'] = this.editedUser.instagram
      if (this.editedUser.facebook)
        config['facebook_url'] = this.editedUser.facebook
      editUser(this.user.id, this.token, config)
    },
  }
}
</script>

<style scoped>

</style>
