<template>
<div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h1>Register</h1>
        <div class="card">
          <div class="card-body">
            <form id="userForm" @submit.prevent="add_user">
              <div class="form-group">
                <label for="username">Username</label>
                <input type="text" class="form-control" id="username" name="username" v-model="formData.username">
              </div>
              <div class="form-group">
                <label for="password">Password</label>
                <input type="password" class="form-control" id="password" name="password" v-model="formData.password">
              </div>
              <div class="form-group">
                <label for="firstname">Firstname</label>
                <input type="text" class="form-control" id="firstname" name="firstname" v-model="formData.firstname">
              </div>
              <div class="form-group">
                <label for="lastname">Lastname</label>
                <input type="text" class="form-control" id="lastname" name="lastname" v-model="formData.lastname">
              </div>
              <div class="form-group">
                <label for="email">Email address</label>
                <input type="email" class="form-control" id="email" name="email" v-model="formData.email">
              </div>
              <div class="form-group">
                <label for="location">Location</label>
                <input type="text" class="form-control" id="location" name="location" v-model="formData.location">
              </div>
              <div class="form-group">
                <label for="biography">Biography</label>
                <textarea class="form-control" id="biography" rows="3" name="biography" v-model="formData.biography"></textarea>
              </div>
              <div class="form-group mb-3">
                <label for="profile_photo">Photo</label>
                <input type="file" @change="handleFileUpload" class="form-control" id="profile_photo" accept="image/*" style="display: none" />
                <div>
                <label for="profile_photo" class="custom-file-upload" style="font-weight: bold;">Browse</label>
                <span id="fileName" style="margin-left: 10px;">{{ selectedFileName }}</span>
                </div>
              </div>
              <button type="submit" class="btn btn-primary btn-width">Register</button>
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
import { ref, onMounted} from "vue";
import { getCsrfToken } from "../assets/helper";

let csrf_token = ref("");
let showSuccessMessage = ref(false);
let showErrorMessages = ref(false);
let successMessage = ref("");
let errorMessages = ref([]);
let formData = ref({
  username: "",
  password: "",
  firstname: "",
  lastname: "",
  email: "",
  location: "",
  biography: "",
  profile_photo: null,
});
    onMounted(async () => {
            let token = await getCsrfToken();
            csrf_token.value = token.csrf_token;
        });
        
let selectedFileName = ref('No file selected'); // Initialize selectedFileName

async function add_user() {
  const userForm = document.getElementById("userForm");
  const form_data = new FormData(userForm);

  // Check if Photo field is valid before adding it to FormData
  if (formData.value.profile_photo) {
    form_data.append("profile_photo", formData.value.profile_photo);
  }

  try {
    const response = await fetch("/api/v1/register", {
      method: "POST",
      body: form_data,
            headers: {
                'X-CSRFToken': csrf_token.value,}
    });

    if (response.ok) {
      const data = await response.json();
      showSuccessMessage.value = true;
      showErrorMessages.value = false;
      successMessage.value = data.message;

      // Clear form data after successful submission
      formData.value.username = "";
      formData.value.password = "";
      formData.value.firstname = "";
      formData.value.lastname = "";
      formData.value.email = "";
      formData.value.location = "";
      formData.value.biography = "";
      formData.value.profile_photo = null;
      
    } else {
      const errorData = await response.json();
      showSuccessMessage.value = false;
      showErrorMessages.value = true;
      errorMessages.value = errorData.errors;
    }
  } catch (error) {
    console.error("Error in add_user:", error);
    showSuccessMessage.value = false;
    showErrorMessages.value = true;
    errorMessages.value = [
      "An unexpected error occurred. Please try again later.",
    ];
  }
}

function handleFileUpload(event) {
  formData.value.profile_photo = event.target.files[0];
  selectedFileName.value = event.target.files[0] ? event.target.files[0].name : 'No file selected';
}

</script>

<style>
.btn-width{
  width: 100%;
}

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