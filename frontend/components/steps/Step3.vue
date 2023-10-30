<template>
  <form @submit.prevent>
    <label for="title">Jako kto upublicznij</label>
    <select>
      <option value="1">Anonimowo</option>
      <option value="2">ty (nick)</option>
      <option value="2">ty (nick)</option>
    </select>

    <button type="submit" @click="submit">Udostępnij</button>
  </form>
</template>

<script setup lang="ts">
import { useAddAnimeFormStore } from "@/stores/addAnimeStore";
import { useUserStore } from "@/stores/userStore";
import { useNotificationStore } from "@/stores/notificationStore";
import { NotificationType } from "@/stores/notificationStore";

const router = useRouter();

const store = useAddAnimeFormStore();
const user = useUserStore();
const notificationStore = useNotificationStore();

const ENV = useRuntimeConfig().public;
const API_URL = ENV.API_URL;

function submit() {
  // add anime

  const payload = {
    name: store.series,
    video_url: store.iframe,
    season: store.season,
    episode: store.episode,
    user_id: user.userId,
    group_id: null,

    // name: int
    // video_url: str
    // season: int
    // episode: int
    // user_id: int
    // group_id: int
  };

  $fetch(API_URL + "/videos/add", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  }),
    notificationStore.addNotification(NotificationType.succesfulVideoAdd);
  router.push("/");
}
</script>

<style scoped>
button {
  margin-top: 1rem;
  background-color: var(--accent-color--opacity);
  color: #fff;
  border: none;
  padding: 1rem 2rem;
  border-radius: 0.5rem;
  font-size: 1.5rem;
  cursor: pointer;
}

button:hover {
  transition: 0.2s;
  background-color: var(--accent-color);
}
</style>
