import { defineStore } from 'pinia'

export const useAddAnimeFormStore = defineStore('addAnimeForm', () => {
    const title = ref('')
    const description = ref('')
  
    return { title, description }
  })