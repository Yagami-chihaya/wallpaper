<template>
  <div id="nav">
    <div class="showBox">
      <div class='black'>
        <img src="../assets/img/black.png">
      </div>
      <div class="preBox" ref="preBox" id="preBox" @click="move">
        <img v-for="item in url_list" :key="item" :src="item">
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

export default {
  el: '',
  data () {
    return {
      url_list:[],
      pre_length:0,
    }
  },
  methods: {
    cover_init(){
      get_data().get('/showalldata').then(res=>{
        console.log(res.data);
        for(let index=0;index<(res.data.length-parseInt(res.data.length*0.75));index++){
          this.url_list.push(res.data[index][5])
        }
        console.log(this.url_list);
        console.log(this.url_list.length);
        this.pre_length=this.url_list.length
        
      })
    },
    move(){
      let h = 0
      setTimeout(()=>{
        h = document.getElementById('preBox').offsetHeight
        
        let movedown = setInterval(() => {
          
          let offsetY = document.getElementById('preBox').offsetTop
          
          if(offsetY<-h+800){
            clearInterval(movedown)
          }
          document.getElementById('preBox').style.top = `${offsetY-1 }px`
        }, 18);
      },5000)
    },
    start(){
      this.$router.push('/top')
    }
  },
  created(){
    this.cover_init()
    
  },
  mounted(){
    this.move()
    
    
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
  .preBox>img{
    flex: 1;
    width: 300px;
    height: 200px;
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
