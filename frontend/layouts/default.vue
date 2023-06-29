<template>
  <div class="default-layout">
    <TheNavbar />
    <slot />
  </div>
</template>

<style scoped>
.default-layout {
  display: flex;
  flex-direction: column;
}
</style>
