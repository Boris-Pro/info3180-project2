<script setup>
import { ref, onMounted } from "vue";
import {getCsrfToken, getUserId} from "../assets/helper";
import router from "../router/index";

let csrf_token = ref("");
let logged_in = ref("");

let dataLoaded = ref(false);

onMounted(async () => {
    let token = await getCsrfToken();
    csrf_token.value = token.csrf_token;
    const alert = document.querySelector("#alert");

    let user_id = await getUserId();
    logged_in.value = user_id.logged_in

    if(logged_in.value){
        fetch('/api/v1/auth/logout', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token.value
        }
        }).then((response) => {
            return response.json()
        }).then((data) => {
            console.log(data);
            alert.style.display = 'block'
            alert.textContent = data.message ? data.message : data.errors[0]
            router.push('/login')
        }).catch((error) => {
            console.log(error)
        })
    } else {
        alert.style.display = 'block'
        alert.textContent = "You are already logged out."
        router.push('/login')
    }

    dataLoaded.value = true;
})
    
</script>

<template>
    <div class="alert" id="alert"></div>
</template>