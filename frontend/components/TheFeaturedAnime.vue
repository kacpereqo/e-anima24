<template>
  <div id="featured-anime">
    <div class="slider">
      <div class="info">
        <h2 class="title">{{ title }}</h2>
        <p class="description">
          {{ description }}
        </p>
        <div class="action-buttons">
          <button class="watch">
            <Icon name="material-symbols:play-arrow" />
            Watch Now
          </button>
          <button class="more-info">
            <Icon name="material-symbols:info-rounded" />
            More Info
          </button>
        </div>
      </div>
      <nuxt-img :src="imageUrl" preload />
    </div>
    <div class="dots" ref="dots">
      <div
        v-for="idx in [1, 2, 3, 4, 5]"
        class="dot"
        :key="idx"
        @click="changeCarouselTo(idx - 1)"
      ></div>
    </div>
    <div class="progress-bar" ref="progressBar"></div>
  </div>
</template>

<script setup lang="ts">
import { LoremIpsum } from "lorem-ipsum";

const description = ref(
  "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Corrupti numquam dolorum repellat veritatis omnis odio modi praesentium earum assumenda voluptates id delectus soluta veniam distinctio, exercitationem cupiditate facilis est neque."
);
const title = ref<string>("Featured Anime");
const imageUrl = ref<string>("https://picsum.photos/1080/720");
const counter = ref<number>(0);

const progressBar = ref<HTMLElement | null>(null);
const dots = ref<HTMLElement | null>(null);

let carouselInterval: any = null;

const lorem = new LoremIpsum({
  sentencesPerParagraph: {
    max: 8,
    min: 4,
  },
  wordsPerSentence: {
    max: 16,
    min: 4,
  },
});

function changeCarouselTo(idx: number) {
  clearTimeout(carouselInterval);
  counter.value = idx;

  colorDots();
  getInfo();
  clearProgressBar();

  changeFeaturedAnime();
}

function clearProgressBar() {
  if (!progressBar.value) return;

  progressBar.value.classList.remove("loading-animation");
  setTimeout(() => {
    if (!progressBar.value) return;
    progressBar.value.classList.add("loading-animation");
  }, 1);
}

function colorDots() {
  if (!dots.value) return;
  const dotsArray = Array.from(dots.value.children);
  dotsArray.forEach((dot, index) => {
    if (index === counter.value) {
      dot.classList.add("active");
    } else {
      dot.classList.remove("active");
    }
  });
}

function getInfo() {
  imageUrl.value = "https://picsum.photos/1080/720?random=" + Math.random();
  title.value = lorem.generateWords(1);
  description.value = lorem.generateSentences(2);
}

function changeFeaturedAnime() {
  carouselInterval = setTimeout(() => {
    if (!dots.value) return;
    if (!progressBar.value) return;

    counter.value = (counter.value + 1) % dots.value.children.length;

    getInfo();
    colorDots();
    clearProgressBar();
    changeFeaturedAnime();
  }, 12 * 1000);
}

onMounted(() => {
  if (!progressBar.value) return;
  if (!dots.value) return;

  progressBar.value.classList.add("loading-animation");
  dots.value.children[0].classList.add("active");
  changeFeaturedAnime();
});
</script>

<style scoped>
#featured-anime {
  position: relative;
  z-index: 10;
  height: 60rem;
}
.progress-bar {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0%;
  height: 0.3rem;
  background-color: var(--accent-color);
}

.loading-animation {
  animation: loading 12s linear forwards;
}

@keyframes loading {
  0% {
    width: 0%;
  }
  100% {
    width: 100%;
  }
}

.slider {
  position: relative;
  z-index: initial;
  background-color: var(--second-color--opacity);
  width: 100%;
  height: 100%;
}

.dots {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  bottom: 10px;
  display: flex;
  gap: 1rem;
  padding: 1rem;
  z-index: 1000;
}

.dot {
  box-sizing: content-box;
  cursor: pointer;
  width: 1rem;
  height: 1rem;
  border-radius: 50%;
  background-color: var(--font-color--dark);
}

.active {
  background-color: var(--accent-color);
}

.info {
  z-index: 1000;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  position: absolute;
  bottom: 40%;
  left: 5%;
  max-width: 35rem;
}

.title {
  font-size: var(--font-size-10);
  font-weight: bolder;
}

.description {
  font-size: var(--font-size-3);
  text-align: justify;
}

.slider img {
  position: relative;
  z-index: -1;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.action-buttons {
  display: flex;
  gap: 1rem;
  align-content: center;
  justify-content: center;
}

.action-buttons button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  justify-content: center;
  flex: 1;
  font-weight: 500;
  font-size: var(--font-size-4);
  transition: all 0.2s ease-in-out;
  border: none;
  padding: 1rem;
  border-radius: 0.5rem;
  color: white;
  cursor: pointer;
}

.watch {
  background-color: var(--accent-color--opacity);
}

.watch:hover {
  background-color: var(--accent-color);
}

.more-info {
  background-color: var(--second-color--opacity);
}

.more-info:hover {
  background-color: var(--second-color);
}
</style>
