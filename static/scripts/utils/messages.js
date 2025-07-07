// static/scripts/utils/messages.js

function showMessage(text, isSuccess = true) {
    const box = document.getElementById("message-box");
    box.innerText = text;

    // Cleans previous classes and adds the new one:
    box.classList.remove("message-success", "message-error");
    box.classList.add(isSuccess ? "message-success" : "message-error");

    // Shows the message:
    box.style.display = "block";

    setTimeout(() => {
        box.innerText = "";
        box.classList.remove("message-success", "message-error");
        box.style.display = "none";
    }, 4000);
}
