<template>
  <section class="bg-c9dbe9 gradient-form">
    <div class="container py-5 h-100">
      
      <div class="row d-flex justify-content-center align-items-center">
        <div class="card rounded-3 text-black">
          <div class="container" style="height: 1000px">
            <div class="row h-100">
              <div
                class="col-9 video-wrapper"
                style="padding-bottom: 40%; position: relative"
              >
                <div id="player" style="width: 100%; height: 100%"></div>
              </div>
              <div class="col-3 d-flex flex-column">
                <div class="chat-container">
                  <ul id="chat-room">
                    <!-- <li v-for="comment in comment_list" :key="comment.id">
                      <img :src="comment.user.profile_image ? 'http://localhost:8000'+comment.user.profile_image : require('@/assets/baseuser.png')" style="width: 25px; height: 25px; border-radius: 50%;" />
                      {{ comment.user.nickname }}: {{ comment.content }}
                    </li> -->
                  </ul>
                  <!-- 기존 메시지들 -->
                </div>

                <div class="chat-input">
                  <input
                    @keyup.enter="addChat"
                    v-model="myText"
                    type="text"
                    placeholder="메시지를 입력하세요"
                    v-show="isLoggedIn"
                  />
                  <input v-show="isLoggedIn" @click="addChat" type="submit" value="전송" />
                </div>
               

                <!-- <div class="chat-box">
                  <ul id="chat-room">
                    <li v-for="comment in comment_list" :key="comment.id">
                      <img :src="comment.user.profile_image ? 'http://localhost:8000'+comment.user.profile_image : require('@/assets/baseuser.png')" style="width: 25px; height: 25px; border-radius: 50%;" />
                      {{ comment.user.nickname }}: {{ comment.content }}
                    </li>
                  </ul>
                </div>
                <div class="chat-form">
                  <input type="text" v-model="myText" @keyup.enter="addChat" placeholder="Type your message..." />
                </div> -->
              </div>
               <div class="position-absolute" style="bottom:20%">
                 <h1 class="fw-bold mt-1 mb-5 pb-1" style="color: black">
        {{ movie.title }}
      </h1>
                 <div class="mb-3">
                  
                  <span>
                    <i
                      v-for="(star, idx) in stars"
                      :key="idx"
                      class="fa-solid fa-star"
                      :class="{
                        'text-danger': (idx + 1) * 2 <= movie.vote_average,
                      }"
                    ></i>{{movie.vote_average}}
                  </span>
                 </div>
                  {{movie.overview}}
                </div>
            </div>
          </div>
        </div>
      </div>



    </div>
  </section>
</template>
<script>
import axios from "axios";

