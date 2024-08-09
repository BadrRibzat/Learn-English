import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import LessonList from '../components/lessons/LessonList.vue'
import LessonDetail from '../components/lessons/LessonDetail.vue'
import FlashcardList from '../components/flashcards/FlashcardList.vue'
import QuizList from '../components/quizzes/QuizList.vue'
import QuizDetail from '../components/quizzes/QuizDetail.vue'
import Profile from '../views/Profile.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/lessons',
    name: 'Lessons',
    component: LessonList
  },
  {
    path: '/lessons/:id',
    name: 'LessonDetail',
    component: LessonDetail
  },
  {
    path: '/flashcards/:id',
    name: 'Flashcards',
    component: FlashcardList
  },
  {
    path: '/quizzes',
    name: 'Quizzes',
    component: QuizList
  },
  {
    path: '/quizzes/:id',
    name: 'QuizDetail',
    component: QuizDetail
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
