// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
    modules: [
      '@nuxt/image',
      "nuxt-icon",
      "@pinia/nuxt"
    ],
    components: [

      {
        path: "~/components/steps",
      },
      "~/components",
    ],
})
