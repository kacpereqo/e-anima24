<template>
  <div class="anime-card">
    <div class="image-container">
      <nuxt-img :src="imageUrl" alt="anime image" />
    </div>
    <h3 class="title">
      <!-- {{ title }} -->
    </h3>
  </div>
</template>

<script setup lang="ts">
import { LoremIpsum } from "lorem-ipsum";

const lorem = new LoremIpsum({
  sentencesPerParagraph: {
    max: 8,
    min: 4,
  },
  wordsPerSentence: {
    max: 16,
    min: 4,
  },
});

const title = ref<string>(lorem.generateWords(2));
const imageUrl = ref<string>(
  "https://picsum.photos/300/150?random=" + Math.random()
);
</script>

<style scoped>
.anime-card {
  width: 30rem;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.image-container {
  width: 30rem;
  height: 15rem;
  border-radius: 0.5rem;
  position: relative;
  overflow: hidden;
}

.title {
  font-weight: 300;
  font-size: var(--font-size-2);
}
</style>
