const {app, BrowserWindow, Menu} = require('electron');
Menu.setApplicationMenu(false)

const url = require('url');

function boot() {
    win = new BrowserWindow()
    win.loadURL(url.format({
        pathname: 'products.html',
        slashes: true
    }))
    win.loadURL(url.format({
        pathname: 'seconnecter.html',
        slashes: true
    }))
    win.loadURL(url.format({
        pathname: 'index.html',
        slashes: true
    }))
}

app.on('ready', boot)
