<template>
  <form @submit.prevent="submit">
    <h2>Logowanie</h2>
    <input
      type="text"
      placeholder="Nazwa użytkownika lub E-mail"
      v-model="username"
    />
    <input type="password" placeholder="Hasło" v-model="password" />

    <button type="submit" class="sign-in" ref="form">Zaloguj się!</button>

    <div class="more">
      <button type="submit" class="google">
        <Icon name="logos:google-icon" />
      </button>
      <button type="submit" class="Facebook">
        <Icon name="logos:facebook" />
      </button>
    </div>
  </form>
</template>

<script setup lang="ts">
import { useAuthStore } from "@/stores/authStore";

const ENV = useRuntimeConfig().public;
const API_URL = ENV.API_URL;
const router = useRouter();

const username = ref("");
const password = ref("");

async function submit() {
  const res = await useFetch(API_URL + "/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    },
    body: new URLSearchParams({
      username: username.value,
      password: password.value,
    }),
    onResponse: (res) => {
      const token = useCookie("token", { sameSite: "strict" });
      const store = useAuthStore();

      store.accessToken = res.response._data.access_token;
      token.value = res.response._data.access_token;

      router.push("/");
    },
  });
}
</script>
