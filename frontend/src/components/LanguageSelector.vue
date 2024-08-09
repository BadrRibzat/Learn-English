<template>
  <select v-model="$i18n.locale" @change="changeLanguage">
    <option value="en">English</option>
    <option value="fr">Français</option>
    <option value="es">Español</option>
    <option value="ar">العربية</option>
    <option value="de">Deutsch</option>
    <option value="ja">日本語</option>
    <option value="ko">한국어</option>
    <option value="zh">中文</option>
  </select>
</template>

<script>
export default {
  name: 'LanguageSelector',
  methods: {
    changeLanguage(event) {
      this.$i18n.locale = event.target.value
      // You might want to save the selected language to localStorage or user preferences
    }
  }
}
</script>
