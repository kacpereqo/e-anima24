export default defineNuxtConfig({
  nitro: {
    compressPublicAssets: true,
  },
  devtools: { enabled: true },
    modules: [
      '@nuxt/image',
      "nuxt-icon",
      "@pinia/nuxt",
      '@vueuse/nuxt',
      '@pinia-plugin-persistedstate/nuxt',
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
    runtimeConfig: {
      public: {
        API_URL:                    process.env.API_URL,
        GOOGLE_OAUTH_CLIENT_ID:     process.env.GOOGLE_OAUTH_CLIENT_ID,
        GOOGLE_OAUTH_CLIENT_SECRET: process.env.GOOGLE_OAUTH_CLIENT_SECRET,
        GOOGLE_OAUTH_REDIRECT:      process.env.GOOGLE_OAUTH_REDIRECT,
      },
    },
})
