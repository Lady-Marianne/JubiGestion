// static/scripts/activity_scripts/add_activity.js:

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("add-activity-form");
    const messageBox = document.getElementById("message-box");

    form.addEventListener("submit", async function (event) {
        event.preventDefault();  // Avoids that the form is submitted traditionally.

        // Clear previous messages:
        messageBox.textContent = "";
        messageBox.style.color = "red";

        // Bring data from the form:
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());  // Convert FormData to an object.

        // Validations before sending data.
        // We check that all required fields are filled:
        const errors = [];
        if (!data.name || data.name.trim() === "") errors.push("El nombre de la actividad es obligatorio.");
        if (!data.schedule || data.schedule.trim() === "") errors.push("El horario de la actividad es obligatorio.");
        if (!data.start_date) errors.push("La fecha de inicio de la actividad es obligatoria.");
        if (!data.end_date) errors.push("La fecha de fin de la actividad es obligatoria.");
        if (!data.capacity || data.capacity.trim() === "") errors.push("La capacidad de la actividad es obligatoria.");

        // If there are errors, show alerts and exit:
        if (errors.length > 0) {
            alert("Errores: \n" + errors.join("\n"));
            return;  // We stop the form submission if there are errors.
        }

        // Send the data to the server:
        try {
            const response = await fetch("/api/activities/new", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)  // Convert data to JSON format.
            });

            const result = await response.json();

            if (response.ok) {
                messageBox.style.color = "green";
                messageBox.textContent = "Actividad creada exitosamente: " + result.activity;
                form.reset();
            } else {
                messageBox.textContent = "Error: " + result.error;
            }

        } catch (error) {
            alert("Error de conexión: " + error.message);  // Handle connection errors.
        }
    });
});
