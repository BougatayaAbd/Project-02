const {app, BrowserWindow} = require('electron');
const url = require('url');

function boot() {
    win = new BrowserWindow()
    win.loadURL(url.format({
        pathname: 'products.html',
        slashes: true,
        frame: false
    }))
    win.loadURL(url.format({
        pathname: 'seconnecter.html',
        slashes: true,
        frame: false
    }))
    win.loadURL(url.format({
        pathname: 'index.html',
        slashes: true,
        frame: false
    }))
}

app.on('ready', boot)
