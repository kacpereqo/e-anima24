<template>
  <div class="add-page">
    <div class="steps">
      <div class="step"></div>
      <div class="step"></div>
      <div class="step"></div>
      <div class="step"></div>
      <div class="step"></div>
    </div>
    <div class="add-form"></div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.add-page {
  position: absolute;
  top: 10rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  gap: 2rem;
}

.steps {
  display: flex;
  justify-content: space-between;
  width: 50%;
  gap: 2rem;
}

.step {
  flex: 1;
  height: 1rem;
  background-color: var(--accent-color);
}

.add-form {
  background-color: var(--second-color);
  width: 50%;
  height: 20rem;
}
</style>
