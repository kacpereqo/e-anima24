<template>
  <form>
    <h2>Rejestracja</h2>
    <input type="text" placeholder="Nazwa użytkownika" />
    <input type="text" placeholder="E-mail" />
    <input type="password" placeholder="Hasło" />
    <input type="password" placeholder="Powtórz hasło" />

    <button type="submit" class="sign-in">Zarejestruj się!</button>

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
