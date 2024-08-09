import api from '@/services/api';

export default {
  namespaced: true,
  state: {
    list: [],
    currentQuiz: null,
    loading: false,
    error: null,
    userProgress: {}
  },
  mutations: {
    SET_QUIZZES(state, quizzes) {
      state.list = quizzes;
    },
    SET_CURRENT_QUIZ(state, quiz) {
      state.currentQuiz = quiz;
    },
    SET_LOADING(state, loading) {
      state.loading = loading;
    },
    SET_ERROR(state, error) {
      state.error = error;
    },
    SET_USER_PROGRESS(state, progress) {
      state.userProgress = progress;
    },
    UPDATE_QUIZ_PROGRESS(state, { quizId, progress }) {
      state.userProgress = {
        ...state.userProgress,
        [quizId]: {
          ...state.userProgress[quizId],
          ...progress
        }
      };
    }
  },
  actions: {
    async fetchQuizzes({ commit }) {
      commit('SET_LOADING', true);
      try {
        const response = await api.getQuizzes();
        commit('SET_QUIZZES', response.data);
      } catch (error) {
        commit('SET_ERROR', error.message);
      } finally {
        commit('SET_LOADING', false);
      }
    },
    async fetchQuiz({ commit }, quizId) {
      commit('SET_LOADING', true);
      try {
        const response = await api.getQuiz(quizId);
        commit('SET_CURRENT_QUIZ', response.data);
      } catch (error) {
        commit('SET_ERROR', error.message);
      } finally {
        commit('SET_LOADING', false);
      }
    },
    async submitQuiz({ commit }, { quizId, answers }) {
      commit('SET_LOADING', true);
      try {
        const response = await api.submitQuiz(quizId, answers);
        commit('UPDATE_QUIZ_PROGRESS', { 
          quizId, 
          progress: { 
            lastAttempt: new Date().toISOString(),
            bestScore: response.data.score
          } 
        });
        return response.data;
      } catch (error) {
        commit('SET_ERROR', error.message);
      } finally {
        commit('SET_LOADING', false);
      }
    },
    async fetchUserQuizProgress({ commit }) {
      try {
        const response = await api.getUserQuizProgress();
        commit('SET_USER_PROGRESS', response.data);
      } catch (error) {
        commit('SET_ERROR', error.message);
      }
    }
  },
  getters: {
    getQuizById: (state) => (id) => {
      return state.list.find(quiz => quiz._id === id);
    },
    getQuizProgress: (state) => (quizId) => {
      return state.userProgress[quizId] || { 
        bestScore: 0, 
        lastAttempt: null
      };
    }
  }
};
