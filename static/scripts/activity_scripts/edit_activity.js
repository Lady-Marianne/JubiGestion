// static/scripts/activity_scripts/edit_activity.js:

// This script handles the editing of activities in the activity list.
// It listens for clicks on the edit button, fetches the activity data.

document.addEventListener('DOMContentLoaded', () => {
    const activityList = document.getElementById('edit-activity-form');
    const urlParams = new URLSearchParams(window.location.search);
    const currentStatus = urlParams.get('status') || 'ACTIVO';

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const activityId = form.dataset.activityId;
        const formData = new FormData(form);

        // Show loader (optional):
        const submitBtn = form.querySelector('button[type="submit"]');
        submitBtn.disabled = true;
        submitBtn.textContent = 'Guardando...';

        try {
            const response = await fetch(`/api/activities/update_activity/${activityId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(Object.fromEntries(formData))
            });

            // Verify if the response is JSON:
            const contentType = response.headers.get('content-type');
            if (!contentType || !contentType.includes('application/json')) {
                const text = await response.text();
                throw new Error(text || 'Response is not JSON');
            }

            const result = await response.json();

            if (!response.ok) {
                throw new Error(result.error || 'Error al guardar');
            }

            showMessage("Actividad/Taller actualizado exitosamente: ", true);

            // Wait 3 seconds before redirecting:
            setTimeout(() => {
                const redirectUrl = `/api/activities/ver_actividades/activity?status=${currentStatus}`;
                console.log("Redirigiendo a:", redirectUrl);
                window.location.href = redirectUrl;
            }, 3000);

        } catch (error) {
            console.error("Error:", error);
            alert("Error: " + (error.message || "Verify the console"));
        } finally {
            submitBtn.disabled = false;
            submitBtn.textContent = 'Guardar Cambios';
        }

    });
});

document.addEventListener("DOMContentLoaded", function () {
    const cancelButton = document.getElementById("cancel-button");
    if (cancelButton) {
        const url = cancelButton.getAttribute("data-url");
        cancelButton.addEventListener("click", function () {
            window.location.href = url;
        });
    }
});