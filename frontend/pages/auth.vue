<template>
  <div class="auth-page">
    <div class="auth">
      <NuxtPage />
    </div>
    <div class="baner">
      <img src="@/assets/featured.jpg" />
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style>
.error {
  color: var(--error-color);
}

.auth-page {
  display: flex;
  flex: 1;
  justify-content: space-between;
}

.auth-page div {
  flex: 1;
}

.auth {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  z-index: 1;
  box-shadow: 0 0 10rem 15rem var(--major-color);
}

form {
  display: flex;
  flex-direction: column;
  width: 50%;
  gap: 2rem;
  padding: 2rem;
  background-color: var(--second-color);
}

.inputs {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.row {
  position: relative;
  display: flex;
  gap: 0.5rem;
  flex-direction: column;
}

.more {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
}

.more .button {
  padding: 2rem;
  background-color: var(--major-color);
}

.more .button:hover {
  background-color: var(--major-color--light);
  transition: 0.1s;
}

.sign-in:hover {
  background-color: var(--accent-color--opacity);
  transition: 0.1s;
}

input {
  padding: 1rem;
  border: none;
  border-radius: 0.5rem;
  background-color: var(--major-color);
  width: 100%;
  color: var(--font-color);
  font-size: var(--font-size-3);
}

.button {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  height: 4rem;
  border: none;
  border-radius: 0.5rem;
  background-color: var(--accent-color);
  color: var(--font-color);
  font-size: var(--font-size-3);
  cursor: pointer;
}

.baner {
  position: relative;
  z-index: 0;
}

.baner img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
