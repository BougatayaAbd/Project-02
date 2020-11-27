const {app, BrowserWindow} = require('electron');
const url = require('url');

let win = null

function boot() {
    win = new BrowserWindow({
        width: 1366,
        height: 768,
        frame: false
    })
    win.loadURL('file://${__dirname}/index.html')
}

app.on('ready', boot)
