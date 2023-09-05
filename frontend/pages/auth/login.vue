<template>
  <form @submit.prevent="submit" ref="form">
    <h2>Logowanie</h2>
    <div class="inputs">
      <div class="row">
        <label for="username">Login lub E-mail</label>
        <input type="text" name="username" v-model="username" />
      </div>
      <div class="row">
        <label for="password">Hasło</label>
        <input type="password" name="password" v-model="password" />
      </div>

      <div class="row">
        <ul>
          <li v-if="error" class="error">{{ error }}</li>
        </ul>
      </div>
    </div>
    <button type="submit" class="sign-in button" ref="form">
      Zaloguj się!
    </button>

    <div class="more">
      <a :href="googleAuthUrl" class="button">
        <Icon name="logos:google-icon" />
      </a>
      <a class="button">
        <Icon name="logos:facebook" />
      </a>
    </div>
    <div class="register">
      Nie masz konta? <NuxtLink to="/auth/register">Zarejestruj się!</NuxtLink>
    </div>
  </form>
</template>

<script setup lang="ts">
import { useUserStore } from "@/stores/userStore";
import {
  NotificationType,
  useNotificationStore,
} from "@/stores/notificationStore";

const ENV = useRuntimeConfig().public;
const API_URL = ENV.API_URL;
const router = useRouter();

const username = ref("");
const password = ref("");
const error = ref();
const form = ref<any>(null);

const googleAuthUrl = computed(() => {
  const params = new URLSearchParams({
    client_id: ENV.GOOGLE_OAUTH_CLIENT_ID,
    redirect_uri: "http://localhost:3000/auth/callback/google",
    response_type: "code",
    scope: [
      "https://www.googleapis.com/auth/userinfo.profile",
      "https://www.googleapis.com/auth/userinfo.email",
      "openid",
    ].join(" "),
    access_type: "offline",
    prompt: "consent",
  });

  return `https://accounts.google.com/o/oauth2/v2/auth?${params.toString()}`;
});

async function submit() {
  form.value.elements.username.classList.remove("inputError");
  form.value.elements.password.classList.remove("inputError");

  await fetch(`${API_URL}/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username: username.value,
      verifier: password.value,
    }),
  }).then((res) => {
    if (res.status === 200) {
      res.json().then((data) => {
        const token = useCookie("token", {
          watch: true,
          maxAge: 60 * 60 * 24 * 30,
        });

        token.value = data.access_token;

        const userStore = useUserStore();
        userStore.userId = data.user.userId;
        userStore.username = data.user.username;
        userStore.email = data.user.email;
        userStore.avatarUrl = data.user.avatar;

        const notificationStore = useNotificationStore();
        notificationStore.addNotification(NotificationType.succesfulLogin);

        router.push("/");
      });
    } else {
      error.value = "Nieprawidłowy login lub hasło";
      form.value.elements.username.classList.add("inputError");
      form.value.elements.password.classList.add("inputError");
    }
  });
}
</script>

<style scoped>
.error {
  color: var(--error-color);
  padding: 0;
  margin-left: 1rem;
}
.register {
  margin-top: 1rem;
  text-align: center;
}

.register a {
  color: var(--accent-color);
}

.inputError {
  outline: 2px solid var(--error-color);
}
</style>
