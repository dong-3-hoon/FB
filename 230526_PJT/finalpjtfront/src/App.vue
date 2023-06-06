<template>
  <!--Main Navigation-->
  <div class="base-background" id="clouds" @click="initialize">
  <div class="position-absolute">
    <div class="cloud x1"></div>
	<!-- Time for multiple clouds to dance around -->
	<div class="cloud x2"></div>
	<div class="cloud x3"></div>
	<div class="cloud x4"></div>
	<div class="cloud x5"></div>
  </div>
  <div class="position-absolute cloud-container">
    <div class="cloud x6"></div>
	<!-- Time for multiple clouds to dance around -->
	<div class="cloud x7"></div>

  <div class="cloud x8"></div>
	<div class="cloud x9"></div>
  <div class="cloud x10"></div>

  </div>
    <header>
      <!-- Sidebar -->
      <nav id="sidebarMenu" class="d-block sidebar bg-c9dbe9">
        <div class="position-sticky">
          <div class="list-group list-group-flush mx-3 rounded">
            <div class="d-flex" v-if="!isLoggedIn">
              <div>
                <router-link
                  :to="{ name: 'login' }"
                  class="py-2 text-black d-flex px-2 text-decoration-none"
                  style="color: #000000"
                  aria-current="true"
                >
                  <div class="rounded-circle me-2 mb-2" style="color: #000000">
                    <i class="fa-solid fa-user"></i>
                  </div>
                  <span class="text-decoration-none">로그인</span>
                </router-link>
              </div>
              <div>
                <router-link
                  :to="{ name: 'signup' }"
                  class="py-2 text-black d-flex px-2 text-decoration-none"
                  style="color: #000000"
                  aria-current="true"
                >
                  <div class="rounded-circle me-2 mb-2"></div>
                  <span class="text-decoration-none">회원가입</span>
                </router-link>
              </div>
            </div>
            <div v-if="isLoggedIn" class="profile-container flex-column d-flex justify-content-center mb-3">
              <label for="upload-profile">
                <div class="d-flex justify-content-between align-items-center">
                  <div class="profile-image rounded-circle d-flex" :class="{ 'bg-white': !profileUrl }">
                    <i v-if="!profileUrl" class="fa-solid fa-user display-6 text-black ms-3 mt-2" style="color: #000000"></i>
                    <img v-else :src="profileUrl" class="profile-image profile-image rounded-circle" alt="" />
                  </div>
                  
                </div>
              </label>
              <input hidden
                  type="file"
                  class="d-none position-absolute p-4"
                  id="upload-profile"
                  @change="onFileChange"
                />
              
              <div class="text-black nickname text-decoration-none ms-2" style="color: #ffffff" to="/">
                <span v-if="!writable"> {{ nickname }} </span>
                <input
                  @keyup.enter="updateNickname()"
                  class="border bg-light text-black"
                  style="color: #ffffff;background-color: aliceblue;"
                  type="text"
                  v-else
                  v-model="CurrentNickname"
                />
                <i
                  @click.stop="correctNickname"
                  class="fa-solid fa-pen pe-5"
                  v-show="!writable"
                  
                ></i>
              </div>
              <span class="text-black ms-2" style="color: #000000"
                >팔로잉 {{ followings }} / 팔로워 {{ followers }}
                
              </span>
              
            </div>
            
            <router-link
              to="/movielist"
              class="text-decoration-none text-black sidebar_list mb-3" style="color: #000000"
            >
              <i class="fa-solid fa-video fa-sm" style="color: #000000;"></i>
              <span> 영화 리스트 </span>
            </router-link>
            
            <router-link
              to="/articles"
              class="text-decoration-none text-black sidebar_list mb-3" style="color: #000000"
            >
              <i class="fa-solid fa-comment fa-sm" style="color: #000000;"></i>
              <span> 커뮤니티 </span>
            </router-link>
            
            <router-link
              to="/cloud"
              class="text-decoration-none text-black sidebar_list mb-3" style="color: #000000"
            >
              <i class="fa-solid fa-cloud fa-sm" style="color: #000000;"></i>
              <span> 영화 추천받기</span>
            </router-link>
            <router-link to="/" class="text-decoration-none text-dark sidebar_list logout" style="color: #000000">
              <i class="fa-solid fa-share-from-square" style="color: #000000;"></i>
                <span @click="logout"> 로그아웃</span>
            </router-link>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>

              <img :src="require('@/assets/testtt.gif')" alt="">
              <!-- <button @click="getMovies">영화 불러오기</button> -->
          </div>
        </div>
      </nav>

      <ul
        class="dropdown-menu dropdown-menu-end"
        aria-labelledby="navbarDropdownMenuAvatar"
      >
        <li>
          <a class="dropdown-item" href="#">My profile</a>
        </li>
        <li>
          <a class="dropdown-item" href="#">Settings</a>
        </li>
        <li>
          <a class="dropdown-item" href="#">Logout</a>
        </li>
      </ul>
      <!-- Sidebar -->

      <!-- Navbar -->

      <!-- Navbar -->
    </header>

    <!--Main Navigation-->
    <main>
      <router-view />
    </main>
  </div>
