<template>
  <form>
    <label for="series">Seria</label>
    <Autocomplete :data="data" />

    <label for="description">Opis</label>
    <textarea
      oninput='this.style.height = "";this.style.height = this.scrollHeight + "px"'
      v-model="store.description"
      class="input"
    />

    <label for="description">Krótki opis</label>
    <textarea
      oninput='this.style.height = "";this.style.height = this.scrollHeight + "px"'
      v-model="store.shortDescription"
      class="input"
    />

    <div class="seasons">
      <label for="season">Sezon <Info>test Sezon </Info></label>
      <label for="episode">Odcinek <Info>Odcinek Sezonu </Info></label>
      <input class="input" v-model="store.season" min="1" step="1" />
      <input class="input" v-model="store.episode" min="1" step="1" />
    </div>
  </form>
</template>

<script setup lang="ts">
import { useAddAnimeFormStore } from "@/stores/addAnimeStore";
const data = ref();
const ENV = useRuntimeConfig().public;
const API_URL = ENV.API_URL;

const store = useAddAnimeFormStore();

watchEffect(() => {
  if (store.series) {
    fetch(`${API_URL}/autocomplete/series?query=${store.series}`)
      .then((res) => res.json())
      .then((res) => {
        data.value = res;
        console.log(data.value);
      });
  }
});
</script>

<style scoped>
.seasons {
  column-gap: 2rem;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(2, 1fr);
}
</style>
