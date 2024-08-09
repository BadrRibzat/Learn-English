import './assets/styles/tailwind.css'
import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import i18n from './i18n'  // This should be your pre-configured i18n instance
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { 
  faGraduationCap, 
  faBook, 
  faQuestionCircle, 
  faSignInAlt, 
  faUserPlus, 
  faSignOutAlt, 
  faLanguage, 
  faChartLine 
} from '@fortawesome/free-solid-svg-icons'
import { 
  faFacebook, 
  faTwitter, 
  faInstagram 
} from '@fortawesome/free-brands-svg-icons'

library.add(
  faGraduationCap, 
  faBook, 
  faQuestionCircle, 
  faSignInAlt, 
  faUserPlus, 
  faSignOutAlt, 
  faLanguage, 
  faChartLine,
  faFacebook, 
  faTwitter, 
  faInstagram
)

const app = createApp(App)

app.use(router)
app.use(store)
app.use(i18n)
app.component('font-awesome-icon', FontAwesomeIcon)

app.mount('#app')
