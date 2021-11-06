import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  {
    path: '/',
    name: 'Welcome',
    component: ()=>import('../views/Welcome.vue')
  },
  {
    path:'/top',
    name:'Top',
    component:()=>import('../views/Top.vue')
  },
  {
    path:'/picture_detail',
    name:'Picture_detail',
    component:()=>import('../views/Picture_detail.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
