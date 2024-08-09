import { createStore } from 'vuex'
import auth from './modules/auth'
import lessons from './modules/lessons'
import flashcards from './modules/flashcards'
import quizzes from './modules/quizzes'
import achievements from './modules/achievements'

export default createStore({
  modules: {
    auth,
    lessons,
    flashcards,
    quizzes,
    achievements
  }
})
