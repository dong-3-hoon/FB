<template>
  <section class="bg-c9dbe9 gradient-form">
    <div class="container py-5 h-100">
      <div class="frame" v-show="errorMessage" style="z-index:9999;">
  
  <div >
  <div class="modal2">
    <img src="https://100dayscss.com/codepen/alert.png" width="44" height="38" />
		<span class="title">Error!</span>
		<p>{{errorMessage}}</p>
		<div class="button" @click="clearError">확인</div>
  </div>
</div>
</div>
      <h1 class="fw-bold mt-1 mb-5 pb-1" style="color: black">사용자 정보</h1>
      <div class="row d-flex justify-content-center align-items-center">
        
        <div class="col-xl-10">
          <div class="card rounded-3 text-black">
            <div class="row g-0">
              <div class="col-lg-12">
                <div class="card-body p-md-5 mx-md-4">
                  <div class="row">
   
                        <div class="form-outline mb-4">
                          <label class="form-label" for="new-password1">New Password</label>
                          <input
                          @keyup.enter="saveChanges"
                            v-model="newPassword1"
                            type="password"
                            id="new-password1"
                            class="form-control"
                            placeholder="New Password"
                          />
                        </div>
                        <div class="form-outline mb-4">
                          <label class="form-label" for="new-password2">Password Confirmation</label>
                          <input
                          @keyup.enter="saveChanges"
                            v-model="newPassword2"
                            type="password"
                            id="new-password2"
                            class="form-control"
                            placeholder="Password Confirmation"
                          />
                        </div>
                      </div>
                    </div>
                  </div>
              <div class="text-right">
                <button
                  class="btn btn-dark fa-lg mb-3 me-1 float-end"
                  type="button"
                >
                  Cancel
                </button>
                <button
                  class="btn btn-dark fa-lg mb-3 me-1 float-end"
                  type="button"
                  @click="saveChanges"
                >
                  Save Changes
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
   
    </div>

  </section>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.01:8000'
export default {
  data() {
    return {
      newPassword1:'',
      newPassword2:'',
      newEmail: '',
      errorMessage : '',
    };
  },
  methods: {
    saveChanges() {
      const updatedPassword = {
        new_password1 : this.newPassword1,
        new_password2 : this.newPassword2,
      
      }
      this.$store.dispatch('updateUserInfo', updatedPassword)
      
      axios({
        url : 'http://localhost:8000/accounts/password/change/',
        method : 'post',
        data : {
          ...updatedPassword
        },
        headers : {
          Authorization : `Bearer ${this.$store.state.token}`,
        }
      })
      .then(res =>{
        this.$router.push({name:'movielist'})
      })
      .catch(err =>{
        this.errorMessage = '비밀번호가 일치하지 않습니다'
        console.log(err)
      })
  
      this.newUsername = '';
      this.newEmail = '';
    },
  },
  computed : {
    username(){
      return this.$store.state.userInfo.username
    },
    email(){
      return this.$store.state.userInfo.email
    }
  }
};
</script>

<style scoped>
section {
  height: 100vh;
}

.gradient-custom-2 {
  /* fallback for old browsers */
  background: #3b3b3b;
}

@media (min-width: 768px) {
  .gradient-form {
    height: 100vh;
  }
}

@media (min-width: 769px) {
  .gradient-custom-2 {
    border-top-right-radius: 0.3rem;
    border-bottom-right-radius: 0.3rem;
  }
}

.gradient-form input.form-control {
  border-radius: 50px;
  padding: 10px 20px;
  margin-top: 10px;
  background-color: #f5f5f5;
  border: none;
}

.gradient-form button.btn-primary {
  border-radius: 50px;
  padding: 10px 20px;
  margin-top: 10px;
  background-color: #e62b1e;
  color: #fff;
  font-weight: bold;
  border: none;
}

.gradient-form button.btn-primary:hover {
  background-color: #dd1813;
  cursor: pointer;
}

.card.text-black {
  background-color: #f5f5f5;
}

.card.text-black,
.card.text-black .card-header {
  background-color: #ffffff;
}

.card-header {
  background-color: #e8e8e8;
  border-bottom: none;
  font-weight: bold;
}

.card-body {
  padding: 1.5rem 2rem;
}

@media (max-width: 768px) {
  .gradient-form {
    height: auto;
  }
}

@import url(https://fonts.googleapis.com/css?family=Open+Sans:400,300);
.frame {
  position: absolute;
  left: 50%;
  width: 400px;
  height: 400px;
  margin-left: -200px;
  border-radius: 2px;
  overflow: hidden;
  font-family: "Open Sans", Helvetica, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.modal2 {
  position: absolute;
  width: 280px;
  height: 210px;
  top: 95px;
  left: 60px;
  background: #fff;
  border-radius: 3px;
  box-shadow: 4px 8px 12px 0 rgba(0, 0, 0, 0.4);
  text-align: center;
  overflow: hidden;
  animation: show-modal 0.7s ease-in-out;
}
.modal2.hide {
  animation: hide-modal 0.6s ease-in-out both;
}
.modal2 img {
  margin-top: 24px;
}
.modal2 .title {
  display: block;
  font-size: 18px;
  line-height: 24px;
  font-weight: 400;
  margin: 14px 0 5px 0;
}
.modal2 p {
  font-size: 14px;
  font-weight: 300;
  line-height: 19px;
  margin: 0;
  padding: 0 30px;
}
.modal2 .button {
  position: absolute;
  height: 40px;
  bottom: 0;
  left: 0;
  right: 0;
  background: #F65656;
  color: #fff;
  line-height: 40px;
  font-size: 14px;
  font-weight: 400;
  cursor: pointer;
  transition: background 0.3s ease-in-out;
}
.modal2 .button:hover {
  background: #EC3434;
}

@keyframes show-modal {
  0% {
    transform: scale(0);
  }
  60% {
    transform: scale(1.1);
  }
  80% {
    transform: scale(0.95);
  }
  100% {
    transform: scale(1);
  }
}
@keyframes hide-modal {
  0% {
    transform: scale(1);
  }
  20% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(0);
  }
}

</style>