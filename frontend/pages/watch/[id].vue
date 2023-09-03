<template>
  <div class="watch-page">
    <div class="player">
      <iframe
        src="https://www.youtube.com/embed/OyDyOweu-PA"
        title="Polish cow (English Lyrics Full Version)"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
      ></iframe>
      <div class="episodes">
        <EpisodeCard v-for="idx in [1, 2, 3, 4, 5]" :key="idx" />
      </div>
    </div>
    <div class="info">
      <h2>polska krowa tanczy poloneza</h2>
    </div>
  </div>
</template>

<style scoped>
.info {
  width: 100%;
  display: flex;
  justify-content: flex-start;
}
.watch-page {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin: 4rem;
  gap: 2rem;
}

.player {
  display: flex;
  width: 100%;
  gap: 2rem;
  height: 80vh;
}

.episodes {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  overflow: scroll;
}

.player iframe {
  flex: 1;
}
</style>
