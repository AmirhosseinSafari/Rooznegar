import Vue from 'vue'
import Router from 'vue-router'
import VueDemo from '@/components/VueDemo'
import News from '@/components/News'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'news',
      component: News
    }
  ]
})
