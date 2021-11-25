import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'


import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import { ElNotification } from 'element-plus'

const Vue = createApp(App)
Vue.use(ElementPlus)

Vue.use(store).use(router).mount('#app')