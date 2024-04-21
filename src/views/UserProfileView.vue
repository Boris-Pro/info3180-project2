<template>
    <div class="container mt-4">
    <div class="card">
      <div class="card-body">
        <div class="user row">
          <div class="profile-header col-md-3">
            <img :src="user.profile_photo" alt="Profile Picture" class="profile-picture" style="width: 100px; height: 100px; object-fit: cover;">
          </div>
  
          <div class="profile-info col-md-6">
            <h2 class="profile-name">{{ user.firstname }} {{ user.lastname }}</h2>
            <p class="profile-location">{{ user.location }}</p>
            <p class="profile-bio">{{ user.biography }}</p>
          </div>
  
          <div class="profile-stats col-md-3">
            <div class="grid2x2">
              <div class="profile-posts">
                <span class="profile-stat-count">0</span>
                <span class="profile-stat-label"><p>Posts</p></span>
              </div>
              <div class="profile-followers">
                <span class="profile-stat-count">0</span>
                <span class="profile-stat-label"><p>Followers</p></span>
              </div>
            </div>
            <div class="profile-actions mt-auto">
              <button class="btn btn-primary btn-block btn-width">Follow</button>
            </div>
          </div>
        </div>
      </div>
    </div>
</div>
  </template>


<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
let user = ref({});
let loading = ref(false);

onMounted(() => {
    loading.value = true;

    fetch('/users/1')
        .then((resp) => resp.json())
        .then((data) => {
            user.value = data.data;
            loading.value = false;
        })
        .catch((err) => {
            console.log(err)
            loading.value = false;
        })
});
</script>
  
  
  <!-- <script>
  export default {
    name: 'Profile',
    data() {
      return {
        profile: {}, // Initialize an empty object to hold user profile data
        postCount: 0,
        followerCount: 0,
      };
    },
    created() {
      // Make an API call to fetch user profile data
      // Replace 'fetchProfileData' with the appropriate API endpoint
      this.fetchProfileData();
    },
    methods: {
      fetchProfileData() {
        // Assuming you have a method in your backend to fetch user profile data by user ID
        // Replace 'userId' with the actual user ID
        // Example API call: axios.get(`/api/profile/${userId}`)
        // After fetching the data, assign it to the 'profile' data property
        // Update the postCount and followerCount properties accordingly
        // For simplicity, I'll set dummy data here
        this.profile = {
          firstname: 'Rosa',
          lastname: 'Diaz',
          location: 'Kingston, Jamaica',
          biography: 'This is my short biography so you can learn more about me.',
          profile_photo: 'profile-picture-url.jpg',
        };
        this.postCount = 6; // You should replace this with the actual post count fetched from the backend
        this.followerCount = 10; // You should replace this with the actual follower count fetched from the backend
      },
    },
  };
  </script> -->
  
  <style>
  /* Your custom styles */
  .grid3x3{
    display: grid;
    grid-template-columns: 15% 50% 35%;
  }
  .grid2x2{
    display: grid;
    grid-template-columns: 50% 50%;
    padding: 10px;
  }
  .btn-width{
      width: 100%;
    }
  </style>
  