<template>
  <div id="app" class="min-h-screen bg-gray-100">
    <Header />
    <main class="container mx-auto mt-6 px-4 pb-12">
      <router-view></router-view>
    </main>
    <Footer />
  </div>
</template>

<script>
import Header from './components/common/Header.vue'
import Footer from './components/common/Footer.vue'

export default {
  name: 'App',
  components: {
    Header,
    Footer
  }
}
</script>
