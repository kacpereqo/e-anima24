<template>
  <div class="index-page">
    <TheFeaturedAnime />
    <div class="anime-showcase-list">
      <AnimeShowCase category="popular" />
      <AnimeShowCase category="trending" />
      <AnimeShowCase category="new" />
    </div>
  </div>
</template>

<style scoped>
.index-page {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 3rem;
}

.anime-showcase-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
</style>
