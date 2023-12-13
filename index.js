
//// Modification in index.js /////


// require ipcRenderer in index.js

const {ipcRenderer} = require('electron')


// modify form submit listener

$("form").submit(e=>{

    e.preventDefault();

    let date = $("#mydate").val();

    console.log("picked date", date)

    ipcRenderer.send("object-date", date);

})



/// modifications in main.js ///

// ipcMain is already required in main.js

// listener to pick the date

ipcMain.on("object-date",(e, date)=>{

  console.log("selected date", date);

})