<template>
  <div class="showcase">
    <h2 class="title">
      <Icon name="material-symbols:auto-awesome-rounded" />
      <span>new</span>
    </h2>
    <div class="wrapper">
      <div class="anime-list">
        <AnimeCardNew
          v-for="(video, idx) in recentVideos"
          :key="idx"
          :image-url="video.thumbnail"
          :id="video.video_id"
        />
      </div>
    </div>
    <div class="arrow-right"></div>
  </div>
</template>

<script setup lang="ts">
const ENV = useRuntimeConfig().public;
const API_URL = ENV.API_URL;

const recentVideos = await $fetch(API_URL + "/videos/recent/10");
</script>

<style scoped>
.showcase {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  margin: 0 2rem;
}

.title {
  display: flex;
  align-items: center;
  gap: 1rem;
  cursor: pointer;
}

.icon {
  color: var(--accent-color);
}

.wrapper {
  position: relative;
  width: 100%;
  height: calc(15rem + 1.7rem);
}

.anime-list {
  display: flex;
  gap: 1rem;
  position: absolute;
  top: 0;
}
</style>
