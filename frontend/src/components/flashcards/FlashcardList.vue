<template>
  <div class="max-w-4xl mx-auto p-4">
    <h2 class="text-3xl font-bold mb-6">Flashcards for {{ lessonTitle }}</h2>
    <div v-if="loading" class="text-center">Loading flashcards...</div>
    <div v-else-if="flashcards.length === 0" class="text-center">No flashcards available for this lesson.</div>
    <div v-else>
      <div v-if="currentFlashcard" class="mb-6 p-6 border rounded shadow-lg">
        <div @click="flipCard" class="cursor-pointer min-h-[200px] flex items-center justify-center">
          <div v-if="!isFlipped">
            <h3 class="text-2xl font-semibold mb-4">Front</h3>
            <p class="text-xl">{{ currentFlashcard.front_content }}</p>
          </div>
          <div v-else>
            <h3 class="text-2xl font-semibold mb-4">Back</h3>
            <p class="text-xl">{{ currentFlashcard.back_content }}</p>
          </div>
        </div>
      </div>
      <div class="flex justify-between">
        <button @click="previousCard" class="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600 transition">Previous</button>
        <span class="text-lg">{{ currentIndex + 1 }} / {{ flashcards.length }}</span>
        <button @click="nextCard" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition">Next</button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRoute } from 'vue-router'

export default {
  name: 'FlashcardList',
  setup() {
    const store = useStore()
    const route = useRoute()
    const lessonId = route.params.id

    const flashcards = computed(() => store.state.flashcards.list)
    const loading = computed(() => store.state.flashcards.loading)
    const lessonTitle = computed(() => {
      const lesson = store.getters['lessons/getLessonById'](lessonId)
      return lesson ? lesson.title : ''
    })

    const currentIndex = ref(0)
    const isFlipped = ref(false)

    const currentFlashcard = computed(() => flashcards.value[currentIndex.value])

    const flipCard = () => {
      isFlipped.value = !isFlipped.value
    }

    const nextCard = () => {
      currentIndex.value = (currentIndex.value + 1) % flashcards.value.length
      isFlipped.value = false
    }

    const previousCard = () => {
      currentIndex.value = (currentIndex.value - 1 + flashcards.value.length) % flashcards.value.length
      isFlipped.value = false
    }

    onMounted(() => {
      store.dispatch('flashcards/fetchFlashcards', lessonId)
    })

    return { flashcards, loading, lessonTitle, currentFlashcard, isFlipped, currentIndex, flipCard, nextCard, previousCard }
  }
}
</script>
