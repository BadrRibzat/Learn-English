import { createI18n } from 'vue-i18n'
import en from './locales/en.json'
import fr from './locales/fr.json'
import es from './locales/es.json'
import ar from './locales/ar.json'
import de from './locales/de.json'
import ja from './locales/ja.json'
import ko from './locales/ko.json'
import zh from './locales/zh.json'

const messages = {
  en,
  fr,
  es,
  ar,
  de,
  ja,
  ko,
  zh
}

export default createI18n({
  legacy: false,
  globalInjection: true,
  locale: 'en', // set default locale
  fallbackLocale: 'en',
  messages
})
