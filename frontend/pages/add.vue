<template>
  <div class="add-page">
    <div class="steps" ref="progress">
      <div
        class="step"
        :class="{ active: currentStep >= idx }"
        v-for="idx in [0, 1, 2, 3, 4]"
        :key="idx"
      ></div>
    </div>
    <div class="add-form">
      <div class="form">
        <component :is="steps[currentStep]" />
      </div>
      <div class="buttons">
        <button
          :disabled="currentStep === 0"
          @click="currentStep--"
          class="prev"
        >
          <Icon name="material-symbols:arrow-back-rounded" />
          <span>Wróć</span>
        </button>
        <button
          :disabled="currentStep === steps.length - 1"
          @click="currentStep++"
          class="next"
        >
          <span>Dalej</span>
          <Icon name="material-symbols:arrow-forward-rounded" />
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const currentStep = ref(0);
const steps = [
  defineAsyncComponent(() => import("../components/steps/Step1.vue")),
  defineAsyncComponent(() => import("../components/steps/Step2.vue")),
  defineAsyncComponent(() => import("../components/steps/Step3.vue")),
  defineAsyncComponent(() => import("../components/steps/Step4.vue")),
  defineAsyncComponent(() => import("../components/steps/Step5.vue")),
];

const progress = ref<HTMLElement | null>(null);
</script>

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

.form {
  flex: 1;
}
.steps {
  display: flex;
  justify-content: space-between;
  width: 50%;
  gap: 2rem;
}

.buttons {
  display: flex;
  justify-content: space-between;
  gap: 2rem;
  padding: 2rem;
  width: 100%;
}

.buttons button {
  width: 30%;
  padding: 0.5rem;
  border-radius: 0.5rem;
  border: none;
  background-color: var(--accent-color);
  color: var(--font-color);
  font-size: var(--font-size-3);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.buttons button:disabled,
.buttons button:disabled:hover {
  background-color: var(--accent-color--dark);
  color: var(--font-color);
  cursor: not-allowed;
}

.buttons button:hover {
  background-color: var(--accent-color--opacity);
}

.buttons button .icon {
  height: 18px;
}

.steps .active {
  background-color: var(--accent-color);
}

.step {
  border-radius: 1rem;
  flex: 1;
  height: 1rem;
  background-color: var(--major-color--light);
}

.add-form {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color: var(--second-color);
  width: 50%;
  height: 20rem;
}
</style>
