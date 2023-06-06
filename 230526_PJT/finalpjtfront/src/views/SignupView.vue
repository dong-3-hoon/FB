<template>
  <!-- <section class="vh-100 bg-c9dbe9" >
    <div class="container h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-lg-12 col-xl-11">
          <div class="card text-black" style="border-radius: 25px">
            <div class="card-body p-md-5">
              <div class="row justify-content-center">
                <div class="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">
                  <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">
                    Sign up
                  </p>

                  <form class="mx-1 mx-md-4">
                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <label class="form-label" for="input-username"
                          >Your Name</label
                        >

                        
                        <b-form-invalid-feedback id="input-username-feedback"
                          >계정 이름은 최소 3글자 이상이어야
                          합니다.</b-form-invalid-feedback
                        >
                      </div>
                    </div>

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-lock fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <label class="form-label" for="form3Example4c"
                          >Password</label
                        >
                       
                      </div>
                    </div>

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-key fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <label class="form-label" for="form3Example4cd"
                          >Repeat your password</label
                        >
                       
                      </div>
                    </div>

                    <div class="form-check d-flex justify-content-center mb-5">
                      <input
                        class="form-check-input me-2"
                        type="checkbox"
                        value=""
                        id="form2Example3c"
                      />
                      <label class="form-check-label" for="form2Example3">
                        I agree all statements in
                        <a href="#!">Terms of service</a>
                      </label>
                    </div>

                    <div
                      class="d-flex justify-content-center mx-4 mb-3 mb-lg-4"
                    >
                      <b-button  @click="()=>{signup(), $bvModal.show('modal-scoped')}" type="button" class="btn btn-dark btn-lg" >
                        Register
                      </b-button>
                    </div>
                  </form>
                </div>
                <div
                  class="col-md-10 col-lg-6 col-xl-7 d-flex align-items-center order-1 order-lg-2"
                >
                  <img
                    src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-registration/draw1.webp"
                    class="img-fluid"
                    alt="Sample image"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>



 

  <b-modal id="my-modal" :title="modalTitle">
    <p v-if="successSignup" class="my-4">회원가입에 성공하셨습니다!! 로그인 페이지로 이동합니다.</p>
    <p v-else class="my-4">회원가입에 실패하셨습니다. 정보를 다시 입력해주세요.</p>
  </b-modal>
</div>



  <b-modal id="modal-scoped" class="bg-dark">
    <template #modal-header="{ close }" >
      <div class="text-center w-100">
        <h5 class="text-white text-center">{{ modalTitle }}</h5>
      </div>
    </template>

    <template >
      <p v-if="successSignup" class="text-white">{{loginTimer}}초 후 로그인 페이지로 이동합니다</p>
      <p v-else class="text-white">{{errorMessage}}</p>
    </template>

    <template #modal-footer="{ ok, cancel, hide }">
      <b-button v-if="successSignup" size="sm" variant="light" @click="goToLogin">
        OK
      </b-button>
      <b-button v-else size="sm" variant="light" @click="ok()">
        OK
      </b-button>

    </template>
  </b-modal>
  </section> -->
  <div class="container">
     
    <div class="wrapper w-100" style="overflow:hidden">
      <ul class="steps">
        <li
          :class="{ 'is-active': currentIndex == 1 }"
        >
          Step 1
        </li>
        <li
          :class="{ 'is-active': currentIndex == 2 }"
        >
          Step 2
        </li>
      </ul>
      <form class="form-wrapper w-100" @submit.prevent="signup">
        <fieldset class="section" :class="{ 'is-active': currentIndex == 1 }">
          <h3 class="fw-bold">회원가입</h3>
          <div class="text-start" style="margin-left:25%">
         <label for="input-username text-start">아이디</label>

          </div>
          <b-form-input
            :value="username"
            id="input-username"
            name="example-input-1"
            v-model.trim="username"
            :state="usernameState"
            aria-describedby="input-username-feedback"
          ></b-form-input>
          <div class="text-start" style="margin-left:25%">
         <label for="input-username text-start">비밀번호</label>

          </div>
            <b-form-invalid-feedback v-if="username" id="input-username-feedback"
                          >계정 이름은 최소 3글자 이상이어야
                          합니다.</b-form-invalid-feedback
                        >
          
          <b-form-input
                        :value="password"
                          id="input-password"
                          name="example-input-2"
                          v-model.trim="password"
                          :state="passwordState"
                          type="password"

                          aria-describedby="input-password-feedback"
                        ></b-form-input>
                        <b-form-invalid-feedback v-if="password" id="input-password-feedback"
                          >비밀번호는 최소 8글자 이상이어야
                          합니다.</b-form-invalid-feedback
                        >
           <div class="text-start" style="margin-left:25%">
         <label for="input-username text-start">비밀번호 확인</label>

          </div>
           <b-form-input
                        :value="password2"
                          id="input-password2"
                          name="example-input-2"
                          type="password"
                          v-model.trim="password2"
                          :state="passwordCheck"
                          aria-describedby="input-password2-feedback"
                        ></b-form-input>
                        <b-form-invalid-feedback v-if="password2" id="input-password2-feedback"
                          >비밀번호가 일치하지
                          않습니다.</b-form-invalid-feedback
                        >
          <input class="submit button" type="button" @click="signup" value="Sign Up" />
        </fieldset>
        <fieldset class="section" :class="{ 'is-active': currentIndex == 2 }">
          <h3 class="fw-bold">회원가입에 성공하셨습니다!!</h3>
          <p class="fw-bold">잠시 후 로그인 페이지로 이동합니다</p>
        </fieldset>
      </form>
  <div class="frame" v-show="checkError" style="z-index:9999;">
  
  <div >
  <div class="modal2">
    <img src="https://100dayscss.com/codepen/alert.png" width="44" height="38" />
		<span class="title">Error!</span>
		<p>{{errorMessage}}</p>
		<div class="button" @click="clearError">확인</div>
  </div>
