<template>
  <form>
    <label for="series">Seria</label>
    <Autocomplete
      :data="data"
      :add-text="{
        first: 'Dodaj nową serię',
        second: 'Jeśli nie ma jej na liście',
      }"
    />
    <div class="seasons">
      <label for="season">Sezon <Info>giga niga</Info></label>
      <label for="episode">Odcinek</label>
      <input
        class="input"
        type="number"
        v-model="store.season"
        :disabled="!store.series"
        min="1"
        step="1"
      />
      <input
        :disabled="!store.season"
        class="input"
        type="number"
        v-model="store.episode"
        min="1"
        step="1"
      />
    </div>
  </form>
</template>

<script setup lang="ts">
import { useAddAnimeFormStore } from "@/stores/addAnimeStore";
const data = ref([
  "Pokemon",
  "Naruto",
  "Bleach",
  "One Piece",
  "Dragon Ball",
  "Death Note",
  "Attack on Titan",
  "Fullmetal Alchemist",
  "Sword Art Online",
  "Fairy Tail",
  "Hunter x Hunter",
]);

const store = useAddAnimeFormStore();
</script>

<style scoped>
.seasons {
  column-gap: 2rem;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(2, 1fr);
}
</style>
