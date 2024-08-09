import api from '@/services/api';

export default {
  namespaced: true,
  state: {
    list: [],
    loading: false,
    error: null
  },
  mutations: {
    SET_FLASHCARDS(state, flashcards) {
      state.list = flashcards;
    },
    SET_LOADING(state, loading) {
      state.loading = loading;
    },
    SET_ERROR(state, error) {
      state.error = error;
    }
  },
  actions: {
    async fetchFlashcards({ commit }, lessonId) {
      commit('SET_LOADING', true);
      try {
        const response = await api.getFlashcards(lessonId);
        commit('SET_FLASHCARDS', response.data);
      } catch (error) {
        commit('SET_ERROR', error.message);
      } finally {
        commit('SET_LOADING', false);
      }
    }
  }
};
