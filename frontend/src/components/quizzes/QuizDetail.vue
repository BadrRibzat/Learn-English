<template>
  <div class="max-w-4xl mx-auto p-4">
    <h2 class="text-3xl font-bold mb-6">{{ quiz ? quiz.title : 'Loading Quiz...' }}</h2>
    <div v-if="loading" class="text-center">Loading quiz...</div>
    <div v-else-if="!quiz" class="text-center">Quiz not found.</div>
    <div v-else>
      <div v-if="!quizStarted" class="text-center">
        <p class="mb-4">This quiz has {{ quiz.questions.length }} questions.</p>
        <button @click="startQuiz" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition">
          Start Quiz
        </button>
      </div>
      <div v-else-if="!quizCompleted">
        <h3 class="text-xl font-semibold mb-4">Question {{ currentQuestionIndex + 1 }} of {{ quiz.questions.length }}</h3>
        <p class="mb-4">{{ currentQuestion.question }}</p>
        <div class="space-y-2">
          <button 
            v-for="option in currentQuestion.options" 
            :key="option"
            @click="selectAnswer(option)"
            class="w-full text-left p-2 border rounded hover:bg-gray-100 transition"
            :class="{'bg-blue-100': selectedAnswer === option}"
          >
            {{ option }}
          </button>
        </div>
        <div class="mt-6 flex justify-between">
          <button 
            @click="previousQuestion" 
            :disabled="currentQuestionIndex === 0"
            class="bg-gray-300 text-gray-800 px-4 py-2 rounded hover:bg-gray-400 transition disabled:opacity-50"
          >
            Previous
          </button>
          <button 
            @click="nextQuestion" 
            :disabled="currentQuestionIndex === quiz.questions.length - 1"
            class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition disabled:opacity-50"
          >
            Next
          </button>
        </div>
        <button 
          @click="submitQuiz" 
          class="mt-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition"
        >
          Submit Quiz
        </button>
      </div>
      <div v-else>
        <h3 class="text-xl font-semibold mb-4">Quiz Completed</h3>
        <p class="mb-4">Your score: {{ score }}%</p>
        <button @click="restartQuiz" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition">
          Retake Quiz
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'

export default {
  name: 'QuizDetail',
  setup() {
    const store = useStore()
    const route = useRoute()
    const router = useRouter()

    const quizId = route.params.id
    const quiz = computed(() => store.state.quizzes.currentQuiz)
    const loading = computed(() => store.state.quizzes.loading)

    const quizStarted = ref(false)
    const quizCompleted = ref(false)
    const currentQuestionIndex = ref(0)
    const selectedAnswer = ref('')
    const userAnswers = ref([])
    const score = ref(0)

    const currentQuestion = computed(() => quiz.value?.questions[currentQuestionIndex.value])

    const startQuiz = () => {
      quizStarted.value = true
      userAnswers.value = new Array(quiz.value.questions.length).fill('')
    }

    const selectAnswer = (answer) => {
      selectedAnswer.value = answer
      userAnswers.value[currentQuestionIndex.value] = answer
    }

    const nextQuestion = () => {
      if (currentQuestionIndex.value < quiz.value.questions.length - 1) {
        currentQuestionIndex.value++
        selectedAnswer.value = userAnswers.value[currentQuestionIndex.value]
      }
    }

    const previousQuestion = () => {
      if (currentQuestionIndex.value > 0) {
        currentQuestionIndex.value--
        selectedAnswer.value = userAnswers.value[currentQuestionIndex.value]
      }
    }

    const submitQuiz = () => {
      const correctAnswers = quiz.value.questions.filter((q, index) => q.correct_answer === userAnswers.value[index]).length
      score.value = Math.round((correctAnswers / quiz.value.questions.length) * 100)
      quizCompleted.value = true
      
      if (store.getters['auth/isAuthenticated']) {
        store.dispatch('quizzes/submitQuizResult', { quizId, score: score.value })
      }
    }

    const restartQuiz = () => {
      quizStarted.value = false
      quizCompleted.value = false
      currentQuestionIndex.value = 0
      selectedAnswer.value = ''
      userAnswers.value = []
      score.value = 0
    }

    onMounted(() => {
      store.dispatch('quizzes/fetchQuiz', quizId)
    })

    return {
      quiz,
      loading,
      quizStarted,
      quizCompleted,
      currentQuestionIndex,
      currentQuestion,
      selectedAnswer,
      score,
      startQuiz,
      selectAnswer,
      nextQuestion,
      previousQuestion,
      submitQuiz,
      restartQuiz
    }
  }
}
</script>
