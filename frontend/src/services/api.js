import axios from 'axios';

const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL || 'http://localhost:8000/api/',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add a request interceptor
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token && config.url !== 'chatbot/') {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default {
  // Auth
  login(credentials) {
    return api.post('token/', credentials);
  },
  register(userData) {
    return api.post('register/', userData);
  },

  // Chatbot
  sendChatMessage(message) {
    return axios.post(`${process.env.VUE_APP_API_URL}/chatbot/`, { message });
  },
  
  // Lessons
  getLessons() {
    return api.get('lessons/visitor/');
  },
  getLesson(id) {
    return api.get(`lessons/${id}/`);
  },
  
  // Flashcards
  getFlashcards(lessonId) {
    return api.get(`lessons/${lessonId}/flashcards/`);
  },
  
  // Quizzes
  getQuizzes() {
    return api.get('quizzes/');
  },
  getQuiz(id) {
    return api.get(`quizzes/${id}/`);
  },
  submitQuiz(quizId, answers) {
    return api.post(`quizzes/${quizId}/submit/`, { answers });
  },
  getUserQuizProgress() {
    return api.get('quizzes/progress/');
  },
  
  // User Progress
  getUserProgress() {
    return api.get('progress/');
  },
  updateUserProgress(lessonId, data) {
    return api.post(`progress/${lessonId}/`, data);
  },
  
  // Achievements
  getAchievements() {
    return api.get('achievements/');
  },
  getUserAchievements() {
    return api.get('user/achievements/');
  },
  
  // User Profile
  getUserProfile() {
    return api.get('user/profile/');
  },
  updateUserProfile(data) {
    return api.put('user/profile/', data);
  },
};
