<template>
  <div class="watch-page">
    <div class="content" ref="content">
      <div class="player">
        <iframe :src="iframeSrc" frameborder="0" allowfullscreem></iframe>
      </div>
      <div class="info">
        <h2>{{ data?.name }} S{{ data?.season }} E{{ data?.episode }}</h2>
        •
        <h3>{{ data?.views }} {{ viewsName(data?.views) }}</h3>
        •
        <div class="likes">
          {{ data?.likes }}
          <Icon class="like" @click="like" name="ic:baseline-thumb-up" />
          {{ data?.dislikes }}
          <Icon
            class="dislike"
            @click="dislike"
            name="ic:baseline-thumb-down"
          />
        </div>
      </div>
      <div class="comments">
        <div class="add-comment">
          <textarea @input="resizeTextarea" rows="1" placeholder="Napisz" />
          <button>Dodaj komentarz</button>
        </div>
      </div>
    </div>
    <div class="episodes" ref="episodes">
      <EpisodeCard v-for="idx in [0, 1, 2, 3, 4, 5]" :key="idx" />
    </div>
  </div>
</template>

<script setup lang="ts">
const route = useRoute();
const id = route.params.id;

const ENV = useRuntimeConfig().public;
const API_URL = ENV.API_URL;
const iframeSrc = ref("");

const episodes = ref();
const content = ref();

function viewsName(views: any) {
  if (views === 1) return "wyświetlenie";
  if (views > 1 && views < 5) return "wyświetlenia";
  return "wyświetleń";
}

const { data } = useFetch<Anime>(API_URL + "/videos/" + id, {
  onResponse: (res) => {
    const iframe = res.response._data.video_url;

    // extract src from iframe
    const parser = new DOMParser();

    const doc = parser.parseFromString(iframe, "text/html");
    iframeSrc.value = doc.querySelector("iframe")!.src;
  },
});

function resizeTextarea() {
  const textarea = document.querySelector("textarea")!;
  textarea.style.height = "auto";
  textarea.style.height = textarea.scrollHeight + "px";
}

function incrementViews() {
  fetch(API_URL + "/videos/" + id + "/views/add", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
}

function like() {
  data.value!.likes++;
}

function dislike() {
  data.value!.dislikes++;
}

onMounted(() => {
  incrementViews();

  const contentHeight = content.value!.clientHeight;
  const episodesHeight = content.value!.clientHeight;

  if (contentHeight > episodesHeight) {
    content.value!.style.height = contentHeight + "px";
    episodes.value!.style.height = contentHeight + "px";
  } else {
    content.value!.style.height = episodesHeight + "px";
    episodes.value!.style.height = episodesHeight + "px";
  }
});

interface Anime {
  id: number;
  name: string;
  video_url: string;
  season: number;
  episode: number;
  user_id: number;
  group_id: number;
  views: number;
  likes: number;
  dislikes: number;
}
</script>

<style scoped>
.info {
  margin: 1rem;
  width: 100%;
  display: flex;
  gap: 1rem;
  justify-content: flex-start;
  align-items: center;
}
.watch-page {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row;
  margin: 4rem;
  gap: 2rem;
}

.content {
  flex: 1;
}

.player {
  display: flex;
  width: 100%;
  gap: 2rem;
  height: 80vh;
}

.episodes {
  display: flex;
  flex-direction: column;
  gap: 1rem;

  overflow: scroll;
}

.player iframe {
  flex: 1;
}

.like:hover,
.dislike:hover {
  color: var(--accent-color);
  transition: 0.1s;
  cursor: pointer;
}

.add-comment {
  display: flex;
  flex: 1;
  flex-direction: row;
  gap: 1rem;
}

.add-comment textarea {
  flex: 1;
  resize: none;
  overflow: hidden;
  border: none;
  border-bottom: 1px solid var(--accent-color);
  background-color: transparent;

  font-family: "Roboto", sans-serif;
  color: var(--text-color);
  font-size: 1.4rem;
}

.add-comment button {
  border: none;
  background-color: var(--accent-color);
  color: var(--text-color);
  height: 4rem;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  font-size: 1.4rem;
  font-family: "Roboto", sans-serif;
  cursor: pointer;
}

.comments {
  display: flex;
  flex: 1;
  width: 100%;
}
</style>
