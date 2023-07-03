import { defineStore } from 'pinia'

export const useAddAnimeFormStore = defineStore('addAnimeForm', () => {
    const title            = ref<string>('')
    const description      = ref<string>('')
    const shortDescription = ref<string>('')
    
    const series           = ref<string>('')
    const season           = ref<number>()
    const episode          = ref<number>()

    const tags             = ref<string[]>([])
    const genres           = ref<string[]>([])
  
    return { title, description, series, shortDescription, season, episode, tags, genres}
  })