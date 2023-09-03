<template>
  <form @submit.prevent="submit">
    <h2>Rejestracja</h2>
    <div class="inputs">
      <div class="row">
        <label for="username">Nazwa użytkownika</label>
        <input type="text" name="username" v-model="username" />
      </div>
      <div class="row">
        <label for="email">E-mail</label>
        <input type="email" name="email" v-model="email" />
      </div>
      <div class="row">
        <label for="password">Hasło</label>
        <div class="password-input">
          <Icon
            v-show="password"
            :name="
              showPassword ? 'heroicons-solid:eye' : 'heroicons-solid:eye-off'
            "
            class="icon"
            @click="showPassword = !showPassword"
          />

          <input
            @focus="showPasswordHint = true"
            @blur="showPasswordHint = false"
            :type="showPassword ? 'text' : 'password'"
            name="password"
            v-model="password"
            @input="validatePasswordStrength"
          />
        </div>
        <ul v-show="showPasswordHint" class="password-hint">
          <li>
            <Icon
              :style="
                passwordNeedings.length
                  ? 'color: var(--accent-color)'
                  : 'color: var(--error-color)'
              "
              :name="
                passwordNeedings.length
                  ? 'heroicons-solid:check'
                  : 'heroicons-solid:x'
              "
            />8 znaków
          </li>
          <li>
            <Icon
              :style="
                passwordNeedings.lowercase
                  ? 'color: var(--accent-color)'
                  : 'color: var(--error-color)'
              "
              :name="
                passwordNeedings.lowercase
                  ? 'heroicons-solid:check'
                  : 'heroicons-solid:x'
              "
            />Mała litera
          </li>
          <li>
            <Icon
              :style="
                passwordNeedings.uppercase
                  ? 'color: var(--accent-color)'
                  : 'color: var(--error-color)'
              "
              :name="
                passwordNeedings.uppercase
                  ? 'heroicons-solid:check'
                  : 'heroicons-solid:x'
              "
            />Duża litera
          </li>
          <li>
            <Icon
              :style="
                passwordNeedings.number
                  ? 'color: var(--accent-color)'
                  : 'color: var(--error-color)'
              "
              :name="
                passwordNeedings.number
                  ? 'heroicons-solid:check'
                  : 'heroicons-solid:x'
              "
            />Cyfra
          </li>
          <li>
            <Icon
              :style="
                passwordNeedings.special
                  ? 'color: var(--accent-color)'
                  : 'color: var(--error-color)'
              "
              :name="
                passwordNeedings.special
                  ? 'heroicons-solid:check'
                  : 'heroicons-solid:x'
              "
            />Znak specjalny
          </li>
        </ul>
      </div>
      <div class="row">
        <label for="repeatPassword">Powtórz hasło</label>
        <div class="password-input">
          <Icon
            v-show="repeatPassword"
            :name="
              showRepeatPassword
                ? 'heroicons-solid:eye'
                : 'heroicons-solid:eye-off'
            "
            class="icon"
            @click="showRepeatPassword = !showRepeatPassword"
          />

          <input
            :type="showRepeatPassword ? 'text' : 'password'"
            name="repeatPassword"
            v-model="repeatPassword"
          />
        </div>
      </div>
    </div>
    <div class="error" v-if="error">{{ error.data.detail }}</div>
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
const ENV = useRuntimeConfig().public;
const API_URL = ENV.API_URL;
const router = useRouter();

function validatePasswordStrength() {
  if (password.value.length >= 8) {
    passwordNeedings.length = true;
  } else {
    passwordNeedings.length = false;
  }

  if (/[a-z]/.test(password.value)) {
    passwordNeedings.lowercase = true;
  } else {
    passwordNeedings.lowercase = false;
  }

  if (/[A-Z]/.test(password.value)) {
    passwordNeedings.uppercase = true;
  } else {
    passwordNeedings.uppercase = false;
  }

  if (/[0-9]/.test(password.value)) {
    passwordNeedings.number = true;
  } else {
    passwordNeedings.number = false;
  }

  if (/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password.value)) {
    passwordNeedings.special = true;
  } else {
    passwordNeedings.special = false;
  }
}

const passwordNeedings = {
  length: false,
  lowercase: false,
  uppercase: false,
  number: false,
  special: false,
};

const username = ref("");
const password = ref("");
const repeatPassword = ref("");
const data = ref();
const error = ref();
const email = ref("");
const showPasswordHint = ref(false);
const showPassword = ref(false);
const showRepeatPassword = ref(false);
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

function submit() {}
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
</style>
