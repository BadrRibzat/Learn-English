<template>
  <div v-if="lesson" class="max-w-4xl mx-auto p-4">
    <h2 class="text-3xl font-bold mb-4">{{ lesson.title }}</h2>
    <div v-if="isAuthenticated">
      <div class="mb-4 p-4 bg-gray-100 rounded">
        <p><strong>Progress:</strong> {{ progressPercentage }}%</p>
        <p><strong>Status:</strong> {{ lessonProgress.completed ? 'Completed' : 'In Progress' }}</p>
        <p v-if="lessonProgress.quizScore !== undefined"><strong>Quiz Score:</strong> {{ lessonProgress.quizScore }}%</p>
      </div>
      <div v-html="lesson.content" class="prose max-w-none mb-6"></div>
      <div class="flex space-x-4">
        <button 
          @click="markAsCompleted" 
          class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition"
          :disabled="lessonProgress.completed"
        >
          {{ lessonProgress.completed ? 'Completed' : 'Mark as Completed' }}
        </button>
        <router-link 
          :to="`/quiz/${lesson._id}`" 
          class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition"
        >
          Take Quiz
        </router-link>
      </div>
    </div>
    <div v-else>
      <p>{{ lesson.brief }}</p>
      <p class="mt-4 text-red-500">Please log in to view the full lesson content.</p>
    </div>
  </div>
</template>

<script>
import { computed, onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRoute } from 'vue-router'

export default {
  name: 'LessonDetail',
  setup() {
    const store = useStore()
    const route = useRoute()
    const lessonId = route.params.id

    const lesson = computed(() => store.state.lessons.currentLesson)
    const isAuthenticated = computed(() => store.getters['auth/isAuthenticated'])
    const lessonProgress = computed(() => store.getters['lessons/getLessonProgress'](lessonId))
    const progressPercentage = computed(() => {
      if (lessonProgress.value.completed) return 100;
      return lessonProgress.value.quizScore || 0;
    })

    onMounted(() => {
      store.dispatch('lessons/fetchLesson', lessonId)
      if (isAuthenticated.value) {
        store.dispatch('lessons/fetchUserProgress')
      }
    })

    const markAsCompleted = () => {
      store.dispatch('lessons/completeLesson', lessonId)
    }

    return { 
      lesson, 
      isAuthenticated, 
      markAsCompleted, 
      lessonProgress,
      progressPercentage
    }
  }
}
</script>
