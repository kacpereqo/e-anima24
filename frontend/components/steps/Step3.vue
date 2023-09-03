<template>
  <form>
    <label for="title">Tagi</label>
    <Multiselect :data="tags" v-model:selecteds="store.tags" />

    <label for="description">Gatunki</label>
    <Multiselect :data="genres" v-model:selecteds="store.genres" />
  </form>
</template>

<script setup lang="ts">
import { useAddAnimeFormStore } from "@/stores/addAnimeStore";

const genres = ref([
  "Akcja",
  "Komedia",
  "Dramat",
  "Fantasy",
  "Harem",
  "Horror",
  "Mecha",
]);

const tags = ref([
  "Akcja",
  "Komedia",
  "Dramat",
  "Fantasy",
  "Harem",
  "Horror",
  "Mecha",
]);

const store = useAddAnimeFormStore();
</script>

<style scoped></style>
