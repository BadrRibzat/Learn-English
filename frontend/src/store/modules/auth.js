import api from '@/services/api';

export default {
  namespaced: true,
  state: {
    user: null,
    token: localStorage.getItem('token') || null,
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user;
    },
    SET_TOKEN(state, token) {
      state.token = token;
      localStorage.setItem('token', token);
    },
    CLEAR_AUTH(state) {
      state.user = null;
      state.token = null;
      localStorage.removeItem('token');
    },
    UPDATE_USER_LEVEL(state, level) {
      if (state.user) {
        state.user.current_level = level;
      }
    },
  },
  actions: {
    async login({ commit, dispatch }, credentials) {
      try {
        const response = await api.login(credentials);
        commit('SET_TOKEN', response.data.access);
        commit('SET_USER', response.data.user);
        return response;
      } catch (error) {
        console.error('Login failed:', error);
        throw error;
      }
    },
    async register({ commit, dispatch }, userData) {
      try {
        const response = await api.register(userData);
        commit('SET_TOKEN', response.data.access);
        commit('SET_USER', response.data.user);
        return response;
      } catch (error) {
        console.error('Registration failed:', error);
        throw error;
      }
    },
    async fetchUserProfile({ commit }) {
      try {
        const response = await api.getUserProfile();
        commit('SET_USER', response.data);
        return response;
      } catch (error) {
        console.error('Fetching user profile failed:', error);
        throw error;
      }
    },
    setLanguage({ commit, state }, language) {
      return api.updateUserProfile({ ...state.user, native_language: language })
        .then(response => {
          commit('SET_USER', response.data);
        });
    },
    updateUserLevel({ commit }, level) {
      commit('UPDATE_USER_LEVEL', level);
    },
    logout({ commit }) {
      commit('CLEAR_AUTH');
    },
  },
  getters: {
    isAuthenticated: state => !!state.token,
    currentUser: state => state.user,
  },
};
