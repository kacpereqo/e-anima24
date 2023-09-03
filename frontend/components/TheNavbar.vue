<template>
  <nav id="navbar">
    <div class="logo">
      <img src="@/assets/logo.png" />
      <h1>e-anima24</h1>
    </div>

    <div>
      <ul class="routes">
        <li>
          <router-link to="/">Home</router-link>
        </li>
        <li>
          <router-link to="#">Anime</router-link>
        </li>
        <li>
          <router-link to="#">Manga</router-link>
        </li>
      </ul>
    </div>

    <div class="user">
      <div v-if="!userStore.isLogged" class="not-loggedin">
        <a href="/auth/login" class="login">Zaloguj</a>
        <a href="/auth/register" class="register">Zarejestruj</a>
      </div>
      <div class="loggedin" v-else>
        <div class="avatar">
          <div v-show="userStore.avatarUrl === null" class="loading" />
          <img
            v-show="userStore.avatarUrl !== null"
            :src="userStore.avatarUrl!"
            ref="avatar"
            referrerpolicy="no-referrer"
          />
        </div>
        <Icon
          @click="showDropdown = !showDropdown"
          name="material-symbols:keyboard-arrow-down-rounded"
          class="icon"
          @mouseenter="showDropdown = true"
          @mouseleave="showDropdown = false"
        />
        <ul
          v-if="debounced"
          class="dropdown"
          @mouseenter="showDropdown = true"
          @mouseleave="showDropdown = false"
        >
          <li>
            <router-link to="">
              <Icon name="material-symbols:person-2-rounded" />
              <span> Profil </span>
            </router-link>
          </li>
          <li>
            <router-link to="">
              <Icon name="material-symbols:space-dashboard-rounded" />
              <span> Panel </span>
            </router-link>
          </li>
          <li>
            <router-link to="">
              <Icon name="material-symbols:settings-outline-rounded" />
              <span> Ustawienia </span>
            </router-link>
          </li>
          <li>
            <router-link to="" @click="userStore.logout">
              <Icon name="material-symbols:logout-rounded" />
              <span> Wyloguj </span>
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { useUserStore } from "@/stores/userStore";
import { gsap } from "gsap";

const avatar = ref<HTMLImageElement | null>(null);
const userStore = useUserStore();
const showDropdown = ref(false);
const debounced = refDebounced(showDropdown, 100);

onMounted(() => {
  if (avatar.value !== null) {
    avatar.value.src = userStore.avatarUrl!;
  }

  const dropdownIcon = document.querySelector(".icon");

  watch(debounced, (value) => {
    if (value) {
      gsap.to(dropdownIcon, { rotation: 180, duration: 0.5 });
    } else {
      gsap.to(dropdownIcon, { rotation: 360, duration: 0.5 });
    }
  });
});
</script>

<style scoped>
#navbar {
  height: var(--navbar-height);
  width: 100%;
  background-color: var(--second-color);
  font-size: var(--font-size-3);
  display: flex;
  padding: 0 1rem;
  justify-content: space-between;
  position: relative;
  align-items: center;
  z-index: 1000;
}

.routes {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  list-style: none;
  gap: 0.5rem;
}

.dropdown {
  display: flex;
  flex-direction: column;
  position: absolute;
  top: 100%;
  right: 0;
  border-radius: 0 0 0.5rem 0.5rem;
  overflow: hidden;
  box-shadow: 0 0 1rem rgba(0, 0, 0, 0.2);
}

.dropdown li {
  user-select: none;
  list-style: none;
  padding: 1.5rem;
  font-size: var(--font-size-3);
  background-color: var(--second-color);
}

.dropdown li:hover {
  transition: 0.1s;
  background-color: var(--accent-color--opacity);
}

.dropdown li a {
  display: flex;
  align-items: center;
  gap: 1rem;
  text-decoration: none;
  color: var(--text-color);
}

.logo {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  gap: 1rem;
}

.logo img {
  height: 100%;
}

.not-loggedin {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
}
.login,
.register {
  background-color: var(--third-color);
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  color: var(--text-color);
  text-decoration: none;
  transition: 0.1s;
}

.login {
  background-color: var(--accent-color);
}
.login:hover {
  background-color: var(--accent-color--opacity);
}

.register:hover {
  background-color: var(--major-color--light);
}
.avatar img {
  padding: 1rem 1rem;
  height: 100%;
  aspect-ratio: 1/1;
  border-radius: 2rem;
}

.avatar .loading {
  animation: pulse 1s ease-in-out infinite;
  height: calc(100% - 2rem);
  aspect-ratio: 1/1;
  border-radius: 1rem;
}

@keyframes pulse {
  0% {
    background-color: var(--major-color);
  }
  50% {
    background-color: var(--major-color--light);
  }
  100% {
    background-color: var(--second-color);
  }
}

.avatar {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.loggedin {
  height: 100%;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
}

.icon {
  padding: 0.5rem;
  box-sizing: content-box;
}
.icon:hover {
  color: var(--accent-color);
}

.user {
  height: 100%;
  display: flex;
  position: relative;
  justify-content: center;
  align-items: center;
}

li {
  height: 100%;
}

.routes a {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  padding: 1rem;
  text-decoration: none;
  color: var(--text-color);
  transition: 0.1s;
}
.routes a:hover {
  color: var(--accent-color);
  text-decoration: underline;
}
</style>
