<template>
  <form>
    <option>
      <select v-model="store.category" class="input">
        <option value="pokemon">pokemon</option>
        <option value="naruto">naruto</option>
        <option value="death note">death note</option>
      </select>
    </option>
  </form>
</template>

<script setup lang="ts">
import { useAddAnimeFormStore } from "@/stores/addAnimeStore";

const store = useAddAnimeFormStore();
</script>
