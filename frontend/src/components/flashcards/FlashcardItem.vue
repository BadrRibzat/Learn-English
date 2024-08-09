<template>
  <div class="flashcard" @click="flip">
    <div v-if="!isFlipped" class="front">
      <h3 class="text-xl font-semibold mb-2">{{ flashcard.front_content }}</h3>
    </div>
    <div v-else class="back">
      <p>{{ flashcard.back_content }}</p>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'FlashcardItem',
  props: {
    flashcard: {
      type: Object,
      required: true
    }
  },
  setup() {
    const isFlipped = ref(false)

    const flip = () => {
      isFlipped.value = !isFlipped.value
    }

    return { isFlipped, flip }
  }
}
</script>
