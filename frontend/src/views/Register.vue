<template>
  <div class="container mx-auto mt-8">
    <h2 class="text-2xl font-bold mb-4">Register</h2>
    <form @submit.prevent="register" class="max-w-md">
      <div class="mb-4">
        <label for="username" class="block mb-2">Username</label>
        <input type="text" id="username" v-model="username" required class="w-full px-3 py-2 border rounded">
      </div>
      <div class="mb-4">
        <label for="email" class="block mb-2">Email</label>
        <input type="email" id="email" v-model="email" required class="w-full px-3 py-2 border rounded">
      </div>
      <div class="mb-4">
        <label for="password" class="block mb-2">Password</label>
        <input type="password" id="password" v-model="password" required class="w-full px-3 py-2 border rounded">
      </div>
      <div class="mb-4">
        <label for="password2" class="block mb-2">Confirm Password</label>
        <input type="password" id="password2" v-model="password2" required class="w-full px-3 py-2 border rounded">
      </div>
      <div class="mb-4">
        <label for="native_language" class="block mb-2">Native Language</label>
        <select id="native_language" v-model="nativeLanguage" required class="w-full px-3 py-2 border rounded">
          <option value="KO">Korean</option>
          <option value="EN">English</option>
          <option value="ZH">Chinese</option>
          <option value="JA">Japanese</option>
          <option value="FR">French</option>
          <option value="ES">Spanish</option>
          <option value="AR">Arabic</option>
          <option value="DE">German</option>
        </select>
      </div>
      <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded">Register</button>
    </form>
    <div v-if="error" class="mt-4 text-red-500">{{ error }}</div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

export default {
  name: 'Register',
  setup() {
    const store = useStore()
    const router = useRouter()
    const username = ref('')
    const email = ref('')
    const password = ref('')
    const password2 = ref('')
    const nativeLanguage = ref('')
    const error = ref('')

    const register = async () => {
      if (password.value !== password2.value) {
        error.value = "Passwords do not match"
        return
      }
      try {
        await store.dispatch('auth/register', {
          username: username.value,
          email: email.value,
          password: password.value,
          password2: password2.value,
          native_language: nativeLanguage.value
        })
        router.push('/lessons')
      } catch (err) {
        console.error('Registration failed:', err)
        error.value = err.response?.data?.error || 'Registration failed. Please try again.'
      }
    }

    return { username, email, password, password2, nativeLanguage, register, error }
  }
}
</script>
