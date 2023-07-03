// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
    modules: [
      '@nuxt/image',
      "nuxt-icon",
      "@pinia/nuxt",
      '@vueuse/nuxt',
    ],
    components: [

      {
        path: "~/components/steps",
      },
      {
        path: "~/components/common",
      },
      "~/components",
    ],
})
