<template>
  <div class="default-layout">
    <TheNavbar />
    <div class="slot">
      <slot />
    </div>
  </div>
</template>

<style>
.default-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.slot {
  display: flex;
  flex: 1;
}
</style>
