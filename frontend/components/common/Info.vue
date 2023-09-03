<template>
  <div class="info" ref="info">
    <Icon name="material-symbols:info-outline-rounded" ref="icon" />
    <div class="info-box" v-if="isHovered">
      <slot />
    </div>
  </div>
</template>

<script setup lang="ts">
const info = ref<HTMLElement | null>(null);

const isHovered = useElementHover(info, { delayEnter: 100, delayLeave: 100 });
</script>

<style scoped>
.info {
  position: relative;
  z-index: 10;
}

.info-box::after {
  content: "";
  position: absolute;
  width: 10px;
  height: 10px;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  border: 0.5rem solid transparent;
  border-bottom-color: var(--major-color--light);
  z-index: -2;
}

.info-box {
  position: absolute;
  top: calc(100% + 0.5rem);
  left: 50%;
  font-size: 1.6rem;
  transform: translateX(-50%);
  background-color: var(--major-color--light);
  color: var(--font-color);
  border-radius: 0.2rem;
  padding: 1rem;
  width: max-content;
  z-index: 1;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  box-shadow: 0 0 1rem 0.2rem rgba(0, 0, 0, 0.8);
}

.icon {
  width: 20px;
  transition: color 0.1s;
}

.info:hover {
  color: var(--font-color--dark);
}
</style>
