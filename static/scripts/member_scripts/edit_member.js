// static/scripts/member_scripts/edit_member.js:

// This script handles the editing of members in the member list.
// It listens for clicks on the edit button, fetches the member data.

document.addEventListener('DOMContentLoaded', () => {
    const memberList = document.getElementById('member-list');

    memberList.addEventListener('click', async (event) => {
        if (event.target.classList.contains('edit-member-btn')) {
            const row = event.target.closest('tr');
            const memberId = row.dataset.id;

            try {
                const res = await fetch(`/api/members/${memberId}`);
                const member = await res.json();

                // Show an emergent form with the loaded data:
                showEditForm(member);
            } catch (error) {
                console.error("Error al obtener los datos del socio:", error);
            }
        }
    });

    function showEditForm(member) {
        const formHtml = `
            <form id="edit-member-form">
                <input type="hidden" name="dni" value="${member.dni}">
                <label>Nombres: <input type="text" name="first_names" value="${member.first_names}"></label><br>
                <label>Apellidos: <input type="text" name="last_name" value="${member.last_name}"></label><br>
                <label>Nro. de Afiliado de PAMI: <input type="text" name="pami_number" value="${member.pami_number}"></label><br>
                <label>Fecha de Nacimiento: <input type="date" name="birth_date" value="${member.birth_date}"></label><br>
                <label>Teléfono: <input type="tel" name="phone" value="${member.phone}"></label><br>
                <label>Correo Electrónico: <input type="email" name="email" value="${member.email}"></label><br>
                <label>Dirección: <input type="text" name="address" value="${member.address}"></label><br>
                <label>Estado:
                    <select name="status">
                        <option value="active" ${member.status === 'active' ? 'selected' : ''}>Activo</option>
                        <option value="inactive" ${member.status === 'inactive' ? 'selected' : ''}>Inactivo</option>
                    </select>
                </label><br>
                <label>Fecha de Ingreso: <input type="date" name="join_date" value="${member.join_date}"></label><br>
                <button type="submit">Guardar cambios</button>
            </form>
        `;

        const modal = document.createElement('div');
        modal.innerHTML = formHtml;
        document.body.appendChild(modal);

        modal.querySelector('#edit-member-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            const data = Object.fromEntries(formData.entries());

            try {
                const res = await fetch(`/api/members/${data.id}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });

                if (res.ok) {
                    alert('Socio actualizado');
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
