import { defineStore } from 'pinia'
import { useNotificationStore, NotificationType } from './notificationStore'

type Role = 'admin' | 'user'

export const useUserStore = defineStore('user', () => {
    const notificationStore = useNotificationStore()

    const username = ref<string | null>(null)
    const userId = ref<number | null>(null)
    const email = ref<string | null>(null)
    const role = ref<Role | null>(null)
    const avatarUrl = ref<string | null>(null)

    const accessToken = useCookie('token')
    const isLogged = computed(() => {accessToken.value !== ''; console.log(accessToken.value)})

    function logout() { 
      $reset();
      localStorage.removeItem('user');
      notificationStore.addNotification(NotificationType.succesfulLogout)
  } 

     function $reset() {
        username.value = null
        userId.value = null
        email.value = null
        role.value = null
        avatarUrl.value = null
        accessToken.value = ''
    }

    return { username, userId, email, role, isLogged, accessToken, avatarUrl,  logout }
  }, {
    persist: {
      storage : persistedState.localStorage,
    }
  })