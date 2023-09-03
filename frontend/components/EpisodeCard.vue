<template>
  <div class="episode-card">
    <img :src="imgUrl" alt="episode cover" />
  </div>
</template>

<script setup lang="ts">
const imgUrl = "https://picsum.photos/300/200?random=" + Math.random();
</script>

<style scoped></style>
