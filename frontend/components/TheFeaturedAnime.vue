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
      <img :src="imageUrl" />
    </div>
    <div class="dots" ref="dots">
      <div class="dot active"></div>
      <div class="dot"></div>
      <div class="dot"></div>
    </div>
    <div class="progress-bar"></div>
  </div>
</template>

<script setup lang="ts">
const description = ref(
  "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Corrupti numquam dolorum repellat veritatis omnis odio modi praesentium earum assumenda voluptates id delectus soluta veniam distinctio, exercitationem cupiditate facilis est neque."
);
const title = ref("Featured Anime");
const imageUrl = ref("");
const counter = ref(0);
const dots = ref(null);

function changeFeaturedAnime() {
  imageUrl.value = "https://picsum.photos/1080/720?random=" + Math.random();
  title.value = "Featured Anime " + Math.random();
  description.value =
    "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Corrupti numquam dolorum repellat veritatis omnis odio modi praesentium earum assumenda voluptates id delectus soluta veniam distinctio, exercitationem cupiditate facilis est neque.";

  counter.value = (counter.value + 1) % dots.value.children.length;
  dots.value.children[counter.value].classList.add("active");
  //   counter.value = counter.value % dots.value.children.length;
  //   dots.value.children.forEach((dot, index) => {
  //     if (index === counter.value) {
  //       dot.classList.add("active");
  //     } else {
  //       dot.classList.remove("active");
  //     }
  //   });
}

onMounted(() => {
  const carousel = setInterval(changeFeaturedAnime, 3000);
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
  animation: loading 3s linear infinite;
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
  top: 25%;
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
