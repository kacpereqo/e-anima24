<template>
  <form>
    <label for="title">Tagi</label>
    <Multiselect :data="tags" v-model:selecteds="store.tags" />

    <label for="description">Gatunki</label>
    <Multiselect :data="genres" v-model:selecteds="store.genres" />

    <label for="iframe">Link do odcinka</label>
    <input type="text" v-model="store.iframe" class="input" />
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
