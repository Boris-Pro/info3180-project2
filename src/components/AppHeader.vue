<template>
  <header v-if="dataLoaded">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <div class="container-fluid">
        <i class="fas fa-camera-retro mr-2"></i>
        <a class="navbar-brand" href="/">Photogram</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent"> 
          <ul class="navbar-nav">
            <li class="nav-item">
              <RouterLink to="/" class="nav-link active">Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/explore">Explore</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="'/users/' + current_user_id">My Profile</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink @click="logout" class="nav-link" to="/logout">Logout</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
  <div class="alert" id="alert"></div>
</template>

<script setup>
import { RouterLink } from "vue-router";
import { ref, onMounted } from "vue";
import router from "../router/index";
import { getCsrfToken, getUserId } from "../assets/helper";

let csrf_token = ref("");
let logged_in = ref("");
let current_user_id = ref("");
let dataLoaded = ref(false);

onMounted(async () => {
  let token = await getCsrfToken();
  csrf_token.value = token.csrf_token;

  let user_id = await getUserId();
  current_user_id.value = user_id.id;
  logged_in.value = user_id.logged_in;
  dataLoaded.value = true;
});

const logout = () => {
  router.push('/logout');
};
</script>

<style scoped>
/* Add any component specific styles here */
</style>
