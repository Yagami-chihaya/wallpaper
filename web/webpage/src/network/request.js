import axios from 'axios'

export function get_data(config){
  let instance = axios.create({
    baseURL:'http://47.105.40.169:5000',
    //baseURL:'http://127.0.0.1:5000',
    timeout:20000,
    headers:{
      'Content-Type':'application/octet-stream'
    }
  })
  instance.interceptors.request.use(config=>config,err=>{console.log(err);})
  console.log(instance(config));
  return instance
}


