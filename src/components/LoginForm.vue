<template>
    <div class="container mt-5">
        <div class="row justify-content-center">
          <div class="col-md-6">
            <h1>Login</h1>
            <div class="card">
              <div class="card-body">
                <form @submit.prevent="login">
                  <div class="form-group">
                    <label for="username">Username</label>
                    <input type="text" class="form-control" id="username" v-model = "username">
                  </div>
                  <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" class="form-control" id="password" v-model = "password">
                  </div>
                  <button type="submit" class="btn btn-success btn-width">Login</button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </template>
    
    <script>
export default {
  data() {
    return {
      username: '',
      password: '',
      error: null
    };
  },
  methods: {
    async login() {
      try {
        const response = await fetch('/api/v1/auth/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password
          })
        });

        const responseData = await response.json();

        // If login is successful, do something with the response
        if (response.ok) {
          console.log(responseData);
          // For example, you can redirect the user to another page
          this.$router.push('/');
        } else {
          // If login fails, handle the error
          if (response.status === 400) {
            // Bad request, form errors returned from server
            this.error = responseData.errors;
          } else {
            // Other types of errors (e.g., server down)
            console.error('Login error:', responseData);
            this.error = 'An error occurred during login.';
          }
        }
      } catch (error) {
        console.error('Fetch error:', error);
        this.error = 'An error occurred during login.';
      }
    }
  }
};
</script>
    
    <style>
    .btn-width{
      width: 100%;
    }
    
    </style>