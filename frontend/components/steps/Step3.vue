<template>
  <form>
    <label for="title">Tagi</label>
    <Multiselect :data="data" />

    <label for="description">Gatunki</label>
    <input type="text" v-model="store.genres" class="input" />
  </form>
</template>

<script setup lang="ts">
import { useAddAnimeFormStore } from "@/stores/addAnimeStore";

const data = ref([
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
