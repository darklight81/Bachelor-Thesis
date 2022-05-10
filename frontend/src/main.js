import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import { fas } from "@fortawesome/free-solid-svg-icons";
import {far} from "@fortawesome/free-regular-svg-icons";
import { faSpotify } from '@fortawesome/free-brands-svg-icons'
import {fab} from '@fortawesome/free-brands-svg-icons'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { HalfCircleSpinner } from 'epic-spinners'

import Axios from 'axios';
Axios.defaults.baseURL = 'https://api.igor.uhlik.ml'

Vue.config.productionTip = false
library.add(far)
library.add(fas)
library.add(fab)
library.add(faSpotify)
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.component('half-circle-spinner', HalfCircleSpinner)
Vue.component('font-awesome-icon', FontAwesomeIcon)
