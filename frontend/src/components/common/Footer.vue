<template>
  <footer class="bg-gray-800 text-white py-6 mt-12 relative">
    <div class="container mx-auto px-4">
      <div class="flex flex-wrap justify-between items-center">
        <div class="w-full md:w-1/3 text-center md:text-left mb-4 md:mb-0">
          <h3 class="text-lg font-semibold">English Learning App</h3>
          <p class="mt-2 text-sm text-gray-400">Empowering language learners worldwide</p>
        </div>
        <div class="w-full md:w-1/3 text-center mb-4 md:mb-0">
          <div class="flex justify-center space-x-4">
            <a href="#" class="text-gray-400 hover:text-white transition-colors duration-200">
              <font-awesome-icon :icon="['fab', 'facebook']" size="lg" />
            </a>
            <a href="#" class="text-gray-400 hover:text-white transition-colors duration-200">
              <font-awesome-icon :icon="['fab', 'twitter']" size="lg" />
            </a>
            <a href="#" class="text-gray-400 hover:text-white transition-colors duration-200">
              <font-awesome-icon :icon="['fab', 'instagram']" size="lg" />
            </a>
          </div>
        </div>
        <div class="w-full md:w-1/3 text-center md:text-right">
          <p>&copy; {{ currentYear }} English Learning App. All rights reserved.</p>
        </div>
      </div>
    </div>
    <Chatbot />
  </footer>
</template>

<script>
import { defineComponent } from 'vue';
import Chatbot from './Chatbot.vue';

export default defineComponent({
  name: 'Footer',
  components: {
    Chatbot
  },
  computed: {
    currentYear() {
      return new Date().getFullYear()
    }
  }
});
</script>
