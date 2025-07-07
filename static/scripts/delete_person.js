document.addEventListener('click', async (event) => {
    if (event.target.classList.contains('delete-person-btn')) {
        event.preventDefault(); // Prevent default action if it's a link.
        const personId = event.target.dataset.id;
        const kind = event.target.dataset.kind;

        if (!confirm(`¿Está segura/o de que quiere eliminar este ${kind}?`)) return;

        try {
            const response = await fetch(`/api/persons/delete_person/${kind}/${personId}`, {
                method: 'PATCH'
            });

            const result = await response.json();

            if (response.ok) {
                // Show success message after deletion:
                showMessage(`${kind.charAt(0).toUpperCase() + kind.slice(1)} eliminado correctamente.`, true);

                // Wait for the message to show, then reload the page:
                setTimeout(() => {
                    location.reload();
                }, 1500); // Wait 1.5 seconds before reloading the page.
            } else {
                showMessage("Error: " + (result.error || "No se pudo eliminar."), false);
            }

        } catch (error) {
            console.error("Error en la eliminación:", error);
            showMessage("Error: " + (result.error || "Error de la red o del servidor."), false);
        }
    }
});
