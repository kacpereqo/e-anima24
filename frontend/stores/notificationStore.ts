import { defineStore } from 'pinia'

interface Notification {
    message: string;
    title: string;
    type: "info" | "success" | "warning" | "error";
}

export enum NotificationType {
    succesfulLogin = "succesfulLogin",
    succesfulLogout = "succesfulLogout",
}

export const useNotificationStore = defineStore('notfications', () => {
    const notifications = ref<Notification[]>([])

    function addNotification(notification: string) {
        switch (notification) {
            case NotificationType.succesfulLogin:
                notifications.value.push({
                    message: "Zostałeś pomyślnie zalogowany",
                    title: "Zalogowano",
                    type: "success",
                })
                break;
            case NotificationType.succesfulLogout:
                notifications.value.push({
                    message: "Zostałeś pomyślnie wylogowany",
                    title: "Wylogowano",
                    type: "success",
                })
                break;
    }}

    function removeNotification(idx: number) {
        notifications.value.splice(idx, 1)
    }

    return { notifications, addNotification, removeNotification}
  })