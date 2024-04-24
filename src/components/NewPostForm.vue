<template>
  <div class="container">
    <div class="row justify-content-center"> <!-- Center the row horizontally -->
    <div class="col-md-6">
    <h2>New Post</h2>
    <div class="card">
      <div class="card-body">
        <form id="postForm" @submit.prevent="add_post">
          <div class="mb-3">
            <label for="photo" class="form-label" style="font-weight: bold;">Photo</label>
            <input type="file" @change="handleFileUpload" class="form-control" id="photo" accept="image/*" style="display: none" />
            <div>
            <label for="photo" class="custom-file-upload" style="font-weight: bold;">Browse</label>
            <span id="fileName" style="margin-left: 10px;">{{ selectedFileName }}</span>
            </div>
          </div>
          <div class="mb-3">
            <label for="caption" class="form-label" style="font-weight: bold;">Caption</label>
            <textarea class="form-control" id="caption" rows="3" v-model="formData.caption" name="caption" placeholder="Write a caption..."></textarea>

          </div>
          <button type="submit" class="btn btn-success" style="width: 100%;">Submit</button>
          <div v-if="showSuccessMessage" class="alert alert-success mt-3">
    {{ successMessage }}
  </div>
  <div v-if="showErrorMessages" class="alert alert-danger mt-3">
    <ul>
      <li v-for="error in errorMessages" :key="error">{{ error }}</li>
    </ul>
  </div>
        </form>
      </div>
    </div>
  </div>
</div>
    
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import {getCsrfToken, getUserId, getJWTToken} from "../assets/helper";

let csrf_token = ref("");
let current_user_id = ref("");
let jwt_token = ref("");
let dataLoaded = ref(false);

onMounted(async () => {
        let token = await getCsrfToken();
        csrf_token.value = token.csrf_token;

        let user_id = await getUserId();
        current_user_id.value = user_id.id;

        let jwt = await getJWTToken();
        jwt_token.value = jwt.jwt_token;

        dataLoaded.value = true;       
    });


let showSuccessMessage = ref(false);
let showErrorMessages = ref(false);
let successMessage = ref("");
let errorMessages = ref([]);
let formData = ref({
  photo: "",
  caption: "",
});

let selectedFileName = ref('No file selected'); // Initialize selectedFileName

async function add_post() {
  const postForm = document.getElementById("postForm");
  const form_data = new FormData(postForm);

  // Check if Photo field is valid before adding it to FormData
  if (formData.value.photo) {
    form_data.append("photo", formData.value.photo);
  }

  try {
    const response = await fetch(`/api/v1/users/${current_user_id.value}/posts`, {
      method: "POST",
      body: form_data,
      headers: {
                'X-CSRFToken': csrf_token.value,
                Authorization: 'Bearer ' + jwt_token.value,
            }
    });

    if (response.ok) {
      const data = await response.json();
      showSuccessMessage.value = true;
      showErrorMessages.value = false;
      successMessage.value = data.message;

      // Clear form data after successful submission
      formData.value.photo = null;
      formData.value.caption = "";
    } else {
      const errorData = await response.json();
      showSuccessMessage.value = false;
      showErrorMessages.value = true;
      errorMessages.value = errorData.errors;
    }
  } catch (error) {
    console.error("Error in add_post:", error);
    showSuccessMessage.value = false;
    showErrorMessages.value = true;
    errorMessages.value = [
      "An unexpected error occurred. Please try again later.",
    ];
  }
}

function handleFileUpload(event) {
  formData.value.photo = event.target.files[0];
  selectedFileName.value = event.target.files[0] ? event.target.files[0].name : 'No file selected';
}

</script>

<style scoped>
/* Add any component-specific styles here */
.custom-file-upload {
display: inline-block;
padding: 8px 20px;
cursor: pointer;
border: 1px solid gray;
background-color: white;
border-radius: 5px;
}

.custom-file-upload:hover {
background-color: #0056b3;
}
</style>
