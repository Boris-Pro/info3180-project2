<template>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <div class="container mt-5">
        <div v-if="showSuccessMessage" class="alert alert-success mt-3">
                  {{ successMessage }}
                </div>
                <div v-if="showErrorMessages" class="alert alert-danger mt-3">
                  <ul>
                    <li v-for="error in errorMessages" :key="error">{{ error }}</li>
                  </ul>
                </div>
      <div class="row">
        <div class="col-md-9">
          <!-- Column 1 with posts -->
          <div class="card mb-4" v-for="(post, index) in posts" :key="index">
            <div class="card-body" >
                <!-- User profile photo and username -->
            <div class="d-flex align-items-center mb-3">
              <img :src="post.user.profile_photo" class="rounded-circle mr-4" :alt="'Profile Photo of ' + post.user.username" style="width: 100px; height: 100px; object-fit: cover;">
              <router-link :to="'/users/' + post.user.id" >
                <span>{{ post.user.username }}</span>
              </router-link>
            </div>
              <!-- Row 1: Post Image -->
              <div class="row">
                <div class="col-md-12">
                  <div class="post-image" style="height: 600px;"> 
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
                        <span @click="likePost(post.id)" class="heart-icon">
                      <i class="far fa-heart " :class="{ 'fas': post.liked, 'far': !post.liked }"></i>
                    </span>
                    <span class="like-count">{{ post.like.count }} Likes</span>
                    </div>
                    <small class="text-muted">{{ formatDate(post.created_on) }}</small>
                  </div>
                </div>
              </div>
            </div>
          </div>
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
import { getUserId } from "../assets/helper";

let current_user_id = ref("");
let showSuccessMessage = ref(false);
let showErrorMessages = ref(false);
let successMessage = ref("");
let errorMessages = ref([]);

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

async function likePost(postId) {
  try {
    const response = await fetch(`/api/v1/posts/${postId}/like`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      
      body: JSON.stringify({ user_id: current_user_id.value }) 
    });

    if (response.ok) {
      // Refresh posts after liking
      const data = await response.json();
      showSuccessMessage.value = true;
      showErrorMessages.value = false;
      successMessage.value = data.message;
      await fetchPosts();
    } else {
      const errorData = await response.json();
      showSuccessMessage.value = false;
      showErrorMessages.value = true;
      errorMessages.value = errorData.errors;
      console.error('Failed to like the post');
    }
  } catch (error) {
    console.error('Error liking the post:', error);
  }
}

onMounted(async () => {

        let user_id = await getUserId();
        current_user_id.value = user_id.id;     
        console.log(current_user_id.value)
        fetchPosts();
    });
  
// onMounted(() => {
//   fetchPosts();
  
// });
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
.like-count {
  margin-left: 8px;
}
.heart-icon {
  cursor: pointer;
}

.router-link-exact-active {
    text-decoration: none;
}
</style>