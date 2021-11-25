module.exports = {
  //打包是否生成.map文件
  
  publicPath:'./',
  
  productionSourceMap: true,
  
  pages: {
      index: {
          entry: 'src/main.js',
          template: 'public/index.html',
          filename: 'index.html',
          chunks: ['chunk-vendors', 'chunk-common', 'index']
      }
  },
  configureWebpack:{
    module:{
      rules:[
        {
          test:/\.mjs$/,
          include:/node_modules/,
          type:"javascript/auto"
        }
      ]
    }
  }
  
};