</template>
<script>
import axios from "axios";
const API_KEY = '프라이베이트안에있는api'

export default {
  setup() {},
  name:'app',
  data() {
    return {
      writable: false,
      settings: false,
      imageUrl: "",
      file: "",
      fileUrl: "",
      CurrentNickname: "",
    };
  },
  components: {},
  methods: {
    testProfile(){
      axios({
        url:'http://localhost:8000/articles/profile/',
        method:'get'
      })
      .then(res =>{
        
        this.imageUrl = res.data.profile_image
        console.log(this.imageUrl)
      }
      )
      
      .catch(err=>{
        console.log(err.response.data)
      })
    },
    getMovies() {
       
        for(let i=201; i<300; i++){
          axios({
            url: `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=true&language=ko-KR&page=${i}&sort_by=popularity.desc`,
            method: "GET",
            headers: {
              Authorization:
                "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMDc4ZjVmNWZjYzg5YjJkOTQ3MDhjNzExNGYyODFmOSIsInN1YiI6IjYzZDMxYjZhYTQxMGM4MTFmOWUwODE2MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.xrFud0jLZqVVUoYkn3vqMno1Q-IPM7pEFNiXbgImyFk",
            },
          }).then((res) => {
            const movieLIst = res.data.results;
            movieLIst.forEach((movie) => {
              axios({
                url: `https://api.themoviedb.org/3/movie/${movie.id}/videos?language=ko-KR`,
                headers: {
                  Authorization:
                    "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMDc4ZjVmNWZjYzg5YjJkOTQ3MDhjNzExNGYyODFmOSIsInN1YiI6IjYzZDMxYjZhYTQxMGM4MTFmOWUwODE2MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.xrFud0jLZqVVUoYkn3vqMno1Q-IPM7pEFNiXbgImyFk",
                },
              })
              .then(res=>{
                console.log(res.data, "비디오 정보")
                if(res.data.results){
                  axios({
                    url : 'http://localhost:8000/movies/',
                    method:'post',
                    data : {
                      ...movie, video_key : res.data.results[0].key
                    },
                    headers : {
                      Authorization : `Bearer ${this.$store.state.token}`
                    }
                  })
                  .then(res=>{
                    console.log(res)
                  })
                  .catch(err=>{
                    console.log(err.response)
                  })
                }
              }).catch(err=>{console.log(err.response)});
            });
          })
          .catch(err=>{
            console.log(err.response)
          });
        }
       
      
    },
    updateNickname() {
      this.$store.dispatch("updateNickname", this.CurrentNickname);
      this.writable = false;
    },
    correctNickname() {
      this.CurrentNickname = this.nickname;
      this.writable = true;
    },
    getImageSrc(base64String) {
      return `data:image/png;base64, ${base64String}`;
    },

    showSetting() {
      this.settings = !this.settings;
    },
    initialize() {
      this.settings = false;
    },
    onFileChange(event) {
      this.file = event.target.files[0];
      // this.fileUrl = URL.createObjectURL(this.file);
      // this.imageUrl = this.fileUrl;
      axios({
        url: "http://localhost:8000/accounts/update/",
        method: "post",
        data: {
          profile_image: this.file,
        },
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `Bearer ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.getProfile();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getProfile() {
      axios({
        url: "http://localhost:8000/accounts/update/",
        method: "get",
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `Bearer ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          //프로필 이미지에 가져온 이미지 저장하기
          this.$store.dispatch("getUserinfo", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    logout() {
      this.$store.dispatch("logout");
    },
     getWeather(){
      axios.get('https://api.openweathermap.org/data/2.5/weather', {
        params: {
          q :'Gwangju',
          appid: API_KEY
        }
      })
      .then((response) => {
        console.log("날씨데이터 받아오기")
        this.$store.dispatch('saveWeather', response.data.weather[0].main)
      })
      .catch((error) => {
        console.log("날씨데이터 받아오기 실패")
        console.error(error);
      });
    },
  },
  computed: {
    isLoggedIn() {
      if (this.$store.state.token) {
        return true;
      } else {
        return false;
      }
    },
    profileUrl() {
      const url = this.$store.state.profileImage;
      return url ?? null;
    },
    nickname() {
      return this.$store.state.nickname;
    },
    followings() {
      return this.$store.state.followings.length;
    },
    followers() {
      return this.$store.state.followers.length;
    },
    
  },
  created() {
    this.$store.dispatch("getToken");
    this.$store.dispatch("getArticles");
    this.$store.dispatch("getUserinfo");
    this.getWeather();
    
  },
};
</script>
<style>
html,
body {
  position: relative;
  background-color: #c9dbe9;
  height: 100vh;
  
  
}
.search_icon {
  color: black;
}

.profile-image {
  width: 70px;
  height: 70px;
  margin-right: 1rem;
  margin-bottom: 1rem;
}

#file-upload-button,
.profile-image:hover {
  cursor: pointer;
}
input[type="file"] {
  width: inherit;
  opacity: 0;
}

input[type="file"]:hover {
  cursor: pointer;
}
main {
  height: 100vh;
  margin-left:240px;
}

.body {
  background-color: #000000;
}


/* Sidebar */

.sidebar {
  position: fixed;
  /* sidebar 옆줄 */
  border-right: 3px solid #ffffff !important;

  top: 0;
  bottom: 0;
  left: 0;
  padding: 30px 0 0; /* Height of navbar */
  box-shadow: 0 2px 5px 0 #c9dbe9, 0 2px 10px 0 #c9dbe9;
  width: 240px;
  z-index: 600;
}

.sidebar .active {
  border-radius: 5px;
  box-shadow: 0 2px 5px 0 #c9dbe9, 0 2px 10px 0 #c9dbe9;
}

.sidebar-sticky {
  position: relative;
  top: 0;
  height: calc(100vh - 48px);
  padding-top: 0.5rem;
  overflow-x: hidden;
  overflow-y: auto; /* Scrollable contents if viewport is shorter than content. */
}

.search__btn:active {
  border: 1px solid #c9dbe9 !important;
}

#main-navbar {
  border-bottom: 1px solid #c9dbe9;
}
.settings {
  position: absolute;
  right: 0px;
}

.sidebar_list {
  font-size: 1.2rem;
  margin-left: 1rem;
}
.profile-img {
  width: 100px;
  height: 100px;
  border-radius: 50%;
}

.logout > span {
  cursor: pointer;
}
</style>
<style>
.base-background {
  background-color: #c9dbe9;
  font-family: "NanumGothic";
  font-weight: bold;
  height: 100vh;
}
.fa-pen {
  cursor: pointer;
}
* {
  margin: 0;
  padding: 0;
}

body {
  /*To hide the horizontal scroller appearing during the animation*/
  overflow: hidden;
}



#clouds {
  padding: 100px 0;
  background: #c9dbe9;
  background: linear-gradient(to bottom, #c9dbe9, #fff);
}


.cloud {
  width: 200px;
  height: 60px;
  background: #fff;
  border-radius: 200px;
  position: relative;
  z-index:0;
}

.cloud:before,
.cloud:after {
  content: "";
  position: absolute;
  background: #fff;
  width: 100px;
  height: 80px;
  position: absolute;
  top: -15px;
  left: 10px;
  border-radius: 100px;
  -webkit-transform: rotate(30deg);
  transform: rotate(30deg);
}

.cloud:after {
  width: 120px;
  height: 120px;
  top: -55px;
  left: auto;
  right: 15px;
}

.x1 {
  -webkit-animation: moveclouds 15s linear infinite;
  animation: moveclouds 15s linear infinite;
  opacity: 0.6;

}

.x2 {
  left: 400px;
  -webkit-transform: scale(0.6);
  transform: scale(0.6);
  opacity: 0.6;
  animation: moveclouds 20s linear infinite;
}

.x3 {
  left: 400px;
  top: -200px;
  -webkit-transform: scale(0.8);
  transform: scale(0.8);
  opacity: 0.8;
  animation: moveclouds 35s linear infinite;
}

.x4 {
  left: 400px;
  top: -250px;
  -webkit-transform: scale(0.75);
  transform: scale(0.75);
  opacity: 0.75;
  animation: moveclouds 40s linear infinite;
}

.x5 {
  left: 400px;
  top: -150px;
  -webkit-transform: scale(0.8);
  transform: scale(0.8);
  opacity: 0.8;
  animation: moveclouds 25s linear infinite;
}

.x6 {
  left: 470px;
  top: -250px;
  -webkit-transform: scale(0.6);
  transform: scale(0.5);
  opacity: 0.8;
  animation: moveclouds 20s linear infinite;
}

.x7 {
  left: 470px;
  top: -200px;
  -webkit-transform: scale(0.8);
  transform: scale(0.8);
  opacity: 0.8;
  animation: moveclouds 25s linear infinite;
}

.x8 {
  left: 470px;
  -webkit-transform: scale(0.8);
  transform: scale(0.8);
  opacity: 0.8;
  animation: moveclouds 30s linear infinite;
}

.x9 {
  left: 470px;
  top: -500px;
  -webkit-transform: scale(0.8);
  transform: scale(0.8);
  opacity: 0.8;
  animation: moveclouds 35s linear infinite;
}

.x10 {
  left: 470px;
  top: -150px;
  -webkit-transform: scale(0.8);
  transform: scale(0.8);
  opacity: 0.8;
  animation: moveclouds 40s linear infinite;
}

@keyframes moveclouds {
  0% {
    margin-left: 1000px;
  }
  100% {
    margin-left: -1000px;
  }
}
.cloud-container{
  top:50%;
}
main{
  margin-top:-100px;
}
</style>

<style scoped>
/*Lets start with the cloud formation rather*/
/*The container will also serve as the SKY*/

</style>