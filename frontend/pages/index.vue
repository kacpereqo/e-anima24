<template>
  <div class="index-page">
    <TheFeaturedAnime />
    <div class="anime-showcase-list">
      <AnimeShowCaseNew />
      <AnimeShowCase category="popular" />
      <AnimeShowCase category="trending" />
    </div>
  </div>
</template>

<style scoped>
.index-page {
  flex: 1;
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
