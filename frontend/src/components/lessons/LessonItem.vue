<template>
  <div class="lesson-item">
    <h3 class="text-xl font-semibold mb-2">{{ lesson.title }}</h3>
    <p class="mb-4">{{ lesson.description }}</p>
    <router-link :to="`/lessons/${lesson._id}`" class="btn btn-primary">
      {{ $t('lessons.startLesson') }}
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'LessonItem',
  props: {
    lesson: {
      type: Object,
      required: true
    }
  }
}
</script>
