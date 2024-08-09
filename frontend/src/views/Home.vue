<template>
  <div class="container mx-auto px-4 py-8 text-center animate-fadeIn">
    <h1 class="text-4xl md:text-5xl font-bold mb-6">{{ $t('home.welcome') }}</h1>
    <p class="text-xl mb-8">{{ $t('home.startJourney') }}</p>
    <div class="space-y-8">
      <router-link 
        to="/lessons" 
        class="btn btn-primary text-lg inline-block"
      >
        <font-awesome-icon icon="book" class="mr-2" /> {{ $t('home.startLearning') }}
      </router-link>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="card transform hover:scale-105 transition-transform duration-300">
          <font-awesome-icon icon="language" class="text-4xl text-blue-500 mb-4" />
          <h3 class="text-xl font-semibold mb-2">{{ $t('home.interactiveLessons') }}</h3>
          <p>{{ $t('home.interactiveLessonsDesc') }}</p>
        </div>
        <div class="card transform hover:scale-105 transition-transform duration-300">
          <font-awesome-icon icon="cards-blank" class="text-4xl text-green-500 mb-4" />
          <h3 class="text-xl font-semibold mb-2">{{ $t('home.flashcards') }}</h3>
          <p>{{ $t('home.flashcardsDesc') }}</p>
        </div>
        <div class="card transform hover:scale-105 transition-transform duration-300">
          <font-awesome-icon icon="chart-line" class="text-4xl text-purple-500 mb-4" />
          <h3 class="text-xl font-semibold mb-2">{{ $t('home.trackProgress') }}</h3>
          <p>{{ $t('home.trackProgressDesc') }}</p>
        </div>
      </div>
    </div>
    <div v-if="isAuthenticated" class="mt-12">
      <h2 class="text-2xl font-bold mb-4">Your Progress</h2>
      <p>Overall Progress: {{ overallProgress.toFixed(2) }}%</p>
      <p>Completed Lessons: {{ completedLessons }} / {{ totalLessons }}</p>
      <router-link to="/profile" class="btn btn-secondary mt-4 inline-block">View Full Profile</router-link>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'

export default {
  name: 'Home',
  setup() {
    const store = useStore()

    const isAuthenticated = computed(() => store.getters['auth/isAuthenticated'])
    const overallProgress = computed(() => store.getters['lessons/overallProgress'])
    const completedLessons = computed(() => store.getters['lessons/completedLessonsCount'])
    const totalLessons = computed(() => store.state.lessons.list.length)

    return {
      isAuthenticated,
      overallProgress,
      completedLessons,
      totalLessons
    }
  }
}
</script>
