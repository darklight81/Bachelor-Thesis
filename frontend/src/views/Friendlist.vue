<template>
    <div class="container" style="background: darkslategrey">
      <div class="row" :key="i" v-for="i in rowCount">
          <UserCard v-for="friend in itemCountInRow(i)"  :key="friend.id" :user="friend.friend" :token="token" :logged-user="user" :followed="true"/>
      </div>
    </div>
</template>

<script>

import {fetchFriends} from "../axios-api";
import UserCard from "../components/UserCard";

export default {
  name: "Friendlist",
  components: {UserCard},
  data(){
    return{
      friends: '',
      isLoading: true,
      declinedLocation: false,
      itemsPerRow: 3
    }
  },
  computed:{
    rowCount() {
      return Math.ceil(this.friends.length / this.itemsPerRow);
    }
  },

  props: {
    token: String,
    user: Object
  },
  async mounted() {
    this.friends = await fetchFriends(this.token, this.user.id)
  },
  methods: {
    itemCountInRow:function(index){
      return this.friends.slice((index - 1) * this.itemsPerRow, index * this.itemsPerRow)
    }
  }
}
</script>

<style scoped>
body{margin-top:20px;
  background:#eee;
}

/* CONTACTS */
.contact-box {
  background-color: #ffffff;
  border: 1px solid #e7eaec;
  padding: 20px;
  margin-bottom: 20px;
}
.contact-box > a {
  color: inherit;
}
.contact-box.center-version > a {
  display: block;
  background-color: #ffffff;
  padding: 20px;
  text-align: center;
}
.contact-box.center-version > a img {
  width: 80px;
  height: 80px;
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
