<template>
  <div class="anime-card">
    <nuxt-link :to="`/watch/${id}`">
      <div class="image-container">
        <nuxt-img :src="imageUrl" alt="anime image" />
      </div>
      <h3 class="title"></h3>
    </nuxt-link>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  imageUrl: string;
  id: string;
}>();
</script>

<style scoped>
.anime-card {
  width: 15rem;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.image-container {
  width: 15rem;
  height: 19rem;
  border-radius: 0.5rem;
  position: relative;
  overflow: hidden;
}

.image-container img {
  width: 100%;
  height: 100%;
  object-fit: fill;
}

.title {
  font-weight: 300;
  font-size: var(--font-size-2);
}
</style>
