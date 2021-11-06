<template>
  <div id="nav">
    <div class="header">
      <img src="../assets/img/钻石.png">
      <span>排行榜</span>
      <p>这里有最热门的壁纸供你下载~</p>
    </div>
    <div class="serachBar">
      <div class="serach_category_button">
        <button v-for="(item,index) in category_list" :key="index" :class="{active:isActive_category.indexOf(index)!=-1}" @click="categoryChange(index)">{{item}}</button>
      </div>
      <div class="serach_resolution_button">
        <p @click="resolutionBoxOpen">分辨率<img :class="{active: isActive_resolution}" src="../assets/img/上.png"></p>
        <div class="optionsBox" :class="{active:isActive_resolution}">
          <div>
            <button class="default" :class="{active:isActive_resolution_default1}" @click="defaultChange">默认</button>
            <span v-for="item in resolution_title" :key="item">{{item}}</span>
            <div v-for="(item,index) in resolution_list" :key="index"><button v-for="(item2,index2) in item" :key="index2" :class="{active:(isActive_resolution_button[0] == index&&isActive_resolution_button[1] == index2&&!isActive_resolution_default1)}" @click="resolutionChange(index,index2,item2)">{{item2}}</button></div>
          </div>
          
        </div>
        <span>{{current_resolution}}</span>
        
      </div>
      <div class="serach_date_button">
        <p @click="dateBoxOpen" >排序时间<img :class="{active:isActive_date}" src="../assets/img/上.png"></p>
        <div class="optionsBox" :class="{active:isActive_date}">
          <button v-for="(item,index) in date_list" :key="index" :class="{active:isActive_date_button==index}" @click="dateChange(index,item)">{{item}}</button>
        </div>
        <span>{{current_date}}</span>
      </div>  
      <div class="refresh" @click="serachRefresh"><img src="../assets/img/refresh.png"></div>
      <div class="download" :class="{active:isActive_download}" @click="showDownloadBox"><img src="../assets/img/下载.png"><span>{{isActive_download?'LOADING':'DOWNLOAD'}}</span></div>
    </div>
      
    <div class="content" ref="content">
      <div v-for="(item,index) in url_list" :key='index' class="page">
        <div class="title">
          <h2>page <span>{{index+1}}</span>/{{Math.ceil((pre_length/24))}}</h2>
          <div class="line"></div>
        </div>
        <div class="imgListBox">
          <div class="imgBox" v-for="(item2,index2) in item" :key="index2">
            <img :src="item2" @click="showPicture(pid_list[index][index2])">
            <div class="backboard">
              <span>{{resolution_all_list[index][index2]}}</span>
              <img class="download" src="../assets/img/下载little.png" @click="download(pid_list[index][index2])">
              
            </div>
            <div class="choose" :class="{active:choose_list.indexOf(pid_list[index][index2])!=-1}" @click="choose(pid_list[index][index2])">
              
            </div>
            
          </div>
        </div>
      </div>
    </div>
    <back-top @click="backTop"></back-top>
    <download-alert></download-alert>
    <download-box :chooseNum="choose_list.length" :class="{downloadBoxActive:choose_list.length>=1||isShowDownloadBox,downloadBoxDeactive:choose_list.length==0&&!isShowDownloadBox}" >
      <template v-slot:function>
        <div class="function" @click="fullselect"><div class="chooseBox"><img src="../assets/img/全选.png"></div>全选</div>
        <div class="function" @click="reverseSelect"><div class="chooseBox"><img src="../assets/img/反选.png"></div>反选</div>
        <div class="function" @click="clearSelect"><div class="chooseBox"><img src="../assets/img/清空.png"></div>清空</div>
        <div class="function" @click="downloadSelect"><div class="chooseBox"><img src="../assets/img/下载.png"></div>下载</div>
      </template>
    </download-box>
  </div>
</template>

<script>
import {get_data} from '../network/request.js'
import backTop from '../components/BackTop.vue'
import downloadAlert from '../components/DownloadAlert.vue'
import downloadBox from '../components/DownloadBox.vue'


