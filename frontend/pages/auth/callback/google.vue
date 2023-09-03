<template>
  <LoadingIndicator />
</template>

<script setup lang="ts">
import { useUserStore } from "@/stores/userStore";
import {
  NotificationType,
  useNotificationStore,
} from "@/stores/notificationStore";

const route = useRoute();
const router = useRouter();
const ENV = useRuntimeConfig().public;
const API_URL = ENV.API_URL;

onMounted(async () => {
  if (!route.query.code) {
    return;
  }
  await $fetch(
    API_URL + "/auth/google/auth?" + new URLSearchParams(route.query as any),
    {
      onResponse: (res) => {
        const token = useCookie("token", {
          watch: true,
          maxAge: 60 * 60 * 24 * 30,
        });
        token.value = res.response._data.access_token;

        const userStore = useUserStore();
        userStore.userId = res.response._data.user.userId;
        userStore.username = res.response._data.user.username;
        userStore.email = res.response._data.user.email;
        userStore.avatarUrl = res.response._data.user.avatar;

        const notificationStore = useNotificationStore();
        notificationStore.addNotification(NotificationType.succesfulLogin);

        router.push("/");
      },
    }
  );
});
</script>
