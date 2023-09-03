<template>
  <div class="notifications">
    <Notification
      v-for="(notification, idx) in notificationStore.notifications"
      :key="idx"
      :notification="notification"
      :startAnimation="idx === 0"
      @close="notificationStore.removeNotification(idx)"
    />
  </div>
</template>

<script setup lang="ts">
import { useNotificationStore } from "@/stores/notificationStore";

const notificationStore = useNotificationStore();
</script>

<style scoped>
.notifications {
  display: flex;
  flex-direction: column;
  position: fixed;
  right: 2rem;
  bottom: 2rem;
  z-index: 1000;
}
</style>