</div>
</div>
</div>
    </div>
    
  
</template>

<script scoped>
import axios from "axios";
export default {
  data() {
    return {
      successSignup: false,
      modalTitle: "",
      errorMessage: "",
      loginTimer: 3,
      nickname:"",
      username: "",
      password: "",
      password2: "",
      auto: true,
      currentIndex: 1,
      idError:'',
    };
  },
  computed: {
    checkError(){
      console.log('why')
      return this.errorMessage ? true : false
    },
    usernameState() {
     
        return this.username.length < 3 ? false : true;
    },
    passwordState() {
      return this.password.length >= 8 ? true : false;
    },
    passwordCheck() {
      if (
        this.password.length > this.password2.length ||
        this.password2 == ""
      ) {
        return false;
      }
      return this.password == this.password2 ? true : false;
    },
  },
  methods: {
    clearError(){
      this.errorMessage = ''
    },
    signup() {
      const username = this.username;
      const password1 = this.password;
      const password2 = this.password2;
      axios({
        url: "http://localhost:8000/auth/signup/",
        data: { username, password1, password2},
        method: "post",
      })
        .then((res) => {
          this.next()
          this.$store.dispatch('updatedNickname', this.nickname)
          this.successSignup = true;
          this.modalTitle = "회원가입에 성공하였습니다!!";
          setInterval(() => {
            this.loginTimer -= 1;
          }, 1000);
          setTimeout(() => {
            if (this.auto) {
              this.$router.push({ name: "login" });
            }
          }, 3000);
        })
        .catch((err) => {
          this.successSignup = false;
          console.log(err.response.data);

          this.modalTitle = "회원가입 실패...";
          const errorData = err.response.data;
          if (errorData.username && errorData.username[0].includes("exists")) {
            this.errorMessage = "이미 존재하는 ID입니다.";
          } else if (
            errorData.password1 &&
            errorData.password1[0].includes("short")
          ) {
            this.errorMessage = "비밀번호가 너무 짧습니다.";
            console.log("비밀번호 x");
          } else if (errorData.non_field_errors) {
            this.errorMessage = "비밀번호가 일치하지 않습니다.";
          } else {
            this.errorMessage = "비어있는 칸이 존재하면 안됩니다.";
          }
        });
    },
    goToLogin() {
      console.log("??");
      this.auto = false;
      this.$router.push({ name: "login" });
    },
    next() {
      this.currentIndex += 1;
    },
  },
  updated(){
    console.log(this.errorMessage)
  }
};
</script>
<style scoped>
html,
body {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  font-family: "Open Sans", sans-serif;
  background-color: #4eb8dd;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-weight: 200;
}

a {
  text-decoration: none;
}

