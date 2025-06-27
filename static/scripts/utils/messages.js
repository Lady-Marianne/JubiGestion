// static/scripts/utils/messages.js

function showMessage(text, isSuccess = true) {
    const box = document.getElementById("message-box");
    box.innerText = text;
    box.className = isSuccess ? "message-success" : "message-error";

    setTimeout(() => {
        box.innerText = "";
        box.className = "";
    }, 4000);
}