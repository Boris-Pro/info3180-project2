<template>
    <div class="container mt-5">
        <div class="row justify-content-center">
          <div class="col-md-6">
            <h1>Login</h1>
            <div class="card">
              <div class="card-body" id="alert">
                <form v-if="dataLoaded" @submit.prevent="loginUser" enctype="multipart/form-data" id="loginForm">
                  <div class="form-group">
                    <label for="username">Username</label>
                    <input type="text" class="form-control" name="username"  id="username">
                  </div>
                  <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" class="form-control" name="password" v-model = "password" id="password">
                  </div>
                  <button type="submit" class="btn btn-success btn-width">Login</button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </template>
    
    <script setup>
    import { ref, onMounted } from "vue";
    import router from "../router/index";
    import {getCsrfToken} from "../assets/helper";

    let csrf_token = ref("");

    let dataLoaded = ref(false);
    let isAuthenticated = ref(false);

    onMounted(async () => {
        let token = await getCsrfToken();
        csrf_token.value = token.csrf_token;

        dataLoaded.value = true;
    });


    let loginUser = () => {
        const alert = document.querySelector("#alert");

        let loginForm = document.querySelector('#loginForm');
        let form_data = new FormData(loginForm);
        fetch("/api/v1/auth/login", {
            method: 'POST',
            body: form_data,
            headers: {
                'X-CSRFToken': csrf_token.value
            }
        }).then(function (response) {
            return response.json();
        }).then(function (data) {
        // display a success message
            console.log(data);
            alert.style.display = 'block'
            alert.textContent = data.message ? data.message : data.errors[0]
            // Update authentication status
            isAuthenticated.value = true;
            router.push('/explore');
            setTimeout(function(){
              document.getElementById("alert").style.display="none";}, 3000
            );
            
            
        }).catch(function (error) {
            console.log(error)
        });
    }
</script>
    
    <style>
    .btn-width{
      width: 100%;
    }
    
    .alert{
    list-style: none;
    font-weight: bold;
    font-size: 14px;
    padding: 10px;
    margin-bottom: 10px;
    padding-left:20px ;
    color: var(--clr-light);
    background-color: #c68141;
    border-radius: 0 0 5px 5px;
    -webkit-border-radius: 0 0 5px 5px;
    -moz-border-radius: 0 0 5px 5px;
    -ms-border-radius: 0 0 5px 5px;
    -o-border-radius: 0 0 5px 5px;
    display: none;
}
    </style>