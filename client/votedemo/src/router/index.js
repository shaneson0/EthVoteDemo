import Vue from 'vue'
import Router from 'vue-router'
import index from '@/components/index'
import info from '@/components/info'
import login from '@/components/login'

Vue.use(Router)

// export default new Router({
//   routes: [
//     {
//       path: '/login',
//       name: 'login',
//       component: login
//     },
//     {
//       path: '/',
//       component: index,
//       beforeEnter: (to, from, next) => {
//         // ...
//         if (!sessionStorage.getItem('username')) {
//           next({
//             path: '/login',
//             query: { redirect: to.fullPath }
//           })
//         } else {
//           next()
//         }
//       },
//       children: [
//         {
//           path: 'voteinfo',
//           name: 'voteinfo',
//           component: info
//         }
//       ]
//     }
//   ]
// })

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/voteinfo',
      name: 'voteinfo',
      component: info
    }
  ]
})
