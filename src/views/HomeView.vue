<script setup>
import { ref } from "vue";

let message = ref("Hello World! This is a VueJS and Flask Starter Template.")

</script>

<template>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <div class="container mt-5">
  <div class="row">
    <div class="col-md-6">
      <div class="card custom-card">
        <img src="\src\assets\photo_h.png" class="card-img-top" alt="Image">
      </div>
    </div>
    <div class="col-md-6">
      <div class="card custom-card">
        <div class="card-body">
          <h5 class="card-title"><i class="fas fa-camera-retro mr-2"></i>Photogram</h5>
          <hr>
          <p class="card-text">Share photos of your favourite moments with friends, family and the world.</p>
          <div class="row element">
            <div class="col-md-6 ">
              <router-link to="/register" class="btn btn-success btn-block mb-2 btn-width">Register</router-link>
            </div>
            <div class="col-md-6">
              <router-link to="/login" class="btn btn-primary btn-block btn-width">Login</router-link>
            </div>
          </div>
          
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<style>
/* Add any component specific styles here */
.custom-card {
      border-radius: 10px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      height: 400px;
    }
.card-img-top {
  height: 100%;
  border-radius: 10px;
  object-fit: cover;
    }
.btn-width{
  width: 100%;
}
.element {
    margin-top: 150px; /* Adjust the value as needed */
}
.card-title {
    text-align: center;
}
</style>