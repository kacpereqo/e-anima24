<template>
  <form>
    <label for="title">Miniaturka</label>
    <input type="file" />

    <lable for="iframe">Link do odcinka</lable>
    <input type="text" v-model="store.iframe" class="input" />
  </form>
</template>

<script setup lang="ts">
import { useAddAnimeFormStore } from "@/stores/addAnimeStore";

const store = useAddAnimeFormStore();
</script>