p,
li,
a {
  font-size: 14px;
}

fieldset {
  margin: 0 !important;
  padding: 0 !important;
  border: none;
}

/* GRID */

.twelve {
  width: 100%;
}
.eleven {
  width: 91.53%;
}
.ten {
  width: 83.06%;
}
.nine {
  width: 74.6%;
}
.eight {
  width: 66.13%;
}
.seven {
  width: 57.66%;
}
.six {
  width: 49.2%;
}
.five {
  width: 40.73%;
}
.four {
  width: 32.26%;
}
.three {
  width: 23.8%;
}
.two {
  width: 15.33%;
}
.one {
  width: 6.866%;
}

/* COLUMNS */

.col {
  display: block;
  float: left;
  margin: 0 0 0 1.6%;
}

.col:first-of-type {
  margin-left: 0;
}

.container {
  width: 100%;
  max-width: 700px;
  margin: 0 auto;
  position: relative;
}

.row {
  padding: 20px 0;
}

/* CLEARFIX */

.cf:before,
.cf:after {
  content: " ";
  display: table;
}

.cf:after {
  clear: both;
}

.cf {
  *zoom: 1;
}

.wrapper {
  width: 100%;
  margin: 30px 0;
}

/* STEPS */

.steps {
  list-style-type: none;
  margin: 0;
  padding: 0;
  background-color: #fff;
  text-align: center;
}

.steps li {
  display: inline-block;
  margin: 20px;
  color: #ccc;
  padding-bottom: 5px;
}

.steps li.is-active {
  border-bottom: 1px solid #4eb8dd;
  color: #4eb8dd;
}

li {
  cursor: pointer;
}
/* FORM */

.form-wrapper .section {
  width:98.2%;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  background-color: #fff;
  opacity: 0;
  -webkit-transform: scale(1, 0);
  transform: scale(1, 0);
  -webkit-transform-origin: top center;
  transform-origin: top center;
  -webkit-transition: all 0.5s ease-in-out;
  transition: all 0.5s ease-in-out;
  text-align: center;
  position: absolute;
  min-height: 300px;
}

.form-wrapper .section h3 {
  margin-bottom: 30px;
}

.form-wrapper .section.is-active {
  opacity: 1;
  transform: scale(1.0);
}

.form-wrapper .button,
.form-wrapper .submit {
  background-color: #4eb8dd;
  display: inline-block;
  padding: 8px 30px;
  color: #fff;
  cursor: pointer;
  font-size: 14px !important;
  font-family: "Open Sans", sans-serif !important;
  position: absolute;
  right: 20px;
  bottom: 20px;
}

.form-wrapper .submit {
  border: none;
  outline: none;
  -webkit-box-sizing: content-box;
  -moz-box-sizing: content-box;
  box-sizing: content-box;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
}

.form-wrapper input[type="text"],
.form-wrapper input[type="password"] {
  display: block;
  padding: 10px;
  margin: 10px auto;
  background-color: #f1f1f1;
  border: none;
  width: 50%;
  outline: none;
  font-size: 14px !important;
  font-family: "Open Sans", sans-serif !important;
}

.form-wrapper input[type="radio"] {
  display: none;
}

.form-wrapper input[type="radio"] + label {
  display: block;
  border: 1px solid #ccc;
  width: 100%;
  max-width: 100%;
  padding: 10px;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  cursor: pointer;
  position: relative;
}

.form-wrapper input[type="radio"] + label:before {
  content: "✔";
  position: absolute;
  right: -10px;
  top: -10px;
  width: 30px;
  height: 30px;
  line-height: 30px;
  border-radius: 100%;
  background-color: #4eb8dd;
  color: #fff;
  display: none;
}

.form-wrapper input[type="radio"]:checked + label:before {
  display: block;
}

.form-wrapper input[type="radio"] + label h4 {
  margin: 15px;
  color: #ccc;
}

.form-wrapper input[type="radio"]:checked + label {
  border: 1px solid #4eb8dd;
}

.form-wrapper input[type="radio"]:checked + label h4 {
  color: #4eb8dd;
}

/* .modal-body, .modal-header, .modal-footer{
  background-color:black !important;
  border : 1px solid black !important;
} */
@import url(https://fonts.googleapis.com/css?family=Open+Sans:400,300);
.frame {
  position: absolute;
  top: 50%;
  left:50%;
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
