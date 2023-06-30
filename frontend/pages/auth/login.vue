<template>
  <form>
    <h2>Logowanie</h2>
    <input type="text" placeholder="Nazwa użytkownika lub E-mail" />
    <input type="password" placeholder="Hasło" />

    <button type="submit" class="sign-in">Zaloguj się!</button>

    <div class="more">
      <button type="submit" class="google">
        <Icon name="logos:google-icon" />
      </button>
      <button type="submit" class="Facebook">
        <Icon name="logos:facebook" />
      </button>
    </div>
  </form>
</template>
