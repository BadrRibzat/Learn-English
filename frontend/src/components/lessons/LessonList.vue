<template>
  <div class="max-w-4xl mx-auto p-4">
    <h2 class="text-3xl font-bold mb-6">Beginner Lessons</h2>
    <div v-if="isAuthenticated" class="mb-6">
      <p class="text-lg">Overall Progress: {{ overallProgress.toFixed(2) }}%</p>
      <p class="text-lg">Average Quiz Score: {{ averageQuizScore.toFixed(2) }}%</p>
    </div>
    <ul>
      <li v-for="lesson in lessons" :key="lesson._id" class="mb-6 p-4 border rounded shadow-sm hover:shadow-md transition-shadow">
        <h3 class="text-2xl font-semibold mb-2">{{ lesson.title }}</h3>
        <p class="mb-3">{{ lesson.brief }}</p>
        <div v-if="isAuthenticated" class="mb-3">
          <div class="flex items-center">
            <div class="w-full bg-gray-200 rounded-full h-2.5 mr-2">
              <div class="bg-blue-600 h-2.5 rounded-full" :style="{ width: `${getLessonProgressPercentage(lesson._id)}%` }"></div>
            </div>
            <span class="text-sm font-medium">{{ getLessonProgressPercentage(lesson._id) }}%</span>
          </div>
          <p class="mt-1">
            <span v-if="getLessonProgress(lesson._id).completed" class="text-green-500">Completed</span>
            <span v-else class="text-yellow-500">In Progress</span>
            <span v-if="getLessonProgress(lesson._id).quizScore !== undefined">
              (Quiz Score: {{ getLessonProgress(lesson._id).quizScore }}%)
            </span>
          </p>
        </div>
        <div class="flex space-x-4">
          <router-link :to="`/lessons/${lesson._id}`" class="inline-block px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition">
            {{ getLessonProgress(lesson._id).completed ? 'Review Lesson' : 'Start Lesson' }}
          </router-link>
          <router-link v-if="isAuthenticated" :to="`/flashcards/${lesson._id}`" class="inline-block px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600 transition">
            Flashcards
          </router-link>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import { computed, onMounted } from 'vue'
import { useStore } from 'vuex'

export default {
  name: 'LessonList',
  setup() {
    const store = useStore()
    const lessons = computed(() => store.state.lessons.list)
    const isAuthenticated = computed(() => store.getters['auth/isAuthenticated'])
    const getLessonProgress = (lessonId) => store.getters['lessons/getLessonProgress'](lessonId)
    const overallProgress = computed(() => store.getters['lessons/overallProgress'])
    const averageQuizScore = computed(() => store.getters['lessons/averageQuizScore'])

    const getLessonProgressPercentage = (lessonId) => {
      const progress = getLessonProgress(lessonId)
      if (progress.completed) return 100
      return progress.quizScore || 0
    }

    onMounted(() => {
      store.dispatch('lessons/fetchLessons')
      if (isAuthenticated.value) {
        store.dispatch('lessons/fetchUserProgress')
      }
    })

    return { 
      lessons, 
      isAuthenticated, 
      getLessonProgress, 
      getLessonProgressPercentage,
      overallProgress,
      averageQuizScore
    }
  }
}
</script>
