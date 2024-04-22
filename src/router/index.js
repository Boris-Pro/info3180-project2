import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AddNewPostFormView from "../views/AddNewPostFormView.vue";
import RegisterFormView from '../views/RegisterFormView.vue';
import LoginFormView from '../views/LoginFormView.vue';
import ExploreView from '../views/ExploreView.vue';
import UserProfileView from '../views/UserProfileView.vue';


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
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }, 
    {
      path: "/posts/new",
      name: "AddNewPostForm",
      component: AddNewPostFormView,
    },
    {
      path: "/register",
      name: "RegisterForm",
      component: RegisterFormView,
    },
    {
      path: "/login",
      name: "LoginForm",
      component: LoginFormView,
    },
    {
      path: "/explore",
      name: "Eplore",
      component: ExploreView,
    },
    {
      path:"/users/:userId",
      name: "UserProfile",
      component: UserProfileView,

    }
  ]
})

export default router
