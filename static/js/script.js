import pyperclip

function copy() {
    var copyText = document.getElementById("link")
    copyText.select()
    document.execCommand("copy")
  }