<template>
  <div
    v-loading="loading"
    element-loading-text="Loading..."
    :element-loading-spinner="svg"
    element-loading-svg-view-box="-10, -10, 50, 50"
    element-loading-background="rgba(0, 0, 0, 0.8)"
    id="nav"
  >
    <div class="left">
      <div
        class="download"
        :class="{ active: isActive_download }"
        @click="download(img_data[0][0])"
      >
        <img src="../assets/img/下载.png" /><span>{{
          isActive_download ? "LOADING" : "DOWNLOAD"
        }}</span>
      </div>
      <div class="info">
        <h3>参数信息</h3>
        <p>分辨率: {{ img_data[0][6] }}</p>
        <p>排序方式: 热度</p>
        <p>排序时间: {{ img_data[0][3] }}</p>
      </div>

      <div class="function">
        <div class="black" @click="to_gray">黑白</div>
        <div class="blur" @click="to_gaussianBlur">高斯模糊</div>
        <div class="classic" @click="to_classical">古典</div>
        <img src="../assets/img/左.png" @click="hue_change(22.5)" />
        <div class="color_change" @click="hue_change(90)">色相转换</div>
        <img
          src="../assets/img/左.png"
          @click="hue_change(-22.5)"
          style="transform: rotate(-180deg)"
        />
        <div class="default" @click="default_img">还原</div>
        <div
          class="set"
          :class="{ active: isActive_setting }"
          @click="set_wallpaper(img_data[0][0])"
        >
          <img src="../assets/img/扳手.png" />设置桌面壁纸
        </div>
      </div>
      <div class="back" @click="back">返回上一页</div>
    </div>
    <div class="right">
      <img src="../assets/img/魔术.png" class="magic" @click="magic" />
      <div class="frame">
        <img
          id="cover"
          :class="{
            toBlack: img_state == 1,
            toBlur: img_state == 2,
            toClassic: img_state == 3,
          }"
          :src="img_data[0][1]"
        />
      </div>
    </div>

    <download-alert></download-alert>
  </div>
</template>

<script>
import { get_data } from "../network/request";
import downloadAlert from "../components/DownloadAlert.vue";
import { ElNotification } from "element-plus";

export default {
  el: "",
  data() {
    return {
      img_data: [[]],
      isActive_download: false,
      isActive_setting: false,
      img_state: 0,
      hue_value: 0,
      magic_state: "",
      loading: false,
    };
  },
  methods: {
    init() {
      this.loading = true;
      get_data()
        .get("/showimg", { params: { pid: this.$store.state.pid } })
        .then((res) => {
          console.log(res);
          this.img_data = res.data;
          this.loading = false;
        });
    },
    download(pid) {
      this.isActive_download = true;
      ElNotification({
        title: "Info",
        message: "开始下载~~",
        type: "info",
      });
      this.$store.state.isDownload = true;
      setTimeout(() => {
        this.$store.state.isDownload = false;
      }, 2000);

      if (this.img_state == 1) {
        get_data()
          .get("/to_gray", { params: { pid: pid } })
          .then((res) => {
            ElNotification({
              title: "Success",
              message: "下载完成！",
              type: "success",
            });
            this.isActive_download = false;
          })
          .catch(() => {});
      } else if (this.img_state == 2) {
        get_data()
          .get("/to_gaussianBlur", { params: { pid: pid } })
          .then((res) => {
            ElNotification({
              title: "Success",
              message: "下载完成！",
              type: "success",
            });
            this.isActive_download = false;
          })
          .catch(() => {});
      } else if (this.img_state == 3) {
        get_data()
          .get("/to_classical", { params: { pid: pid } })
          .then((res) => {
            ElNotification({
              title: "Success",
              message: "下载完成！",
              type: "success",
            });
            this.isActive_download = false;
          })
          .catch(() => {});
      } else {
        get_data()
          .get("/download", { params: { pid: pid } })
          .then((res) => {
            console.log(res);
            ElNotification({
              title: "Success",
              message: "下载完成！",
              type: "success",
            });
            this.isActive_download = false;
          })
          .catch(() => {});
      }
    },
    to_gray() {
      this.img_state = 1;
    },
    to_gaussianBlur() {
      this.img_state = 2;
    },
    to_classical() {
      this.img_state = 3;
    },
    hue_change(value) {
      this.img_state = 4;
      this.hue_value += value;
      document.getElementById(
        "cover"
      ).style.filter = `hue-rotate(${this.hue_value}deg)`;
    },
    default_img() {
      this.img_state = 0;
      document.getElementById("cover").style.filter = ``;
      clearInterval(this.magic_state);
    },
    magic() {
      clearInterval(this.magic_state);
      this.img_state = 4;
      this.magic_state = setInterval(() => {
        this.hue_change(1);
      }, 1);
    },
    set_wallpaper(pid) {
      ElNotification({
        title: "Info",
        message: "壁纸获取中...",
        type: "info",
      });
      this.isActive_setting = true;
      get_data()
        .get("/setwallpaper", { params: { pid } })
        .then((res) => {
          ElNotification({
            title: "Success",
            message: "已设置壁纸，请在桌面查看",
            type: "success",
          });
          this.isActive_setting = false;
        });
    },
    back() {
      this.$router.go(-1);
      clearInterval(this.magic_state);
    },
  },
  created() {
    this.init();
  },
  components: {
    downloadAlert,
  },
};
</script>

<style scoped>
@keyframes downloading {
  0% {
    background-color: green;
  }
  100% {
    background: rgb(255, 115, 0);
  }
}

