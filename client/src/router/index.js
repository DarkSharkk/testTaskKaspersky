import Vue from 'vue'
import VueRouter from 'vue-router'
import WelcomePage from '@/components/WelcomePage'
import UsersInfoPage from '@/components/UsersInfoPage'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'WelcomePage',
    component: WelcomePage
  },
  {
    path: '/users',
    name: 'users',
    component: UsersInfoPage
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
