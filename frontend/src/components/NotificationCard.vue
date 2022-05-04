<template>
  <div class="p-3 d-flex align-items-center border-bottom osahan-post-header">
    <div class="dropdown-list-image mr-3">
      <img v-if="like.given_by.profile_picture" class="rounded-circle" :src="like.given_by.profile_picture" alt="" />
      <img v-else class="rounded-circle" src="https://bootdey.com/img/Content/avatar/avatar4.png" alt="" />
    </div>
    <div class="font-weight-bold mr-3">
      <div>
        {{this.like.given_by.username}} <span class="font-weight-normal">liked the song you were listening to:</span> {{this.like.song_name}}
        <div class="small text-success"> <router-link :to="{ name: 'Profile', params: { id: this.like.given_by.id }, query: { id: this.like.given_by.id }}"><font-awesome-icon icon="check-circle"/> Visit profile </router-link></div>
      </div>
    </div>
    <span class="ml-auto mb-auto">
                            <div class="btn-group">
                                <button type="button" class="btn btn-light btn-sm rounded" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                    <i class="mdi mdi-dots-vertical"></i>
                                </button>
                                <div class="dropdown-menu dropdown-menu-right">
                                    <button class="dropdown-item" type="button"><i class="mdi mdi-delete"></i> Delete</button>
                                    <button class="dropdown-item" type="button"><i class="mdi mdi-close"></i> Turn Off</button>
                                </div>
                            </div>
                            <br />
                            <div class="text-right text-muted pt-1">4d</div>
                        </span>
  </div>
</template>

<script>
export default {
  name: "NotificationCard",
  props: {
    like: Object
  },
  mounted() {
    console.log(this.like)
  }
}
</script>

<style scoped>
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
