import { defineStore } from 'pinia'

export const useAuthStore= defineStore('auth', () => {
    const accessToken = ref<string>('')
  
    const is_logged = computed(() => accessToken.value !== '')

    return { accessToken, is_logged }
  })