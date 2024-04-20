<template>
    <div class="profile">
      <!-- User Profile Section -->
      <div class="profile-info">
        <h2>{{ userProfile.name }}</h2>
        <p>{{ userProfile.location }}</p>
        <p>Member since {{ userProfile.memberSince }}</p>
        <p>{{ userProfile.biography }}</p>
      </div>
  
      <!-- Posts Section -->
      <div class="posts">
        <div class="row">
          <div v-for="(post, index) in posts" :key="index" class="col-md-4">
            <img :src="post.imageUrl" alt="Post Image">
          </div>
        </div>
      </div>
  
      <!-- Followers Section -->
      <div class="followers">
        <p>Followers: {{ userProfile.followers }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        userProfile: {
          name: 'Rosa Diaz',
          location: 'Kingston, Jamaica',
          memberSince: 'January 2018',
          biography: 'This is my short biography so you can learn more about me.',
          followers: 10
        },
        posts: [
          { imageUrl: 'image1.jpg' },
          { imageUrl: 'image2.jpg' },
          { imageUrl: 'image3.jpg' },
          { imageUrl: 'image4.jpg' },
          { imageUrl: 'image5.jpg' },
          { imageUrl: 'image6.jpg' }
        ]
      };
    }
  };
  </script>
  
  <style>
  /* Add your CSS styling here */
  </style>
  