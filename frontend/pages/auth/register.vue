<template>
  <form @submit.prevent="submit" ref="form">
    <h2>Rejestracja</h2>
    <div class="inputs">
      <div class="row">
        <label for="username">Nazwa użytkownika</label>
        <input type="text" name="username" v-model="formData.username" />
      </div>
      <div class="row">
        <label for="email">E-mail</label>
        <input type="email" name="email" v-model="formData.email" />
      </div>
      <div class="row">
        <label for="password">Hasło</label>
        <div class="password-input">
          <Icon
            v-show="formData.password"
            :name="
              formData.showPassword
                ? 'heroicons-solid:eye'
                : 'heroicons-solid:eye-off'
            "
            class="icon"
            @click="formData.showPassword = !formData.showPassword"
          />

          <input
            :type="formData.showPassword ? 'text' : 'password'"
            name="password"
            v-model="formData.password"
          />
        </div>
      </div>
      <div class="row">
        <label for="repeatPassword">Powtórz hasło</label>
        <div class="password-input">
          <Icon
            v-show="formData.repeatPassword"
            :name="
              formData.showPassword
                ? 'heroicons-solid:eye'
                : 'heroicons-solid:eye-off'
            "
            class="icon"
            @click="formData.showPassword = !formData.showPassword"
          />

          <input
            :type="formData.showPassword ? 'text' : 'password'"
            name="repeatPassword"
            v-model="formData.repeatPassword"
          />
        </div>
      </div>

      <div class="row">
        <ul class="error">
          <li v-for="(error, idx) in errors" :key="idx">
            {{ error.data.error }}
          </li>
        </ul>
      </div>
    </div>
    <button type="submit" class="sign-in button" ref="form">
      Zarejestruj się
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
import { useUserStore } from "@/stores/userStore";
import {
  NotificationType,
  useNotificationStore,
} from "@/stores/notificationStore";

const ENV = useRuntimeConfig().public;
const API_URL = ENV.API_URL;
const router = useRouter();

interface registerError {
  data: {
    elementName: string;
    error: string;
  };
}

const data = ref();
const errors = ref<registerError[]>([]);
const form = ref<any>(null);
const formData = ref({
  username: "kacperek",
  password: "aaaaaaaaaaaaaaaaaaa",
  repeatPassword: "aaaaaaaaaaaaaaaaaaa",
  email: "a@a.com",
  showPassword: false,
});

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

function check() {
  // Username

  if (formData.value.username === "") {
    errors.value.push({
      data: {
        elementName: "username",
        error: "Nazwa użytkownika nie może być pusta",
      },
    });
  }

  // Email

  if (formData.value.email === "") {
    errors.value.push({
      data: {
        elementName: "email",
        error: "E-mail nie może być pusty",
      },
    });
  } else {
    const emailRegex = new RegExp(
      "^[a-zA-Z0-9._:$!%-]+@[a-zA-Z0-9.-]+.[a-zA-Z]$"
    );
    if (!emailRegex.test(formData.value.email)) {
      errors.value.push({
        data: {
          elementName: "email",
          error: "E-mail jest niepoprawny",
        },
      });
    }
  }

  // Password

  if (formData.value.password === "") {
    errors.value.push({
      data: {
        elementName: "password",
        error: "Hasło nie może być puste",
      },
    });
  } else if (formData.value.password.length < 8) {
    errors.value.push({
      data: {
        elementName: "password",
        error: "Hasło musi mieć co najmniej 8 znaków",
      },
    });
  } else if (formData.value.password !== formData.value.repeatPassword) {
    errors.value.push({
      data: {
        elementName: "repeatPassword",
        error: "Hasła muszą być takie same",
      },
    });
  }
}

function showErrors() {
  for (const input of form.value.elements) {
    input.classList.remove("inputError");
    for (const error of errors.value) {
      if (input.name === error.data.elementName) {
        input.classList.add("inputError");
      }
    }
  }
}

function submit() {
  errors.value = [];
  check();
  showErrors();

  if (errors.value.length > 0) {
    return;
  }

  fetch(`${API_URL}/auth/register`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username: formData.value.username,
      email: formData.value.email,
      provider: "auth",
      verifier: formData.value.password,
    }),
  }).then((res) => {
    if (res.status === 200) {
      console.log("Registered");
      res.json().then((data) => {
        const token = useCookie("token", {
          sameSite: "lax",
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
        notificationStore.addNotification(NotificationType.succesfulRegister);

        router.push("/");
      });
    } else {
      res.json().then((data) => {
        errors.value.push(data.detail);
        showErrors();
      });
    }
  });
}
</script>

<style scoped>
.password-hint {
  list-style: none;
  position: absolute;
  bottom: calc(100%);
  right: 50%;
  transform: translateX(50%);
  background-color: var(--second-color);
  color: var(--major-color-text);
  border-radius: 0.5rem;
  border: 2px solid var(--accent-color);
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 1);
  z-index: 1000;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.password-hint::after {
  content: "";
  position: absolute;
  top: 100%;
  right: 50%;
  transform: translateX(50%);
  border: 1rem solid transparent;
  border-top-color: var(--accent-color);
}

.password-input {
  position: relative;
}

.password-input .icon {
  position: absolute;
  top: 50%;
  right: 1rem;
  transform: translateY(-50%);
  cursor: pointer;
}
.inputError {
  outline: 2px solid var(--error-color);
}
.error {
  color: var(--error-color);
  padding: 0;
  margin-left: 1rem;
}
</style>
