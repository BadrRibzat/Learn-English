import api from '@/services/api';

export default {
  namespaced: true,
  state: {
    list: [],
    currentLesson: null,
    loading: false,
    error: null,
    userProgress: {}
  },
  mutations: {
    SET_LESSONS(state, lessons) {
      state.list = lessons;
    },
    SET_CURRENT_LESSON(state, lesson) {
      state.currentLesson = lesson;
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
    UPDATE_LESSON_PROGRESS(state, { lessonId, progress }) {
      state.userProgress = {
        ...state.userProgress,
        [lessonId]: {
          ...state.userProgress[lessonId],
          ...progress
        }
      };
    }
  },
  actions: {
    async fetchLessons({ commit }) {
      commit('SET_LOADING', true);
      try {
        const response = await api.getLessons();
        commit('SET_LESSONS', response.data);
      } catch (error) {
        commit('SET_ERROR', error.message);
      } finally {
        commit('SET_LOADING', false);
      }
    },
    async fetchLesson({ commit }, lessonId) {
      commit('SET_LOADING', true);
      try {
        const response = await api.getLesson(lessonId);
        commit('SET_CURRENT_LESSON', response.data);
      } catch (error) {
        commit('SET_ERROR', error.message);
      } finally {
        commit('SET_LOADING', false);
      }
    },
    async fetchUserProgress({ commit }) {
      try {
        const response = await api.getUserProgress();
        commit('SET_USER_PROGRESS', response.data);
      } catch (error) {
        commit('SET_ERROR', error.message);
      }
    },
    async updateUserProgress({ commit }, { lessonId, data }) {
      try {
        const response = await api.updateUserProgress(lessonId, data);
        commit('UPDATE_LESSON_PROGRESS', { lessonId, progress: response.data });
      } catch (error) {
        commit('SET_ERROR', error.message);
      }
    },
    async completeLesson({ dispatch }, lessonId) {
      await dispatch('updateUserProgress', { 
        lessonId, 
        data: { completed: true, completedAt: new Date().toISOString() }
      });
    },
    async updateQuizScore({ dispatch }, { lessonId, score }) {
      await dispatch('updateUserProgress', { 
        lessonId, 
        data: { quizScore: score, lastAttemptAt: new Date().toISOString() }
      });
    }
  },
  getters: {
    getLessonById: (state) => (id) => {
      return state.list.find(lesson => lesson._id === id);
    },
    getLessonProgress: (state) => (lessonId) => {
      return state.userProgress[lessonId] || { 
        completed: false, 
        quizScore: 0, 
        completedAt: null,
        lastAttemptAt: null
      };
    },
    overallProgress: (state) => {
      const totalLessons = state.list.length;
      const completedLessons = Object.values(state.userProgress).filter(progress => progress.completed).length;
      return (completedLessons / totalLessons) * 100;
    },
    averageQuizScore: (state) => {
      const scores = Object.values(state.userProgress)
        .filter(progress => progress.quizScore !== undefined)
        .map(progress => progress.quizScore);
      if (scores.length === 0) return 0;
      return scores.reduce((a, b) => a + b, 0) / scores.length;
    }
  }
  completedLessonsCount: (state) => {
    return Object.values(state.userProgress).filter(progress => progress.completed).length;
  }
};
