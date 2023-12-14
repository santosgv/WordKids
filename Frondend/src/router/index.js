import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import DesenhosView from '../views/DesenhosView.vue'
import Desenho from '../views/Desenho.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path:'/categoria/:id',
      name: 'categoria',
      component: DesenhosView
    },
    {
      path:'/desenho/:id',
      name:'desenho',
      component: Desenho
    }
  ]
})

export default router
