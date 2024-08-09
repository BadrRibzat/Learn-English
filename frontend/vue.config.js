const { defineConfig } = require("@vue/cli-service");
const webpack = require('webpack');

module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  configureWebpack: {
    plugins: [
      new webpack.DefinePlugin({
        __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: 'false'
      })
    ]
  },
  css: {
    loaderOptions: {
      postcss: {
        postcssOptions: {
          plugins: [
            require('tailwindcss'),
            require('autoprefixer'),
          ],
        },
      },
    },
  },
  pwa: {
    name: 'English Learning App',
    themeColor: '#4DBA87',
    msTileColor: '#000000',
    appleMobileWebAppCapable: 'yes',
    appleMobileWebAppStatusBarStyle: 'black',
    manifestOptions: {
      name: "English Learning App",
      short_name: "ELA",
      icons: [
        {
          src: "/img/icons/favicon-192x192.png",
          sizes: "192x192",
          type: "image/png"
        },
        {
          src: "/img/icons/favicon-512x512.png",
          sizes: "512x512",
          type: "image/png"
        }
      ],
      start_url: ".",
      display: "standalone",
      background_color: "#ffffff",
      theme_color: "#4DBA87"
    },
    workboxPluginMode: 'InjectManifest',
    workboxOptions: {
      swSrc: './src/service-worker.js',
    }
  },
  chainWebpack: config => {
    config.plugin('html').tap(args => {
      args[0].title = 'English Learning App';
      return args;
    });
  }
});
