<template>
  <div class="downloadAlert" :class="{active:$store.state.isDownload}">
    下载中 稍等片刻...
  </div>
</template>

<script>
export default {
  el: '',
  data () {
    return {
      
    }
  },
  props:{
    
  },
  methods: {

  },
}
</script>

<style scoped>
@keyframes show{
  0%{
    opacity: 0;
  }
  30%{
    opacity: 1;
  }
  70%{
    opacity: 1;
  }
  100%{
    opacity: 0;
  }
}
  .downloadAlert{
    position: absolute;
    top: 50%;
    left: 50%;
    width: 200px;
    height: 60px;
    line-height: 60px;
    text-align: center;
    
    transform: translate(-50%,-50%);
    background: rgba(0, 0, 0, 0.5);
    color: white;
    font-weight: 700;
    opacity: 0;
  }
  .active{
    animation: show 2s;
    opacity: 1;
  }

</style>
