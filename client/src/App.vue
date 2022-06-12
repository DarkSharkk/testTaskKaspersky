<template>
  <div id="app">
    <nav>
      <router-link to="/">Домашняя</router-link> |
      <router-link to="/users">Пользователи</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #dddddd;
}

nav {
  margin-bottom: 15px;
  padding: 5px;
  background-color: blueviolet;
}

nav a {
  font-size: 20px;
  font-weight: bold;
  text-decoration: none;
  color: white;
}

nav a:hover {
  color: yellow;
}

nav a.router-link-exact-active {
  color: white;
  text-decoration: underline 0.28rem;
}

html {
  background-color: #dddddd;
}
</style>
