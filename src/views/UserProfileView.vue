<template>
    <div v-if="userProfile" class="container mt-4">
        <div class="card">
            <div class="card-body">
                <div class="user row">
                    <div class="profile-header col-md-3">
                        <img :src="userProfile.profile_photo" alt="Profile Picture" class="profile-picture" style="width: 100px; height: 100px; object-fit: cover;">
                    </div>

                    <div class="profile-info col-md-6">
                        <h2 class="profile-name">{{ userProfile.firstname }} {{ userProfile.lastname }}</h2>
                        <p class="profile-location">{{ userProfile.location }}</p>
                        <p class="profile-bio">{{ userProfile.biography }}</p>
                    </div>

                    <div class="profile-stats col-md-3">
                        <div class="grid2x2">
                            <div class="profile-posts">
                                <span class="profile-stat-count">{{ userProfile.post.count }}</span>
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
        <!-- Display grid of posts' photos -->
            <div class="row mt-4">
            <div class="col-md-4" v-for="post in userProfile.post.data" :key="post.id">
                <div class="card card-hh mb-4">
                <img :src="post.photo" alt="Post Photo" class="card-img-top" style="object-fit: contain;">
                <div class="card-body">
                </div>
                </div>
            </div>
            </div>
    </div>
    <div v-else>
        Loading...
    </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

let userProfile = ref(null);
const route = useRoute();

async function fetchUserProfile(userId) {
    try {
        console.log('Fetching user profile...');
        const response = await fetch(`/api/v1/users/${userId}`);
        if (response.ok) {
            const data = await response.json();
            console.log('User profile data:', data);
            userProfile.value = data;
        } else {
            console.error('Failed to fetch user profile');
        }
    } catch (error) {
        console.error('Error fetching user profile:', error);
    }
}

onMounted(() => {
    const userId = route.params.userId; // Access userId from the URL params using route object
    fetchUserProfile(userId);
});
</script>




<style>
/* Your custom styles */
.grid3x3 {
    display: grid;
    grid-template-columns: 15% 50% 35%;
}
.grid2x2 {
    display: grid;
    grid-template-columns: 50% 50%;
    padding: 10px;
}
.btn-width {
    width: 100%;
}
.card-hh {
    height:350px;
}
</style>
