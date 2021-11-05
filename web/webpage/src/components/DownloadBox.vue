<template>
  <div class="downloadBox">
    <div class="leftBox">
      <span>已选择</span>
      <span class="chooseNum">{{chooseNum}}</span>
      <span>张图片</span>
    </div>
    <slot name="function"></slot>
    <div class="rightBox" @click="openFile">
      <img src="../assets/img/文件夹.png">
      查看下载文件夹
    </div>

   
  </div>
</template>

<script>
import {get_data} from '../network/request'

export default {
  el: '',
  data () {
    return {
      
    }
  },
  props:{
    chooseNum:Number,
  },
  methods: {
    openFile(){
      get_data().get('/checkfile').then(res=>{
        console.log(res);
      })
    }
  },
}
</script>

<style scoped>

  .downloadBox{
    position: fixed;
    background: rgba(26, 26, 26, 0.87);
    color: white;
    
    width: 100%;
    height: 80px;
    bottom: -80px;

    z-index: 3;
    display: flex;
    justify-content: space-around;
    align-items: center;
  }
  .downloadBox>.leftBox{
    font-size: 1.5rem;
    font-weight: 600;
    width: 300px;
    height: 100%;
    
    display: flex;
    justify-content: space-evenly;
  }
  .downloadBox>.leftBox>span{

    display: inline-block;  
    
    line-height: 80px;

  }
  .downloadBox>.leftBox>.chooseNum{
    
    color: rgb(0, 131, 11);
    font-size: 2.5rem;
    
  }
  .rightBox{
    background: rgb(0, 111, 185);
    
    height: 30px;
    line-height: 30px;
    padding: 5px 20px;
    cursor: pointer;
    border-radius: 3px;
    vertical-align: middle;
  }
  .rightBox>img{
    
    width: 18px;
    
    vertical-align: middle;
  }
  
</style>
