module.exports = {
    publicPath: '',
    pwa: {
        // General config bits..
        name: 'BachelorThesis',
        color: '#1DB954',
        themeColor: '#1DB954',
        start_url: '/?source=pwa',

        // Configuration of the workbox plugin
        workboxPluginMode: 'GenerateSW',
        workboxOptions: {
            navigateFallback: 'index.html',
            skipWaiting: true,
            runtimeCaching: [
                {
                    urlPattern: new RegExp('https://fonts.(gstatic|googleapis).*'),
                    handler: 'NetworkFirst',
                    method: 'GET',
                    options: {cacheableResponse: {statuses: [0, 200, 203]}}
                },
            ],
        }
    }
};
