// Show all activities if we are in the correspondent view:

document.addEventListener("DOMContentLoaded", async function () {
    const activitiesTable = document.querySelector("#activitiesTable");
    if (!activitiesTable) return; // If we are not on the activities list page, exit.

    try {
        const response = await fetch("/api/activities");
        const activities = await response.json();

        // Log the raw response from the server for debugging purposes:
        console.log("Respuesta cruda del servidor:", activities);
        const tbody = activitiesTable.querySelector("tbody");

        if (!response.ok) {
            console.error("Error en la respuesta HTTP:", response.status);
            alert("No se pudieron obtener los datos de las actividades.");
            return;
        }

        if (!Array.isArray(activities)) {
            console.error("Respuesta inesperada: no es un array", activities);
            alert("Error: los datos recibidos no son válidos.");
            return;
        }

        activities.forEach(activity => {
            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${activity.name}</td>
                <td>${activity.start_date}</td>
                <td>${activity.end_date}</td>
                <td>${activity.schedule}</td>
                <td>${activity.description}</td>
                <td>${activity.capacity}</td>
                <td>${activity.members_count || 0}</td>
            `;

            tbody.appendChild(row);
        });

    } catch (error) {
        alert("Error al obtener los datos de las actividades: " + error.message);
    }
});