import Vue from 'vue'
import axios from 'axios'
import App from './app.vue'
import Vuetify from 'vuetify'
import router from './router'
import store from './store/app.store'

axios.defaults.baseURL = process.env.VUE_APP_BASE_URL

window.axios = axios
Vue.use(require('./api/api').default)
// User Vuetify material desing && customize own theme
Vue.use(Vuetify, {
    theme: {
        primary: '#4445e7',
        secondary: '#e0e0e0',
        accent: '#ff4081',
        error: '#f44336',
        warning: '#ffeb3b',
        info: '#2196f3',
        success: '#4caf50'
    }
})

Vue.config.productionTip = false
Vue.config.delimiters = ['[[', ']]']

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
