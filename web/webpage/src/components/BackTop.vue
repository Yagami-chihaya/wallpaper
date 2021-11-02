<template>
  <div class="backTop">
    <img src="../assets/img/回到顶部.png">
  </div>
</template>

<script>
export default {
  el: '',
  data () {
    return {
      
    }
  },
  methods: {

  },
}
</script>

<style scoped>
@keyframes show{
  0%{

  }
  100%{
    opacity: 1;
    background: rgb(155, 0, 0);
  }
}
  .backTop{
    position: fixed;
    bottom: 20px;
    right: 40px;
    width: 40px;
    height: 40px;
    background: rgb(104, 104, 104);
    border-radius: 50%;
    cursor: pointer;
    opacity: .4;
  }
  .backTop>img{
    margin: 50% 50%;
    transform: translate(-50%,-50%);
  }
  .backTop:hover{
    animation: show .5s;
    animation-fill-mode: forwards;
  }
</style>
