<script setup>
import { ref } from "vue";

let message = ref("Hello World! This is a VueJS and Flask Starter Template.")

</script>

<template>
    <div class="container mt-5">
  <div class="row">
    <div class="col-md-6">
      <div class="card custom-card">
        <img src="https://via.placeholder.com/300" class="card-img-top" alt="Image">
      </div>
    </div>
    <div class="col-md-6">
      <div class="card custom-card">
        <div class="card-body">
          <h5 class="card-title">Photogram</h5>
          <hr>
          <p class="card-text">Share photos of your favourite moments with friends, family and the world.</p>
          <div class="row">
            <div class="col-md-6">
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
      border-radius: 15px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
.card-img-top {
  height: 100%;
  object-fit: cover;
    }
.btn-width{
  width: 100%;
}
</style>