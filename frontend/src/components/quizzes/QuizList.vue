<template>
  <div class="max-w-4xl mx-auto p-4">
    <h2 class="text-3xl font-bold mb-6">Quizzes</h2>
    <div v-if="loading" class="text-center">Loading quizzes...</div>
    <div v-else-if="quizzes.length === 0" class="text-center">No quizzes available.</div>
    <ul v-else>
      <li v-for="quiz in quizzes" :key="quiz._id" class="mb-6 p-4 border rounded shadow-sm hover:shadow-md transition-shadow">
        <h3 class="text-2xl font-semibold mb-2">{{ quiz.title }}</h3>
        <p class="mb-4">Questions: {{ quiz.questions.length }}</p>
        <div v-if="getUserQuizProgress(quiz._id)" class="mb-4">
          <p>Your best score: {{ getUserQuizProgress(quiz._id).bestScore }}%</p>
          <p>Last attempt: {{ formatDate(getUserQuizProgress(quiz._id).lastAttempt) }}</p>
        </div>
        <router-link :to="`/quizzes/${quiz._id}`" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition">
          {{ getUserQuizProgress(quiz._id) ? 'Retake Quiz' : 'Start Quiz' }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { computed, onMounted } from 'vue'
import { useStore } from 'vuex'

export default {
  name: 'QuizList',
  setup() {
    const store = useStore()
    const quizzes = computed(() => store.state.quizzes.list)
    const loading = computed(() => store.state.quizzes.loading)
    const userQuizProgress = computed(() => store.state.quizzes.userProgress)

    const getUserQuizProgress = (quizId) => userQuizProgress.value[quizId]

    const formatDate = (dateString) => {
      if (!dateString) return 'Never'
      return new Date(dateString).toLocaleDateString()
    }

    onMounted(() => {
      store.dispatch('quizzes/fetchQuizzes')
      if (store.getters['auth/isAuthenticated']) {
        store.dispatch('quizzes/fetchUserQuizProgress')
      }
    })

    return { quizzes, loading, getUserQuizProgress, formatDate }
  }
}
</script>
