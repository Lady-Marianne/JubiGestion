document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", async function (event) {
        event.preventDefault();  // Avoids that the form is submitted traditionally.

        // Bring data from the form:
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());  // We convert FormData to an object.

        // Validations before sending data.
        // We check that all required fields are filled:
        const errors = [];
        if (!data.dni || data.dni.trim() === "") errors.push("El DNI es obligatorio.");
        if (!data.gender || data.gender.trim() === "") errors.push("El sexo es obligatorio.");
        if (!data.first_names || data.first_names.trim() === "") errors.push("El nombre es obligatorio.");
        if (!data.last_name || data.last_name.trim() === "") errors.push("El apellido es obligatorio.");
        if (!data.pami_number || data.pami_number.trim() === "") errors.push("El número de PAMI es obligatorio.");
        if (!data.birth_date) errors.push("La fecha de nacimiento es obligatoria.");
        if (!data.phone || data.phone.trim() === "") errors.push("El teléfono es obligatorio.");
        if (!data.email || data.email.trim() === "") errors.push("El correo electrónico es obligatorio.");
        if (!data.address || data.address.trim() === "") errors.push("La dirección es obligatoria.");
        if (!data.join_date) errors.push("La fecha de ingreso es obligatoria.");

        // If there are errors, show alerts and exit:
        if (errors.length > 0) {
            alert("Errores: \n" + errors.join("\n"));
            return;  // We stop the form submission if there are errors.
        }

        // Send the data to the server:
        try {
            // Log the data to be sent:
            console.log("Datos a enviar:", data);
            const response = await fetch("/api/members", {  // We use /api/members to send the request.
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)  // Convert data to JSON format.
            });

            const result = await response.json();

            if (response.ok) {
                alert("Socio creado exitosamente: " + result.member);
                form.reset();  // Clean the form.
            } else {
                alert("Error: " + result.error);  // Show error if the server returns an error.
            }
        } catch (error) {
            alert("Error de conexión: " + error.message);  // Handle connection errors.
        }
    });
});
