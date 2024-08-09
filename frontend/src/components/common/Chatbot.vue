<template>
  <div class="fixed bottom-4 right-4 z-50">
    <button @click="toggleChat" class="bg-green-500 text-white rounded-full p-3 shadow-lg hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-300">
      <svg v-if="!isChatOpen" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
      </svg>
      <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
      </svg>
    </button>
    <div v-if="isChatOpen" class="absolute bottom-16 right-0 w-72 bg-white rounded-lg shadow-xl overflow-hidden">
      <div class="bg-green-500 text-white p-3 flex items-center">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
        </svg>
        <h3 class="text-lg font-semibold">Chatbot</h3>
      </div>
      <div class="h-64 overflow-y-auto p-3 bg-gray-100" ref="chatContainer">
        <div v-for="(message, index) in messages" :key="index" 
             :class="['mb-2 p-2 rounded-lg shadow text-sm', message.isUser ? 'bg-blue-500 text-white ml-auto' : 'bg-green-500 text-white']">
          {{ message.text }}
        </div>
        <div v-if="isLoading" class="text-center text-gray-600">
          <p>Thinking...</p>
        </div>
      </div>
      <div class="p-3 border-t bg-white">
        <form @submit.prevent="sendMessage">
          <div class="flex">
            <input v-model="userInput" type="text" placeholder="Type your message..." 
                   class="flex-grow border rounded-l px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-green-500 text-gray-700"
                   :disabled="isLoading">
            <button type="submit" class="bg-green-500 text-white px-3 py-2 rounded-r hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-300" :disabled="isLoading || !userInput.trim()">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
              </svg>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch, nextTick } from 'vue';
import api from '@/services/api';

export default {
  name: 'Chatbot',
  setup() {
    const isChatOpen = ref(false);
    const userInput = ref('');
    const messages = ref([]);
    const chatContainer = ref(null);
    const isLoading = ref(false);

    const toggleChat = () => {
      isChatOpen.value = !isChatOpen.value;
    };

    const sendMessage = async () => {
      if (!userInput.value.trim() || isLoading.value) return;

      const userMessage = userInput.value;
      messages.value.push({ text: userMessage, isUser: true });
      userInput.value = '';
      isLoading.value = true;

      try {
        console.log('Sending message:', userMessage);
        console.log('API URL:', process.env.VUE_APP_API_URL);
        const response = await api.sendChatMessage(userMessage);
        console.log('Received response:', response);
        messages.value.push({ text: response.data.response, isUser: false });
      } catch (error) {
        console.error('Error details:', error.response || error);
        console.error('Error config:', error.config);
        messages.value.push({ text: 'Sorry, I encountered an error. Please try again later.', isUser: false });
      } finally {
        isLoading.value = false;
      }
    };

    watch(messages, () => {
      nextTick(() => {
        if (chatContainer.value) {
          chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
        }
      });
    }, { deep: true });

    return {
      isChatOpen,
      userInput,
      messages,
      chatContainer,
      isLoading,
      toggleChat,
      sendMessage,
    };
  }
};
</script>
