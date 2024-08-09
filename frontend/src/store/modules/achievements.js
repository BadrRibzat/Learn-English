import api from '@/services/api';

export default {
  namespaced: true,
  state: {
    list: [],
    userAchievements: [],
    loading: false,
    error: null
  },
  mutations: {
    SET_ACHIEVEMENTS(state, achievements) {
      state.list = achievements;
    },
    SET_USER_ACHIEVEMENTS(state, achievements) {
      state.userAchievements = achievements;
    },
    SET_LOADING(state, loading) {
      state.loading = loading;
    },
    SET_ERROR(state, error) {
      state.error = error;
    }
  },
  actions: {
    async fetchAchievements({ commit }) {
      commit('SET_LOADING', true);
      try {
        const response = await api.getAchievements();
        commit('SET_ACHIEVEMENTS', response.data);
      } catch (error) {
        commit('SET_ERROR', error.message);
      } finally {
        commit('SET_LOADING', false);
      }
    },
    async fetchUserAchievements({ commit }) {
      commit('SET_LOADING', true);
      try {
        const response = await api.getUserAchievements();
        commit('SET_USER_ACHIEVEMENTS', response.data);
      } catch (error) {
        commit('SET_ERROR', error.message);
      } finally {
        commit('SET_LOADING', false);
      }
    }
  },
  getters: {
    getAchievementById: (state) => (id) => {
      return state.list.find(achievement => achievement._id === id);
    },
    hasAchievement: (state) => (id) => {
      return state.userAchievements.some(achievement => achievement._id === id);
    }
  }
};
