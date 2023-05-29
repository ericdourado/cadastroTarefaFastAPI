import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Registrar from '../views/Register.vue'
import Tarefas from '../views/Tarefas.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/registrar',
      name: 'registrar',
      component: Registrar
    },
    {
      path: '/tarefas',
      name: 'tarefas',
      component: Tarefas
    },

  ]
})

export default router
