export default defineNuxtRouteMiddleware(({ store, route, redirect }) => {
    if (!store.auth.loggedIn) {
        return redirect('/login')
    }
    else if (route.path.includes('/auth')) {
        return redirect('/')
    }
    else {
        return
    }
})