<template>
  <div class="notification">
    <div class="close">
      <Icon
        name="material-symbols:close-rounded"
        @click="
          {
            emit('close');
            tl.play(0);
            bar!.style.width = '0%';
          }
        "
      />
    </div>
    <div class="content">
      <Icon :name="icons[props.notification.type]" class="notifciation-type" />
      <div class="message">
        <h3>{{ props.notification.title }}</h3>
        <p>
          {{ props.notification.message }}
        </p>
      </div>
    </div>

    <div ref="bar" class="progress-bar" />
  </div>
</template>

<script setup lang="ts">
import { gsap } from "gsap";

const bar = ref<HTMLElement | null>(null);
const tl = gsap.timeline();

enum icons {
  info = "material-symbols:info-rounded",
  success = "material-symbols:check-circle-rounded",
  warning = "material-symbols:warning-rounded",
  error = "material-symbols:error-rounded",
}

interface Notification {
  message: string;
  title: string;
  type: "info" | "success" | "warning" | "error";
}

const emit = defineEmits<{
  (e: "close"): void;
}>();

const props = defineProps<{
  notification: Notification;
  startAnimation: boolean;
}>();

function animate() {
  tl.to(bar.value, {
    width: "100%",
    duration: 3,
    ease: "none",
    onComplete: () => {
      bar.value!.style.width = "0%";
      emit("close");
    },
  });
}

onMounted(() => {
  if (props.startAnimation) {
    animate();
  }
});

onUpdated(() => {
  if (props.startAnimation) {
    animate();
  }
});
</script>

<style scoped>
.progress-bar {
  width: 0%;
  background-color: var(--accent-color);
  height: 0.5rem;
}

.close {
  cursor: pointer;
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
}

.notifciation-type {
  width: 3rem;
  height: 3rem;
  flex-shrink: 0;
}
.content {
  display: flex;
  align-items: center;
  height: 100%;
  padding: 1rem;
  gap: 1rem;
}

.message {
  height: 100%;
  display: flex;
  flex-direction: column;
}
.notification {
  position: relative;
  width: 30rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow: hidden;
  background-color: var(--second-color);
  box-shadow: 0 0 0.5rem 0 rgba(150, 150, 150, 0.3);
  margin-bottom: 1rem;
  color: white;
}
</style>
