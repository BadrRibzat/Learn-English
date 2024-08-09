<template>
  <header class="bg-blue-600 text-white shadow-lg">
    <nav class="container mx-auto px-4 py-4 flex flex-wrap justify-between items-center">
      <router-link to="/" class="text-2xl font-bold flex items-center mb-2 md:mb-0">
        <font-awesome-icon icon="graduation-cap" class="mr-2" />
        {{ $t('common.appName') }}
      </router-link>
      <div class="flex flex-wrap items-center space-x-2 md:space-x-4 mt-4 md:mt-0">
        <router-link to="/lessons" class="nav-link">
          <font-awesome-icon icon="book" class="mr-1" /> {{ $t('common.lessons') }}
        </router-link>
        <router-link to="/flashcards" class="nav-link">
          <font-awesome-icon icon="cards-blank" class="mr-1" /> {{ $t('common.flashcards') }}
        </router-link>
        <router-link to="/quizzes" class="nav-link">
          <font-awesome-icon icon="question-circle" class="mr-1" /> {{ $t('common.quizzes') }}
        </router-link>
        <router-link v-if="!isLoggedIn" to="/login" class="btn btn-secondary">
          <font-awesome-icon icon="sign-in-alt" class="mr-1" /> {{ $t('common.login') }}
        </router-link>
        <router-link v-if="!isLoggedIn" to="/register" class="btn btn-secondary">
          <font-awesome-icon icon="user-plus" class="mr-1" /> {{ $t('common.register') }}
        </router-link>
        <button v-if="isLoggedIn" @click="logout" class="btn btn-secondary">
          <font-awesome-icon icon="sign-out-alt" class="mr-1" /> {{ $t('common.logout') }}
        </button>
        <LanguageSelector class="ml-2 md:ml-4" />
      </div>
    </nav>
  </header>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'
import { useI18n } from 'vue-i18n'
import LanguageSelector from '../LanguageSelector.vue'

export default {
  name: 'Header',
  components: {
    LanguageSelector
  },
  setup() {
    const store = useStore()
    const { t } = useI18n()
    const isLoggedIn = computed(() => store.getters['auth/isAuthenticated'])

    const logout = () => {
      store.dispatch('auth/logout')
    }

    return { isLoggedIn, logout, t }
  }
}
</script>
