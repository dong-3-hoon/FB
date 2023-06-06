<template>
  <div class="w-100 h-100">
    <div class="login-form">

      <form class="d-block" @submit.prevent="">
        <div class="svgContainer">
          <div>
           <img src="../assets/asdf.gif" alt="">
          </div>
        </div>
  <p v-show="errorMessage" class="text-danger">잘못된 정보입니다. <br>
    아이디와 패스워드를 확인해주세요</p>
        <div class="">
          <label for="username">ID</label>
          <input type="text" id="username" v-model="username" maxlength="256" />
        </div>
        <div class="inputGroup inputGroup2">
          <label for="password">Password</label>
          <input
            type="password"
            v-model="password"
            id="password"
            class="password"
          />
        </div>
        <div class="inputGroup inputGroup3">
          <button id="login" @click="login">Log in</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      password: "",
      errorMessage:"",
    };
  },
  methods: {
    login() {
      const username = this.username;
      const password = this.password;
      axios({
        url: "http://localhost:8000/auth/login/",
        method: "post",
        data: { username, password },
      })
        .then((res) => {
          this.$store.dispatch("saveToken", res.data);
          this.$store.dispatch("getUserinfo");
          this.$router.push({ name: "home" });
        })
        .catch((err) => {
          console.log(err.response.data);
          this.errorMessage = true
        });
    },
  },
  mounted() {
    var email = document.querySelector("#email"),
      password = document.querySelector("#password"),
      mySVG = document.querySelector(".svgContainer"),
      armL = document.querySelector(".armL"),
      armR = document.querySelector(".armR"),
      eyeL = document.querySelector(".eyeL"),
      eyeR = document.querySelector(".eyeR"),
      nose = document.querySelector(".nose"),
      mouth = document.querySelector(".mouth"),
      mouthBG = document.querySelector(".mouthBG"),
      mouthSmallBG = document.querySelector(".mouthSmallBG"),
      mouthMediumBG = document.querySelector(".mouthMediumBG"),
      mouthLargeBG = document.querySelector(".mouthLargeBG"),
      mouthMaskPath = document.querySelector("#mouthMaskPath"),
      mouthOutline = document.querySelector(".mouthOutline"),
      tooth = document.querySelector(".tooth"),
      tongue = document.querySelector(".tongue"),
      chin = document.querySelector(".chin"),
      face = document.querySelector(".face"),
      eyebrow = document.querySelector(".eyebrow"),
      outerEarL = document.querySelector(".earL .outerEar"),
      outerEarR = document.querySelector(".earR .outerEar"),
      earHairL = document.querySelector(".earL .earHair"),
      earHairR = document.querySelector(".earR .earHair"),
      hair = document.querySelector(".hair");

    function onEmailFocus(e) {
      e.target.parentElement.classList.add("focusWithText");
    }

    function onEmailBlur(e) {
      if (e.target.value == "") {
        e.target.parentElement.classList.remove("focusWithText");
      }
    }

    function onPasswordFocus(e) {
      coverEyes();
    }

    function onPasswordBlur(e) {
      uncoverEyes();
    }

    function getAngle(x1, y1, x2, y2) {
      var angle = Math.atan2(y1 - y2, x1 - x2);
      return angle;
    }

    function getPosition(el) {
      var xPos = 0;
      var yPos = 0;

      while (el) {
        if (el.tagName == "BODY") {
          // deal with browser quirks with body/window/document and page scroll
          var xScroll = el.scrollLeft || document.documentElement.scrollLeft;
          var yScroll = el.scrollTop || document.documentElement.scrollTop;

          xPos += el.offsetLeft - xScroll + el.clientLeft;
          yPos += el.offsetTop - yScroll + el.clientTop;
        } else {
          // for all other non-BODY elements
          xPos += el.offsetLeft - el.scrollLeft + el.clientLeft;
          yPos += el.offsetTop - el.scrollTop + el.clientTop;
        }

        el = el.offsetParent;
      }
      return {
        x: xPos,
        y: yPos,
      };
    }

    email.addEventListener("focus", onEmailFocus);
    email.addEventListener("blur", onEmailBlur);
    email.addEventListener("input", onEmailInput);
    password.addEventListener("focus", onPasswordFocus);
    password.addEventListener("blur", onPasswordBlur);
  },
};
</script>

<style scoped>
/* colors */
html {
  width: 100%;
  height: 100%;
}

body {
  background-color: #eff3f4;
  position: relative;
  width: 100%;
  height: 100%;
  font-size: 16px;
  font-family: "Source Sans Pro", sans-serif;
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
}

form {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: block;
  width: 100%;
  max-width: 400px;
  background-color: #fff;
  margin: 0;
  padding: 2.25em;
  box-sizing: border-box;
  border: solid 1px #ddd;
  border-radius: 0.5em;
  font-family: "Source Sans Pro", sans-serif;
}
form .svgContainer {
  position: relative;
  width: 200px;
  height: 200px;
  margin: 0 auto 1em;
  border-radius: 50%;
  background: none;
  border: solid 2.5px #3a5e77;
  overflow: hidden;
  pointer-events: none;
}
form .svgContainer div {
  position: relative;
  width: 100%;
  height: 0;
  overflow: hidden;
  padding-bottom: 100%;
}
form .svgContainer .mySVG {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}
form .inputGroup {
  margin: 0 0 2em;
  padding: 0;
  position: relative;
}
form .inputGroup:last-of-type {
  margin-bottom: 0;
}
form label {
  margin: 0 0 12px;
  display: block;
  font-size: 1.25em;
  color: #217093;
  font-weight: 700;
  font-family: inherit;
}
form input[type="email"],
form input[type="text"],
form input[type="password"] {
  display: block;
  margin: 0;
  padding: 0 1em 0 !important;
  background-color: #f3fafd;
  border: solid 2px #217093;
  border-radius: 4px;
  -webkit-appearance: none;
  box-sizing: border-box;
  width: 100%;
  height: 65px;
  font-size: 1.55em;
  color: #353538;
  font-weight: 600;
  font-family: inherit;
  transition: box-shadow 0.2s linear, border-color 0.25s ease-out;
}
form input[type="email"]:focus,
form input[type="text"]:focus,
form input[type="password"]:focus {
  outline: none;
  box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
  border: solid 2px #4eb8dd;
}
form input[type="email"],
form input[type="text"] {
  padding: 14px 1em 0px;
}
form button {
  display: block;
  margin: 0;
  padding: 0.65em 1em 1em;
  background-color: #4eb8dd;
  border: none;
  border-radius: 4px;
  box-sizing: border-box;
  box-shadow: none;
  width: 100%;
  height: 65px;
  font-size: 1.55em;
  color: #fff;
  font-weight: 600;
  font-family: inherit;
  transition: background-color 0.2s ease-out;
}
form button:hover,
form button:active {
  background-color: #217093;
}
form .inputGroup1 .helper {
  position: absolute;
  z-index: 1;
  font-family: inherit;
}
form .inputGroup1 .helper1 {
  top: 0;
  left: 0;
  transform: translate(1.4em, 2.6em) scale(1);
  transform-origin: 0 0;
  color: #217093;
  font-size: 1.25em;
  font-weight: 400;
  opacity: 0.65;
  pointer-events: none;
  transition: transform 0.2s ease-out, opacity 0.2s linear;
}
form .inputGroup1.focusWithText .helper {
  /*input[type='email']:focus + .helper {*/
  transform: translate(1.4em, 2em) scale(0.65);
  opacity: 1;
}

form{
  margin-left:100px;
}

</style>
