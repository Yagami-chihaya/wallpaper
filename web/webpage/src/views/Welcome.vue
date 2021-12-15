<template>
  <div v-loading="loading" element-loading-text="Loading..."
    :element-loading-spinner="svg"
    element-loading-svg-view-box="-10, -10, 50, 50"
    element-loading-background="rgba(0, 0, 0, 0.8)" id="nav">
    <div class="showBox">
      <div class='black'>
        <img  src="../assets/img/black.png">
      </div>
      <div  class="preBox" ref="preBox" id="preBox" @click="move">
        <div v-for="item in url_list" :key="item" style="margin:0;padding:0;">
          <img  v-if="item" :src="item">
        
          <el-empty v-else description="description"></el-empty>
        </div>
        
        
      </div>
      <div class="startBox">
        <p class="title">🌈开始你的壁纸之旅</p>
        <div class="button" @click="start">start</div>
      </div>
    </div>
    
  </div>
</template>

<script>
import {get_data} from '../network/request.js'

let animation1 = null
let animation2 = null
let h = 0
let translateY = 0
let speed = 1


export default {
  el: '',
  data () {
    return {
      url_list:[],
      pre_length:0,
      loading:false,
      
    }
  },
  methods: {
    cover_init(){
      this.loading = true
      get_data().get('/showalldata').then(res=>{
        // console.log(res.data);
        for(let index=0;index<(res.data.length-parseInt(res.data.length*0.75));index++){
          this.url_list.push(res.data[index][5])
        }
        // console.log(this.url_list);
        // console.log(this.url_list.length);
        this.pre_length=this.url_list.length
        this.loading = false
      })
    },
    movedown(){
      
      if(translateY<-h+800){
        cancelAnimationFrame(animation1)
      }
      document.getElementById('preBox').style.transform = `translateY(${translateY=translateY - speed}px)`
      animation1 = requestAnimationFrame(this.movedown)
      
    },
    animation_start(){
      h = document.getElementById('preBox').offsetHeight
      
    },
    move(start_time){
      
      
    
      animation2 = setTimeout(() => {
        this.animation_start()
        this.movedown()
      },start_time);
    },
    start(){
      this.$router.push('/top')
    }
  },
  created(){
    this.cover_init()
    
  },
  mounted(){
   
    this.move(2000)
  },
  beforeDestoryed(){
    cancelAnimationFrame(animation1)
    clearTimeout(animation2)
  }
 
}
</script>

<style scoped>
  @keyframes show{
    0%{
      opacity: 0;
    }
    100%{
      opacity: 1;
    }
  }
  .showBox{
    position: relative;
    width: 100%;
    height: 100%;
    overflow:hidden;
    
  }
  .preBox{
    
    position: absolute;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    animation: show 3s;
    
  }
  .preBox>div{
    
    width: 20%;
    
  }
  .preBox>div>img{
    width: 100%;
    height: 100%;
  }
  .black{
    width: 100%;
    height: 100%;
    position: absolute;
    z-index:2;
    opacity: 0.7;
  }
  .black>img{
    width: 100%;
    height: 100%;
  }
  .startBox{
    position: absolute;
    z-index: 3;
    width: 600px;
    height: 200px;
    color: white;
    background: rgba(68, 149, 255, 0.877);
    border-radius: 30px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    margin: 50vh 50vw;
    transform: translate(-50%,-50%);
  }
  .title{
    font-weight: bold;
    font-size: 2.5rem;
  }
  .startBox>.button{
    
    width: 120px;
    height: 40px;
    background: rgb(160, 160, 160);
    text-align: center;
    line-height: 40px;
    border-radius: 40px;
    cursor: pointer;
    font-size: 20px;
  }
  .startBox>.button:hover{
    background: rgb(107, 107, 107);
  }

</style>
