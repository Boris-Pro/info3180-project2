<template>
    <div class="container mt-4">
      <div class="row">
        <div class="col-md-9">
          <!-- Column 1 with posts -->
          <div class="card mb-4" v-for="(post, index) in posts" :key="index">
            <div class="card-body" >
                <!-- User profile photo and username -->
            <div class="d-flex align-items-center mb-3">
              <img :src="post.user.profile_photo" class="rounded-circle mr-2" :alt="'Profile Photo of ' + post.user.username" style="width: 100px; height: 100px; object-fit: cover;">
              <span>{{ post.user.username }}</span>
            </div>
              <!-- Row 1: Post Image -->
              <div class="row">
                <div class="col-md-12">
                  <div class="post-image" style="height: 600px;"> <!-- Adjust the height as needed -->
                    <img :src="post.photo" class="photo-img  photo-img" :alt="'Post Image ' + index" style="object-fit: fill;">
                  </div>
                </div>
              </div>
              <!-- Row 2: Post Content -->
              <div class="row mt-3">
                <div class="col-md-12">
                  <p class="card-text">{{ post.caption }}</p>
                  <div class="d-flex justify-content-between align-items-center">
                    <div class="btn-group">
                      <button type="button" class="btn btn-sm btn-outline-secondary">{{ post.likes }} Likes {{ post.count_likes }}</button>
                    </div>
                    <small class="text-muted">{{ formatDate(post.created_on) }}</small>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- Add more posts here -->
        </div>
        <div class="col-md-3">
          <!-- Column 2 with New Post button -->
          <div class="text-center">
            <router-link to="/posts/new" class="btn btn-primary btn-block btn-width">New Post</router-link>
          </div>
        </div>
      </div>
    </div>
  </template>
  

<script setup>
import { ref, onMounted } from 'vue';

const posts = ref([]);

async function fetchPosts() {
  try {
    const response = await fetch('/api/v1/posts');
    if (response.ok) {
      const data = await response.json();
      posts.value = data.posts;
    } else {
      console.error('Failed to fetch posts');
    }
  } catch (error) {
    console.error('Error fetching posts:', error);
  }
}
function formatDate(dateString) {
  const date = new Date(dateString);
  return `${date.getDate()} ${date.toLocaleString('default', { month: 'short' })} ${date.getFullYear()}`;
}

onMounted(() => {
  fetchPosts();
});
</script>

<style>
.btn-width{
      width: 100%;
    }


    .photo-img{
    height: 100%; 
    width: 100%;
    margin-bottom:16px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    /* object-fit: cover; */
    object-fit: contain;
    object-position: top; 
}
</style>