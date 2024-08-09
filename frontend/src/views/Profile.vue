<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-6">User Profile</h1>
    <div v-if="user" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
      <div class="mb-4">
        <p class="font-bold">Username: <span class="font-normal">{{ user.username }}</span></p>
        <p class="font-bold">Email: <span class="font-normal">{{ user.email }}</span></p>
        <p class="font-bold">Native Language: <span class="font-normal">{{ getNativeLanguage(user.native_language) }}</span></p>
        <p class="font-bold">Current Level: <span class="font-normal">{{ getCurrentLevel(user.current_level) }}</span></p>
      </div>
      <h2 class="text-2xl font-bold mb-4">Progress Overview</h2>
      <div v-if="lessonsProgress.length > 0">
        <div v-for="progress in lessonsProgress" :key="progress.lesson._id" class="mb-4 border-b pb-2">
          <p class="font-semibold">{{ progress.lesson.title }}</p>
          <div class="flex items-center mt-2">
            <div class="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700 mr-2">
              <div class="bg-blue-600 h-2.5 rounded-full" :style="{ width: `${progress.completionPercentage}%` }"></div>
            </div>
            <span class="text-sm font-medium text-gray-500 dark:text-gray-400">{{ progress.completionPercentage }}%</span>
          </div>
          <p class="mt-1 text-sm">
            Status: {{ progress.completed ? 'Completed' : 'In Progress' }}
            <span v-if="progress.score !== null">(Score: {{ progress.score }}%)</span>
          </p>
        </div>
      </div>
      <p v-else>No progress recorded yet.</p>
    </div>
    <div v-else>Loading user profile...</div>
  </div>
</template>

<script>
import { computed, onMounted } from 'vue'
import { useStore } from 'vuex'

export default {
  name: 'Profile',
  setup() {
    const store = useStore()

    const user = computed(() => store.state.auth.user)
    const lessonsProgress = computed(() => {
      const progress = store.state.lessons.userProgress
      const lessons = store.state.lessons.list
      return lessons.map(lesson => ({
        lesson,
        completed: progress[lesson._id]?.completed || false,
        score: progress[lesson._id]?.score || null,
        completionPercentage: calculateCompletionPercentage(progress[lesson._id])
      }))
    })

    const calculateCompletionPercentage = (lessonProgress) => {
      if (!lessonProgress) return 0
      // You can adjust this calculation based on your specific progress tracking
      return lessonProgress.completed ? 100 : (lessonProgress.score || 0)
    }

    const getNativeLanguage = (code) => {
      const languages = {
        'KO': 'Korean',
        'ZH': 'Chinese',
        'JA': 'Japanese',
        'FR': 'French',
        'ES': 'Spanish',
        'AR': 'Arabic',
        'DE': 'German'
      }
      return languages[code] || code
    }

    const getCurrentLevel = (code) => {
      const levels = {
        'BEG': 'Beginner',
        'INT': 'Intermediate',
        'ADV': 'Advanced'
      }
      return levels[code] || code
    }

    onMounted(() => {
      store.dispatch('auth/fetchUserProfile')
      store.dispatch('lessons/fetchLessons')
      store.dispatch('lessons/fetchUserProgress')
    })

    return { user, lessonsProgress, getNativeLanguage, getCurrentLevel }
  }
}
</script>
