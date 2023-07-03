<template>
  <div id="app">
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script setup lang="ts">
onMounted(() => {
  window.addEventListener(
    "keydown",
    function (e: any) {
      if (
        e.keyIdentifier == "U+000A" ||
        e.keyIdentifier == "Enter" ||
        e.keyCode == 13
      ) {
        e.preventDefault();
        return false;
      }
    },
    true
  );
});
</script>

<style>
@import url("assets/variables.css");
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@300;500&display=swap");
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 62.5%;
}

#app {
  overflow-x: hidden;
  font-family: "Inter", sans-serif;
  color: var(--font-color);
  font-size: var(--font-size-2);
  min-height: 100vh;
  width: 100%;
  background-color: var(--major-color);
}
</style>
