// static/scripts/member_scripts/edit_member.js:

// This script handles the editing of members in the member list.
// It listens for clicks on the edit button, fetches the member data.
/*
document.addEventListener('DOMContentLoaded', () => {
    const memberList = document.getElementById('member-list');
    if (!memberList) return; // If we are not on the member list page, exit.

    memberList.addEventListener('click', async (event) => {
        if (event.target.classList.contains('edit-member-btn')) {
            const row = event.target.closest('tr');
            const memberId = event.target.dataset.id;
            try {
                const res = await fetch(`/api/members/${memberId}`);
                if (!res.ok) throw new Error("No se pudo obtener el socio");
                const member = await res.json();

                // Show an emergent form with the loaded data:
                showEditForm(member, memberId);
            } catch (error) {
                console.error("Error al obtener los datos del socio:", error);
                alert("Error al obtener los datos del socio: " + error.message);
            }
        }
    });

    function showEditForm(member, memberId) {
        const formHtml = `
            <div class="modal-container">
                <form id="edit-member-form">
                    <h3>Editando Socio: ${member.first_names} ${member.last_name}</h3>
                    <input type="hidden" name="id" value="${member.id}">
                    <label for="gender">Sexo:</label>
                    <select name="gender" required>
                        <option value="M" ${member.gender === 'M' ? 'selected' : ''}>Masculino</option>
                        <option value="F" ${member.gender === 'F' ? 'selected' : ''}>Femenino</option>
                    </select><br>
                    <label>DNI: <input type="text" name="dni" value="${member.dni}" required></label><br>
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
                    <div class="form-actions">
                        <button type="submit" class="btn-save">Guardar</button>
                        <button type="button" id="cancel-btn" class="btn-cancel">Cancelar</button>
                    </div>
                </form>
            </div>
        `;

        const modal = document.createElement('div');
        modal.innerHTML = formHtml;
        document.body.appendChild(modal);

        modal.querySelector('#edit-member-form').addEventListener('submit', async (e) => {
            e.preventDefault();

            try {
                const formData = new FormData(e.target);
                const res = await fetch(`/api/members/${memberId}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(Object.fromEntries(formData.entries()))
                });

                if (res.ok) {
                    alert('Socio actualizado');
                    lwindow.location.reload();
                } else {
                    const errorData = await res.json();
                    alert('Error: ' + errorData.error);
                }
            } catch (error) {
                console.error("Error al enviar PUT:", error);
                alert("Error al actualizar el socio");
            }
        });
        // Cancel button:
        modal.querySelector('#cancel-btn').addEventListener('click', () => {
            modal.remove();
        });
    }
});
*/