const API_KEY = "d838f386c11255ef5f578f676243694f"; // 사용하는 API의 키를 설정하세요.
const API_URL = "https://api.themoviedb.org/3";
let videoWrapper = document.querySelector(".video-wrapper");
let player = document.getElementById("player");
export default {
  name: "MovieDetail",
  computed: {},
  data() {
    return {
      stars:5,
      movie: null,
      videoId: "IoWAdxwfNGU",
      player: null,
      videoDuration: "",
      myText: "",
      comment_list: "",
    };
  },
  created() {
    this.getMovieDetail(this.$route.params.id);
  },
  mounted() {
    const movieId = this.$route.params.id; // 라우터 파라미터로부터 영화 ID를 가져옵니다.
    this.getMovieDetail(movieId);
    // YouTube 플레이어 API 초기화
    const tag = document.createElement("script");
    tag.src = "https://www.youtube.com/iframe_api";
    const firstScriptTag = document.getElementsByTagName("script")[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

    // YouTube Iframe API 초기화를 기다리는 로직 추가
    const waitForAPI = setInterval(() => {
      if (typeof YT !== "undefined" && typeof YT.Player !== "undefined") {
        window.addEventListener("resize", () => {
          player = document.querySelector("#player");
          videoWrapper = document.querySelector(".video-wrapper");
          if (player && videoWrapper) {
            // player.style.width = videoWrapper.clientWidth
            // player.style.height = videoWrapper.clientHeight
          }
        });
        clearInterval(waitForAPI);
        this.player = new YT.Player("player", {
          videoId: this.movie.video_key,
          events: {
            onReady: this.onPlayerReady,
          },
        });
      } else {
        location.reload();
      }
    }, 100);

    axios({
      url: `http://localhost:8000/${this.$route.params.id}/comments/`,
    })
      .then((res) => {
        console.log(res.data, "댓글 리스트 받아오기");
        this.comment_list = res.data;
        this.comment_list.sort((next, current) => {
          const next_time = next.created_at.split(":");
          const cur_time = current.created_at.split(":");
          const next_min = parseInt(next_time[0]);
          const next_sec = parseInt(next_time[1]);
          const cur_min = parseInt(cur_time[0]);
          const cur_sec = parseInt(cur_time[1]);

          if (next_min > cur_min) {
            return 1;
          } else if (next_min < cur_min) {
            return -1;
          } else if (next_sec > cur_sec) {
            return 1;
          } else {
            return -1;
          }
        });
      })
      .catch((err) => {
        console.log(err);
      });

 
  },
  methods: {
    addChat() {
      axios({
        url: `http://localhost:8000/movies/${this.$route.params.id}/comments/`,
        data: { content: this.myText, created_at: this.videoDuration },
        method: "post",
        headers: {
          Authorization: `Bearer ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          const chatRoom = document.querySelector("#chat-room");
          const li = document.createElement("li");
          li.innerText = `${this.$store.state.nickname} : ${this.myText}`;
          const profile = document.createElement("img");
          profile.src = this.$store.state.profileImage
            ? this.$store.state.profileImage
            : require("@/assets/baseuser.png");
          profile.setAttribute(
            "style",
            "width: 25px; height: 25px; border-radius: 50%;"
          );
          li.prepend(profile);
          this.myText = "";

          chatRoom.append(li);
        })
        .catch((err) => {
          console.log(err.response.data);
        });
      // .then((res) => {
      //   const chatRoom = document.querySelector("#chat-room");
      //   const li = document.createElement("li");
      //   li.innerText = this.myText;
      //   chatRoom.append(li);
      // })
      // .catch((err) => {
      //   console.log(err.response.data);
      // });
    },
    getMovieDetail(movieId) {
      axios
        .get(`http://localhost:8000/movies/${movieId}`, {})
        .then((response) => {
          this.movie = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getGenresString(genres) {
      if (!genres) return "";
      return genres.map((genre) => genre.name).join(", ");
    },
    onPlayerReady(event) {
      setInterval(() => {
        this.videoDuration = this.formatTime(event.target.getCurrentTime());
      });
      if (this.comment_list) {
        setInterval(() => {
          this.comment_list.forEach((comment) => {
            if (
              comment.created_at === this.videoDuration &&
              comment.updated == false
            ) {
              comment.updated = true;
              const chatRoom = document.querySelector("#chat-room");
              const li = document.createElement("li");
              li.innerText = `${comment.user.nickname} : ${comment.content}`;
              const profile = document.createElement("img");
              profile.src = comment.user.profile_image
                ? "http://localhost:8000" + comment.user.profile_image
                : require("@/assets/baseuser.png");
              profile.setAttribute(
                "style",
                "width: 25px; height: 25px; border-radius: 50%;"
              );
              li.prepend(profile);

              chatRoom.append(li);
            }
          });
        }, 1000);
      }
      // YouTube 플레이어가 준비되었을 때의 동작
    },
    formatTime(time) {
      const minutes = Math.floor(time / 60);
      const seconds = Math.floor(time % 60);
      return `${minutes}:${seconds < 10 ? "0" : ""}${seconds}`;
    },
    addComment() {
      console.log(this.myText + this.videoDuration);
    },
  },
  updated(){
  },
  computed:{
    isLoggedIn(){
      return this.$store.state.token ? true : false
    }
  }
};
</script>

<style scoped>
section {
  height: 100%;
  min-height: 100vh;
  overflow-y: scroll;
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
ul {
  list-style: none;
}

#player {
  width: 100%;
  height: 100%;
}
<style scoped>
/* ... Existing styles ... */

.chat-box {
  height: 100%;
  background-color: #ffffff;
  padding: 10px;
  border-radius: 10px;
  overflow-y: auto;
}

ul#chat-room {
  list-style: none;
  padding: 0;
  margin: 0;
}

.chat-message {
  display: flex;
  align-items: flex-start;
  margin-bottom: 10px;
}

.profile-image img {
  width: 30px;
  height: 30px;
  border-radius: 50%;
}

.message-content {
  margin-left: 10px;
}

.user-nickname {
  font-weight: bold;
  margin-bottom: 5px;
}

.message-text {
  margin: 0;
}

.chat-form input[type="text"] {
  width: 100%;
  border: none;
  border-radius: 5px;
  padding: 8px;
  font-size: 14px;
}
/* 유튜브 채팅창 디자인 */
.chat-container {
  width: 100%;
  height:50%;
  background-color: #f9f9f9;
  border: 1px solid #ccc;
  overflow-y: scroll;
  padding: 10px;
}

.chat-message {
  margin-bottom: 10px;
}

.chat-message .author {
  font-weight: bold;
  color: #0366d6;
}

.chat-message .message {
  margin-top: 5px;
  color: #333;
}

.chat-input {
  width: 100%;
  margin-top: 10px;
}

.chat-input input[type="text"] {
  width: 80%;
  padding: 8px;
  border: none;
  border-bottom: 2px solid #ccc;
  font-size: 14px;
  color: #333;
  outline: none;
}

.chat-input input[type="submit"] {
  width: 18%;
  padding: 8px;
  border: none;
  background-color: #0366d6;
  color: white;
  cursor: pointer;
  font-size: 14px;
  outline: none;
}

.chat-input input[type="submit"]:hover {
  background-color: #0056b3;
}
/* 일반적인 스크롤바 스타일링 */
.chat-container {
  scrollbar-width: thin;
  scrollbar-color: #888 #f9f9f9;
}

.chat-container::-webkit-scrollbar {
  width: 8px;
}

.chat-container::-webkit-scrollbar-track {
  background-color: #f9f9f9;
}

.chat-container::-webkit-scrollbar-thumb {
  background-color: #888;
  border-radius: 4px;
}

.chat-container::-webkit-scrollbar-thumb:hover {
  background-color: #555;
}
</style>
