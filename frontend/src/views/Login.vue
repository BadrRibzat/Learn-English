<template>
  <div class="max-w-md mx-auto">
    <h2 class="text-3xl font-bold mb-6 text-center">Login</h2>
    <form @submit.prevent="login" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
          Username
        </label>
        <input 
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
          id="username" 
          type="text" 
          placeholder="Username"
          v-model="username" 
          required
        >
      </div>
      <div class="mb-6">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
          Password
        </label>
        <input 
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" 
          id="password" 
          type="password" 
          placeholder="******************"
          v-model="password" 
          required
        >
      </div>
      <div class="flex items-center justify-between">
        <button 
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" 
          type="submit"
        >
          Sign In
        </button>
        <router-link 
          class="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800" 
          to="/register"
        >
          Need an account?
        </router-link>
      </div>
    </form>
    <div v-if="error" class="text-red-500 text-center mt-4">{{ error }}</div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

export default {
  name: 'Login',
  setup() {
    const store = useStore()
    const router = useRouter()
    const username = ref('')
    const password = ref('')
    const error = ref('')

    const login = async () => {
      try {
        await store.dispatch('auth/login', { username: username.value, password: password.value })
        router.push('/lessons')
      } catch (err) {
        console.error('Login failed:', err)
        error.value = 'Login failed. Please check your credentials and try again.'
      }
    }

    return { username, password, login, error }
  }
}
</script>