export default {
  el: '',
  data () {
    return {
      isActive_category:[0,1,2],
      isActive_resolution:false,
      isActive_date:false,
      category_list:['风景','动漫','人'],
      url_list:[],
      pre_length:0,
      resolution_list:[['2560x1080','3440x1440','3840x1600'],
                       ['1280x720','1600x900','1920x1080','2560x1440','3840x2160'],
                       ['1280x800','1600x1000','1920x1200','2560x1600','3840x2400'],
                       ['1280x960','1600x1200','1920x1440','2560x1920','3840x2880'],
                       ['1280x1024','1600x1280','1920x1536','2560x2048','3840x3072']
                      ],
      resolution_title:['其他','16:9','16:10','4:3','5:4'],
      isActive_resolution_button:'默认',
      isActive_resolution_default1:false,
      date_list:['一天','三天','一周','一个月','三个月','半年','一年'],
      isActive_date_button:0,
      current_resolution:'默认',
      current_date:'一年',
      resolution_all_list:[],   //存储所有图片的分辨率信息
      pid_list:[],
      choose_list:[],
      isShowDownloadBox:false,
      isActive_download:false,
    }
  },
  methods: {
    categoryChange(index){
      console.log(this.isActive_category.indexOf(index));
      if(this.isActive_category.indexOf(index)!=-1){
        this.isActive_category.splice(this.isActive_category.indexOf(index),1)
        console.log(this.isActive_category);
      }else{
        this.isActive_category.push(index)
      }
    },
    resolutionBoxOpen(){
      this.isActive_resolution = !this.isActive_resolution
    },
    dateBoxOpen(){
      this.isActive_date = !this.isActive_date
    },
    resolutionChange(index,index2,item){
      this.isActive_resolution_button = [index,index2]
      if(!this.isActive_resolution_default1){
        this.current_resolution = item
      }
      
    },
    defaultChange(){
      this.isActive_resolution_default1 = !this.isActive_resolution_default1
      this.current_resolution = '默认'
    },
    dateChange(index,item){
      this.isActive_date_button = index
      this.current_date = item
    },
    serachRefresh(){
      this.url_list = []
      this.resolution_all_list = []
      this.pid_list = []
      let category = ''
      let resolution = ''
      let date = this.current_date

      if(this.isActive_category.indexOf(0)!=-1){
        category+=1
      }else{category+=0}
      if(this.isActive_category.indexOf(1)!=-1){
        category+=1
      }else{category+=0}
      if(this.isActive_category.indexOf(2)!=-1){
        category+=1
      }else{category+=0}
      
      if(this.current_resolution=='默认'){
        resolution=''
      }else{
        resolution=this.current_resolution
      }

      if(this.current_date=='一天'){date='1d'}
      else if(this.current_date=='三天'){date='3d'}
      else if(this.current_date=='一周'){date='1w'}
      else if(this.current_date=='一个月'){date='1M'}
      else if(this.current_date=='三个月'){date='3M'}
      else if(this.current_date=='半年'){date='6M'}
      else if(this.current_date=='一年'){date='1y'}


      console.log(category);
      console.log(resolution);
      console.log(date);

      get_data().get('showdata',{params:{category,resolution,date}}).then(res=>{
        console.log(res.data);
        for(let item of res.data){
          this.url_list.push(item[5])
          this.resolution_all_list.push(item[6])
          this.pid_list.push(item[0])
        }
        console.log(this.url_list);
        console.log(this.resolution_all_list);
        console.log(this.pid_list);
        //将缩略图url数组分成多个数组
        this.pre_length=this.url_list.length
        let i = 0
        let new_url_arr = []
        let new_resolution_arr = []
        let new_pid_arr = []
        console.log(this.pre_length);
        while(i<this.pre_length){
          new_url_arr.push(this.url_list.slice(i,i+24))
          new_resolution_arr.push(this.resolution_all_list.slice(i,i+24))
          new_pid_arr.push(this.pid_list.slice(i,i+24))
          i+=24
        }
        this.url_list = new_url_arr
        this.resolution_all_list = new_resolution_arr
        this.pid_list = new_pid_arr
        console.log(this.url_list);
        console.log(this.resolution_all_list);
        console.log(this.pid_list);
      })
    },
    backTop(){
      console.log(this.$refs.content.scrollTop);
      this.$refs.content.scrollTop = 0
    },
    download(pid){
      this.isActive_download = true
      console.log('开始下载了');
      this.$store.state.isDownload = true
      setTimeout(()=>{
        this.$store.state.isDownload = false
      },2000)
      console.log(this.$store.state.isDownload);
      get_data().get('/download',{params:{pid:pid}}).then(res=>{
        console.log(res);
        this.isActive_download = false
      }).catch(()=>{
        
      })
      
    },
    choose(pid){
      if(this.choose_list.indexOf(pid)==-1){
        this.choose_list.push(pid)
      }else{
        this.choose_list.splice(this.choose_list.indexOf(pid),1)
      }
      console.log(this.choose_list);
      this.isShowChooseBox()
      
    },
    isShowChooseBox(){
      if(this.choose_list.length>=1){
        for(let item of document.getElementsByClassName('backboard')){
          item.setAttribute('style','opacity:1 !important')
        }
        for(let item of document.getElementsByClassName('choose')){
          item.setAttribute('style','opacity:1 !important')
        }
        this.isShowDownloadBox = true
      }else {
        for(let item of document.getElementsByClassName('backboard')){
          item.setAttribute('style','')
        }
        for(let item of document.getElementsByClassName('choose')){
          item.setAttribute('style','')
        }
        this.isShowDownloadBox = false
      }
    },
    showDownloadBox(){
      if(this.isShowDownloadBox){
        for(let item of document.getElementsByClassName('backboard')){
          item.setAttribute('style','')
        }
        for(let item of document.getElementsByClassName('choose')){
          item.setAttribute('style','')
        }
      }else{
        for(let item of document.getElementsByClassName('backboard')){
          item.setAttribute('style','opacity:1 !important')
        }
        for(let item of document.getElementsByClassName('choose')){
          item.setAttribute('style','opacity:1 !important')
        }
      }
      
      this.isShowDownloadBox = !this.isShowDownloadBox
    },
    fullselect(){
      
      this.choose_list = []
    
      for(let item of this.pid_list){
        for(let item2 of item){
          this.choose_list.push(item2)
        }
        
      }
      
      console.log(this.choose_list);
      this.isShowChooseBox()
    },
    reverseSelect(){
      let last_choose_list = this.choose_list
      this.choose_list = []
      console.log(this.choose_list);
      for(let item of this.pid_list){
        for(let item2 of item){
          if(last_choose_list.indexOf(item2)==-1  )
          this.choose_list.push(item2)
        }
        
      }
    },
    clearSelect(){
      this.choose_list = []
    },
    downloadSelect(){
      this.$store.state.isDownload = true
      this.isActive_download = true
      
      function p(pid,arr,index){
        
        return new Promise((resolve,reject)=>{
 
          get_data().get('/download',{params:{pid:pid}}).then(()=>{
            if(index+1<arr.length){
              pid = arr[index+1]

              console.log(pid);
              resolve(p(pid,arr,index+1))
            }else {
              
              reject(1)
            }
            
          })
        })
      } 
      p(this.choose_list[0],this.choose_list,0).catch(res=>{
        this.isActive_download = false
        setTimeout(()=>{
          this.$store.state.isDownload = false
        },2000)
        
      })

    },
    showPicture(id){
      this.$router.push('/picture_detail')
      this.$store.state.pid = id
    }

  },
  components:{
    backTop,
    downloadAlert,
    downloadBox
  },
  created(){
    //this.cover_init()
    this.serachRefresh()
  }
}
</script>

<style>
  
</style>
<style scoped>
  @import url('../assets/css/top.css');
</style>
