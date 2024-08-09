import api from '@/services/api';

export default {
  namespaced: true,
  state: {
    progress: [],
    loading: false,
    error: null
  },
  mutations: {
    SET_PROGRESS(state, progress) {
      state.progress = progress;
    },
    UPDATE_PROGRESS(state, updatedProgress) {
      const index = state.progress.findIndex(p => p._id === updatedProgress._id);
      if (index !== -1) {
        state.progress.splice(index, 1, updatedProgress);
      } else {
        state.progress.push(updatedProgress);
      }
    },
    SET_LOADING(state, loading) {
      state.loading = loading;
    },
    SET_ERROR(state, error) {
      state.error = error;
    }
  },
  actions: {
    async fetchUserProgress({ commit }) {
      commit('SET_LOADING', true);
      try {
        const response = await api.getUserProgress();
        commit('SET_PROGRESS', response.data);
      } catch (error) {
        commit('SET_ERROR', error.message);
      } finally {
        commit('SET_LOADING', false);
      }
    },
    async updateUserProgress({ commit }, { lessonId, data }) {
      commit('SET_LOADING', true);
      try {
        const response = await api.updateUserProgress(lessonId, data);
        commit('UPDATE_PROGRESS', response.data);
      } catch (error) {
        commit('SET_ERROR', error.message);
      } finally {
        commit('SET_LOADING', false);
      }
    }
  },
  getters: {
    getProgressByLessonId: (state) => (lessonId) => {
      return state.progress.find(p => p.lesson === lessonId);
    }
  }
};
