// static/scripts/member_scripts/add_member.js:

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("add-member-form");
    const messageBox = document.getElementById("message-box");

    form.addEventListener("submit", async function (event) {
        event.preventDefault(); // Prevent traditional submission.

        // Clear previous messages:
        messageBox.textContent = "";
        messageBox.style.color = "red";

        // Get form data:
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        // Validations:
        const errors = [];
        if (!data.dni || data.dni.trim() === "") errors.push("El DNI es obligatorio.");
        if (!data.gender || data.gender.trim() === "") errors.push("El sexo es obligatorio.");
        if (!data.first_names || data.first_names.trim() === "") errors.push("El nombre es obligatorio.");
        if (!data.last_name || data.last_name.trim() === "") errors.push("El apellido es obligatorio.");
        if (!data.birth_date) errors.push("La fecha de nacimiento es obligatoria.");
        if (!data.phone || data.phone.trim() === "") errors.push("El teléfono es obligatorio.");
        if (!data.email || data.email.trim() === "") errors.push("El correo electrónico es obligatorio.");
        if (!data.address || data.address.trim() === "") errors.push("La dirección es obligatoria.");
        if (!data.join_date) errors.push("La fecha de ingreso es obligatoria.");

        if (errors.length > 0) {
            messageBox.textContent = "Errores:\n" + errors.join("\n");
            return;
        }

        // Send data:
        try {
            const response = await fetch("/api/members/create", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (response.ok) {
                messageBox.style.color = "green";
                messageBox.textContent = "Socio creado exitosamente: " + result.member;
                form.reset();
            } else {
                messageBox.textContent = "Error: " + result.error;
            }
        } catch (error) {
            messageBox.textContent = "Error de conexión: " + error.message;
        }
    });
});
// This script handles the addition of a new member to the system.