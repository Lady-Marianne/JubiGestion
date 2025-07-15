// scripts/utils/confirmation.js:

function showConfirmation(message, onConfirm) {
    const modal = document.getElementById("confirm-modal");
    const msgBox = document.getElementById("confirm-message");
    const yesBtn = document.getElementById("confirm-yes");
    const noBtn = document.getElementById("confirm-no");

    msgBox.textContent = message;
    modal.classList.remove("hidden");

    // Evitar múltiples listeners: primero los quitamos
    yesBtn.replaceWith(yesBtn.cloneNode(true));
    noBtn.replaceWith(noBtn.cloneNode(true));

    // Volvemos a seleccionarlos (ahora sin listeners previos)
    const newYesBtn = document.getElementById("confirm-yes");
    const newNoBtn = document.getElementById("confirm-no");

    newYesBtn.addEventListener("click", () => {
        modal.classList.add("hidden");
        onConfirm();
    });

    newNoBtn.addEventListener("click", () => {
        modal.classList.add("hidden");
    });
}
