<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-lg-9">
        <div class="box shadow-sm rounded bg-white mb-3">
          <div class="box-title border-bottom p-3">
            <h6 class="m-0">Recent</h6>
          </div>
          <div class="box-body p-0">
            <NotificationCard v-for="like in likes" :key="like.id" :like="like"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {getLikes} from "../axios-api";
import NotificationCard from "../components/NotificationCard";

export default {
  name: "Notifications",
  components: {NotificationCard},
  props: {
    user: Object,
    token: String
  },
  data(){
    return {
      likes: null
    }
  },
  async mounted() {
    this.likes = await getLikes(this.token, this.user.id)
  },
  methods: {
  }
}
</script>

<style scoped>
body{
  margin-top:20px;
  background-color: #f0f2f5;
}
.dropdown-list-image {
  position: relative;
  height: 2.5rem;
  width: 2.5rem;
}
.dropdown-list-image img {
  height: 2.5rem;
  width: 2.5rem;
}
.btn-light {
  color: #2cdd9b;
  background-color: #e5f7f0;
  border-color: #d8f7eb;
}
</style>
