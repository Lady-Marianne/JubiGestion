// static/scripts/cancel_activity.js
// This script handles the cancellation of an activity or service when the cancel button is clicked.

document.addEventListener('click', async (event) => {
    if (event.target.classList.contains('cancel-activity-btn')) {
        event.preventDefault(); // Prevent default action if it's a link.
        const activityId = event.target.dataset.id;

        if (!confirm(`¿Está segura/o de que quiere cancelar esta actividad/taller?`)) return;

        try {
            const response = await fetch(`/api/activities/cancel_activity/${activityId}`, {
                method: 'PATCH'
            });

            const result = await response.json();

            if (response.ok) {
                showMessage("Actividad/Taller cancelado correctamente", true);
                setTimeout(() => {
                    window.location.reload();
                }, 3000);
            } else {
                showMessage("Error: " + (result.error || "No se pudo cancelar."), false);
            }

        } catch (error) {
            console.error("Error en la cancelación:", error);
            showMessage("Error: " + (error.message || "Error de red o del servidor."), false);
        }
    }
});