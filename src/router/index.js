import { createRouter, createWebHashHistory } from 'vue-router'
import home from '../views/home.vue'
import create from '../views/create.vue'

const routes = [
  {
    path: '/home',
    name: 'home',
    component: home
  },
  {
    path: '/create',
    name: 'create',
    component: create
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
