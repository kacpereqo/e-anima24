<template>
  <div class="container">
    <div class="sidebar">
      <ul>
        <li>
          <div class="add">
            <NuxtLink to="/create">
              <Icon class="icon" name="material-symbols:add-rounded" />
              <span> DODAJ </span>
            </NuxtLink>
          </div>
        </li>
        <li>
          <div class="button">
            <span>test</span>
          </div>
        </li>
        <li>
          <div class="button">test</div>
        </li>
        <li>
          <div class="button">test</div>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.sidebar {
  position: fixed;
  background-color: var(--second-color);
  width: 200px;
  height: 100vh;
  top: var(--navbar-height);
  left: 0;
  z-index: 100;
  transition: 0.5s;
  overflow-y: auto;
}

.container {
  height: 100vh;
}

.add a {
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 1rem;
  height: 4rem;
  font-size: 1.6rem;
  border-radius: 0.3rem;
  cursor: pointer;
  position: relative;
  color: var(--accent-color-dark);
  border: 4px solid var(--accent-color);
}
.add .icon {
  left: 1rem;
  position: absolute;
  color: var(--accent-color);
}

.button {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 1rem;
  font-size: 1.6rem;
  border-radius: 0.3rem;
  cursor: pointer;
  color: var(--accent-color-dark);
}
</style>
