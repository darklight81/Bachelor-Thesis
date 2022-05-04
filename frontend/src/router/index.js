import Vue from 'vue'
import VueRouter from 'vue-router'
import Dashboard from "../views/Dashboard";
import ProfileEdit from "../views/ProfileEdit";
import Notifications from "../views/Notifications";
import Friendlist from "../views/Friendlist";
import Profile from "../views/Profile";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Dashboard,

  },
  {
    path: '/profile',
    name: 'ProfileEdit',
    component: ProfileEdit
  },
  {
    path: '/notifications',
    name: 'Notifications',
    component: Notifications
  },
  {
    path: '/friends',
    name: 'Friends',
    component: Friendlist
  },
  {
    path: '/profile/:id',
    name: 'Profile',
    component: Profile,
    props: true
  },
  {
    path :'*',
    redirect: '/',
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
