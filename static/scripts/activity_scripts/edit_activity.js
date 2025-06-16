// static/scripts/activity_scripts/edit_activity.js:

// This script handles the editing of activities in the activity list.
// It listens for clicks on the edit button, fetches the activity data.

document.addEventListener('DOMContentLoaded', () => {
    const activityList = document.getElementById('activity-list');

    activityList.addEventListener('click', async (event) => {
        if (event.target.classList.contains('edit-activity-btn')) {
            const row = event.target.closest('tr');
            const activityId = row.dataset.id;

            try {
                const res = await fetch(`/api/activities/${activityId}`);
                const activity = await res.json();

                // Show an emergent form with the loaded data:
                showEditForm(activity);
            } catch (error) {
                console.error("Error al obtener los datos de la actividad:", error);
            }
        }
    });

    function showEditForm(activity) {
        const formHtml = `
            <form id="edit-activity-form">
                <input type="hidden" name="id" value="${activity.id}">
                <label>Nombre: <input type="text" name="name" value="${activity.name}"></label><br>
                <label>Descripción: <textarea name="description">${activity.description}</textarea></label><br>
                <label>Horario: <input type="text" name="schedule" value="${activity.schedule}"></label><br>
                <label>Inicio: <input type="date" name="start_date" value="${activity.start_date}"></label><br>
                <label>Fin: <input type="date" name="end_date" value="${activity.end_date}"></label><br>
                <label>Capacidad: <input type="number" name="capacity" value="${activity.capacity}"></label><br>
                <button type="submit">Guardar cambios</button>
            </form>
        `;

        const modal = document.createElement('div');
        modal.innerHTML = formHtml;
        document.body.appendChild(modal);

        modal.querySelector('#edit-activity-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            const data = Object.fromEntries(formData.entries());

            try {
                const res = await fetch(`/api/activities/${data.id}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });

                if (res.ok) {
                    alert('Actividad actualizada');
                    location.reload();
                } else {
                    const errorData = await res.json();
                    alert('Error: ' + errorData.error);
                }
            } catch (error) {
                console.error("Error al enviar PUT:", error);
            }
        });
    }
});
