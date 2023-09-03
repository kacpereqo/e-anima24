<template>
  <form @submit.prevent="submit">
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
    </div>
    <div class="error" v-if="error">{{ error.data.detail }}</div>
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
  </form>
</template>

<script setup lang="ts">
const ENV = useRuntimeConfig().public;
const API_URL = ENV.API_URL;
const router = useRouter();

const username = ref("");
const password = ref("");
const data = ref();
const error = ref();

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
  const { error: newError } = await useFetch(API_URL + "/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    },
    body: new URLSearchParams({
      username: username.value,
      password: password.value,
    }),
    // onResponse: (res) => {
    //   const token = useCookie("token", {
    //     watch: true,
    //     maxAge: 60 * 60 * 24 * 30,
    //   });
    //   token.value = res.response._data.access_token;

    //   router.push("/");
    // },
    // onResponseError: (res) => {
    //   console.log(res);
    // },
  });
  error.value = newError.value;
  // data.value = res;
  // error.value = res.value;
}
</script>
