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
                showMessage("¿Está seguro/a de que quiere eliminar este " + kind + "?", true);

                location.reload();
            } else {
                showMessage("Error: " + (result.error || "No se pudo eliminar."), false);
            }

        } catch (error) {
            console.error("Error en la eliminación:", error);
            showMessage("Error: " + (result.error || "Error de la red o del servidor."), false);
        }
    }
});
