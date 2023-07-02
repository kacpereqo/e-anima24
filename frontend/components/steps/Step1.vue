<template>
  <form>
    <label for="title">Tytuł</label>
    <input type="text" v-model="store.title" class="input" />

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
  </form>
</template>

<script setup lang="ts">
import { useAddAnimeFormStore } from "@/stores/addAnimeStore";

const store = useAddAnimeFormStore();
</script>