@keyframes downloading_img {
  0% {
  }
  49% {
    transform: translateY(30px);
  }
  50% {
    transform: translateY(-30px);
  }
  100% {
    transform: translateY(0);
  }
}
@keyframes setting {
  0% {
    width: 0%;
  }
  100% {
    width: 100%;
  }
}
#nav {
  background: url("../assets/img/bg-dark-grain.png");
  overflow: hidden;
  display: flex;
  justify-content: center;
}
.left {
  width: 20%;
  height: 100vh;
  background: rgba(83, 83, 83, 0.404);
  position: relative;
}
.left > .download {
  width: 70%;
  margin: 20px 5%;
  border-radius: 5px;
  height: 30px;
  text-align: center;
  line-height: 30px;
  background-color: green;
  cursor: pointer;
  padding: 5px 10%;
  overflow: hidden;
}
.left > .active {
  animation: downloading 1s;
  animation-fill-mode: forwards;
}
.left > .active > img {
  animation: downloading_img 1s infinite;
}
.download > img {
  width: 25px;
  padding: 0 5px;
  vertical-align: middle;
}
.download > span {
  color: white;
  vertical-align: middle;
}
.left > .info {
  width: 80%;
  margin: 10% 10%;
  border-radius: 5px;
  border: 1px solid rgb(109, 109, 109);
}
.left > .info > h3 {
  color: white;
  text-align: center;
}
.left > .info > p {
  margin: 0;
  color: rgb(209, 209, 209);
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  text-align: center;
  border-top: 0.5px solid grey;
}
.left > .function {
  width: 100%;
  height: 140px;

  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  align-items: center;
}
.left > .function > div {
  padding: 0 15px;
  height: 40px;
  line-height: 40px;
  text-align: center;
  border-radius: 5px;
  color: white;
  font-weight: bold;
  font-size: 24px;
  margin: 10px 0;
  cursor: pointer;
}
.left > .function > .color_change {
  width: 60%;
  background: rgb(3, 100, 190);
  border-radius: 15px;
}
.left > .function > .color_change:hover {
  filter: hue-rotate(-90deg);
}
.left > .function > img {
  width: 26px;
  cursor: pointer;
  border-radius: 50%;
}
.left > .function > .black {
  background: white;
  color: rgb(53, 53, 53);
}
.left > .function > .black:hover {
  background: rgb(53, 53, 53);
  color: white;
}
.left > .function > .blur {
  background: grey;
  filter: blur(1px);
}
.left > .function > .blur:hover {
  filter: blur(0);
}
.left > .function > .classic {
  background: rgb(75, 33, 16);
}
.left > .function > .classic:hover {
  background: rgb(95, 55, 40);
}
.left > .function > .default {
  width: 80%;
  border: 1px solid white;
  margin: 20px 0;
}
.left > .function > .default:hover {
  border: 1px solid rgb(124, 124, 124);
}
.left > .function > .set {
  width: 80%;
  border: 1px solid white;
  position: relative;
  z-index: 3;
  overflow: hidden;
}
.left > .function > .set:hover {
  border: 1px solid rgb(105, 105, 105);
}
.left > .function > .set::after {
  content: "";
  position: absolute;
  display: block;
  background-color: rgb(187, 187, 187);
  width: 0%;
  height: 100%;
  top: 0;
  left: 0;
  z-index: -1;
}
.left > .function > .active::after {
  animation: setting 3s;
}
.left > .function > .set > img {
  width: 32px;
  vertical-align: middle;
}
.left > .function > .set > span {
  vertical-align: middle;
}
.left > .back {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 50px;
  color: white;
  font-size: 24px;
  font-weight: bold;
  text-align: center;
  line-height: 50px;
  cursor: pointer;
  background: rgb(146, 140, 132);
  border-top: 1px solid white;
}
.left > .back:hover {
  opacity: 0.5;
}
.right {
  width: 80%;
  height: 100vh;
  display: flex;
  justify-content: center;
}
.frame {
  background: rgb(214, 183, 160);
  border: solid 5vmin rgb(112, 76, 55);
  border-bottom-color: rgb(255, 140, 106);
  border-left-color: rgb(112, 76, 55);
  border-radius: 2px;
  border-right-color: rgb(112, 76, 55);
  border-top-color: rgb(180, 142, 93);
  box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.25) inset,
    0 5px 10px 5px rgba(0, 0, 0, 0.25);
  box-sizing: border-box;
  display: inline-block;
  margin: 5vh 0;

  height: 90vh;
  padding: 4vmin;
  position: relative;
  text-align: center;
}
.frame:before {
  border-radius: 2px;
  bottom: -2vmin;
  box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.25) inset;
  content: "";
  left: -2vmin;
  position: absolute;
  right: -2vmin;
  top: -2vmin;
}
.frame:after {
  border-radius: 2px;
  bottom: -2.5vmin;
  box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.25);
  content: "";
  left: -2.5vmin;
  position: absolute;
  right: -2.5vmin;
  top: -2.5vmin;
}
.frame > img {
  border: solid 2px;
  border-bottom-color: #ffe;
  border-left-color: #eed;
  border-right-color: #eed;
  border-top-color: #ccb;
  max-height: 100%;
  max-width: 100%;
}
.toBlack {
  filter: grayscale(1);
}
.toBlur {
  filter: blur(5px);
}
.toClassic {
  filter: sepia(100%);
}
.magic {
  position: fixed;
  top: 10px;
  right: 2px;
  width: 24px;
  border-radius: 50%;
  cursor: pointer;
}
</style>
