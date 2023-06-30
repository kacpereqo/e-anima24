<template>
  <div class="showcase">
    <h2 class="title" @mouseenter="titleAnimation" ref="title">
      <Icon class="icon" :name="icon" />
      <span>{{ category }}</span>
    </h2>
    <div class="wrapper">
      <div class="anime-list">
        <AnimeCard v-for="idx in [1, 2, 3, 4, 5, 6]" :key="idx" />
      </div>
    </div>
    <div class="arrow-right"></div>
  </div>
</template>

<script setup lang="ts">
const title = ref<HTMLElement | null>(null);

type category = "popular" | "trending" | "new";

const icon = computed(() => {
  switch (props.category) {
    case "popular":
      return "streamline:interface-content-fire-lit-flame-torch-trending";
    case "trending":
      return "fluent:arrow-trending-24-filled";
    case "new":
      return "material-symbols:auto-awesome-rounded";
  }
});

function titleAnimation() {
  if (!title.value) return;
}

const props = defineProps<{
  category: category;
}>();
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
