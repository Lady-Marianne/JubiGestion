// static/scripts/activity_scripts/show_activities.js

document.addEventListener("DOMContentLoaded", async function () {
    const activitiesTable = document.querySelector("#activitiesTable");
    if (!activitiesTable) return;

    const urlParams = new URLSearchParams(window.location.search);
    const status = urlParams.get("status") || "ACTIVO";

    const titleMap = {
        "ACTIVO": "ACTIVIDADES Y TALLERES ACTIVOS:",
        "SUSPENDIDO": "ACTIVIDADES Y TALLERES SUSPENDIDOS:",
        "CANCELADO": "ACTIVIDADES Y TALLERES CANCELADOS:"
    };
    const titleElement = document.getElementById("activities-title");
    if (titleElement) {
        titleElement.textContent = titleMap[status] || "LISTADO DE ACTIVIDADES Y TALLERES:";
    }

    try {
        const response = await fetch(`/api/activities/all?status=${status}`);
        if (!response.ok) {
            showMessage("Error al obtener las actividades y talleres.", false);
            return;
        }

        const activities = await response.json();
        const tbody = activitiesTable.querySelector("tbody");
        tbody.innerHTML = "";

        if (!Array.isArray(activities)) {
            showMessage("Error: los datos recibidos no son válidos.", false);
            return;
        }

        activities.forEach(activity => {
            const row = document.createElement("tr");

            const startDate = activity.start_date?.split('T')[0] || "";
            const endDate = activity.end_date?.split('T')[0] || "";

            row.innerHTML = `
                <td>${activity.name}</td>
                <td>${activity.description}</td>
                <td>${activity.schedule}</td>
                <td>${startDate}</td>
                <td>${endDate}</td>
                <td>${activity.capacity}</td>
                <td>
                    <button class="edit-activity-btn" data-id="${activity.id}" title="Editar">
                        <i class="fas fa-pen"></i>
                    </button>
                    <button class="delete-activity-btn" data-id="${activity.id}" title="Cancelar">
                        <i class="fas fa-trash"></i>
                    </button>
                </td>`;
            tbody.appendChild(row);
        });

        // Edit buttons
        document.querySelectorAll(".edit-activity-btn").forEach(btn => {
            btn.addEventListener("click", (e) => {
                e.preventDefault();
                const id = e.currentTarget.dataset.id;
                window.location.href = `/api/activities/editar_actividad/${id}`;
            });
        });

    } catch (error) {
        console.error("Error al cargar actividades y talleres:", error);
        showMessage("Error al obtener las actividades y talleres. Verificá tu conexión.", false);
    }
});

// ✅ Delete handler con confirmación:
document.addEventListener("click", async function (event) {
    const button = event.target.closest(".delete-activity-btn");
    if (!button) return;

    const activityId = button.dataset.id;

    showConfirmation("¿Estás segura/o de que querés cancelar esta actividad/taller?", async () => {
        try {
            const response = await fetch(`/api/activities/delete/${activityId}`, {
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
    });
});
