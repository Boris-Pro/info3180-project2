<template>
<div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h1>Register</h1>
        <div class="card">
          <div class="card-body">
            <form>
              <div class="form-group">
                <label for="username">Username</label>
                <input type="text" class="form-control" id="username" >
              </div>
              <div class="form-group">
                <label for="password">Password</label>
                <input type="password" class="form-control" id="password">
              </div>
              <div class="form-group">
                <label for="firstname">Firstname</label>
                <input type="text" class="form-control" id="firstname" >
              </div>
              <div class="form-group">
                <label for="lastname">Lastname</label>
                <input type="text" class="form-control" id="lastname" >
              </div>
              <div class="form-group">
                <label for="email">Email address</label>
                <input type="email" class="form-control" id="email">
              </div>
              <div class="form-group">
                <label for="location">Location</label>
                <input type="text" class="form-control" id="location" >
              </div>
              <div class="form-group">
                <label for="biography">Biography</label>
                <textarea class="form-control" id="biography" rows="3" ></textarea>
              </div>
              <div class="form-group">
                <label for="photo">Photo</label>
                <input type="file" class="form-control-file" id="photo">
              </div>
              <button type="submit" class="btn btn-primary btn-width">Register</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

</script>

<style>
.btn-width{
  width: 100%;
}

</style>