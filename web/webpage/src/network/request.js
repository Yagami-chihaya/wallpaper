import axios from 'axios'

export function get_data(config){
  let instance = axios.create({
    baseURL:'http://127.0.0.1:5000',
    timeout:120000
  })
  instance.interceptors.request.use(config=>config,err=>{console.log(err);})
  console.log(instance(config));
  return instance
}

