document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", async function (event) {
        event.preventDefault();  // Avoids that the form is submitted traditionally.

        // Bring data from the form:
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());  // Convert FormData to an object.

        // Validations before sending data.
        // We check that all required fields are filled:
        const errors = [];
        if (!data.name || data.name.trim() === "") errors.push("El nombre de la actividad es obligatorio.");
        if (!data.start_date) errors.push("La fecha de inicio de la actividad es obligatoria.");
        if (!data.end_date) errors.push("La fecha de fin de la actividad es obligatoria.");
        if (!data.schedule || data.schedule.trim() === "") errors.push("El horario de la actividad es obligatorio.");
        if (!data.description || data.description.trim() === "") errors.push("La descripción de la actividad es obligatoria.");
        if (!data.capacity || data.capacity.trim() === "") errors.push("La capacidad de la actividad es obligatoria.");

        // If there are errors, show alerts and exit:
        if (errors.length > 0) {
            alert("Errores: \n" + errors.join("\n"));
            return;  // We stop the form submission if there are errors.
        }

        // Send the data to the server:
        try {
            console.log("Datos a enviar:", data);
            const response = await fetch("/api/activities", {  // We use /api/activities to send the request.
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)  // Convert data to JSON format.
            });

            const result = await response.json();

            if (response.ok) {
                alert("Actividad creada exitosamente: " + result.activity);
                form.reset();  // Clean the form.
            } else {
                alert("Error: " + result.error);  // Show error if the server returns an error.
            }
        } catch (error) {
            alert("Error de conexión: " + error.message);  // Handle connection errors.
        }
    });
});
