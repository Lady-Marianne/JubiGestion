document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('edit-member-form');
    const urlParams = new URLSearchParams(window.location.search);
    const currentStatus = urlParams.get('status') || 'ACTIVO';

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const memberId = form.dataset.memberId;
        const formData = new FormData(form);
        
        // Show loader (optional):
        const submitBtn = form.querySelector('button[type="submit"]');
        submitBtn.disabled = true;
        submitBtn.textContent = 'Guardando...';

        try {
            const response = await fetch(`/api/members/update_member/${memberId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(Object.fromEntries(formData))
            });

            // Verificar si la respuesta es JSON:
            const contentType = response.headers.get('content-type');
            if (!contentType || !contentType.includes('application/json')) {
                const text = await response.text();
                throw new Error(text || 'Respuesta no JSON');
            }

            const result = await response.json();
            
            if (!response.ok) {
                throw new Error(result.error || 'Error al guardar');
            }

            alert(result.message || "¡Cambios guardados!");
            const redirectUrl = `/api/persons/ver_personas/member?status=${currentStatus}`;
            console.log("Redirigiendo a:", redirectUrl);
            window.location.href = redirectUrl;
            
        } catch (error) {
            console.error("Error:", error);
            alert("Error: " + (error.message || "Verifica la consola"));
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
