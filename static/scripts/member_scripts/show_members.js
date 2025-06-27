// static/scripts/member_scripts/show_members.js:

// Show all members if we are in the correspondent view:

document.addEventListener("DOMContentLoaded", async function () {
    const membersTable = document.querySelector("#membersTable");
    if (!membersTable) return; // If we are not on the members list page, exit.

    try {
        const response = await fetch("/api/members/all");
        if (!response.ok) {
            console.error("Error en la respuesta HTTP:", response.status);
            showMessage("Error al obtener los datos de los socios.", false);
            return;
        }
        const members = await response.json();
        console.debug("Datos recibidos:", members);
        // Log the raw response from the server for debugging purposes:
        console.log("Respuesta cruda del servidor:", members);

        const tbody = membersTable.querySelector("tbody");
        tbody.innerHTML = ""; // Clear existing rows.

        if (!response.ok) {
            console.error("Error en la respuesta HTTP:", response.status);
            showMessage("Error al obtener los datos de los socios.", false);
            return;
        }

        if (!Array.isArray(members)) {
            console.error("Respuesta inesperada: no es un array", members);
            showMessage("Error: los datos recibidos no son válidos.", false);
            return;
        }

        members.forEach(member => {
            const row = document.createElement("tr");

            const pamiDisplay = member.pami_number ? member.pami_number : "NO AFILIADO";
            const birthDate = member.birth_date ? member.birth_date.split('T')[0] : "";
            const joinDate = member.join_date ? member.join_date.split('T')[0] : "";

            row.innerHTML = `
                <td>${member.dni}</td>
                <td>${member.last_name}</td>
                <td>${member.first_names}</td>
                <td>${pamiDisplay}</td>
                <td>${birthDate}</td>
                <td>${member.phone}</td>
                <td>${member.email}</td>
                <td>${member.address}</td>
                <td>${member.status}</td>
                <td>${joinDate}</td>
             <td>
                    <button class="edit-member-btn" data-id="${member.id}">Editar</button>
                    <button class="delete-person-btn" data-id="${member.id}" data-kind="member">Eliminar</button>
            </td>`;

            tbody.appendChild(row);
        });

        // Handle events for Edit buttons:
        document.querySelectorAll(".edit-member-btn").forEach(btn => {
            btn.addEventListener("click", (e) => {
                e.preventDefault();
                const memberId = e.currentTarget.dataset.id;
                console.log(`Editando socio ID: ${memberId}`);

                // Redirection to edit page:
                window.location.href = `/api/members/editar_socio/${memberId}`;
            });
        });

        // Handle events for Delete buttons:
        document.addEventListener('click', async (event) => {
            if (event.target.classList.contains('delete-person-btn')) {
                const memberId = event.target.dataset.id;        
                if (!confirm("¿Estás segura/o de que querés eliminar este socio?")) return;
                try {
                    const response = await fetch(`/api/persons/delete_person/member/${memberId}`, {
                        method: 'PATCH'
                    });
                    const result = await response.json();
                    if (response.ok) {
                        window.location.href = "/api/members/ver_socios";
                        // Show success message:
                        showMessage("Socio eliminado correctamente", true);
                        setTimeout(() => {
                            window.location.href = "/api/members/ver_socios";
                        }, 3000); // Wait 3 seconds before reloading/redirecting.

                    }
                    else {
                        showMessage("Error: " + (result.error || "No se pudo eliminar."), false);
                    }
                } catch (error) {
                    console.error("Error en la eliminación:", error);
                    showMessage("Error: " + (error.message || "Error de red o del servidor."), false);
                }
            }
        });


    } catch (error) {
        // alert("Error al obtener los datos de los socios: " + error.message);
                console.error("Error al cargar socios:", error);

        // Show error message in the UI:
        const errorContainer = document.createElement("div");
        errorContainer.className = "alert alert-danger";
        errorContainer.textContent = 
            "Error al cargar la lista de socios. Por favor recarga la página.";
        
        membersTable.parentNode.insertBefore(
            errorContainer, 
            membersTable.nextSibling
        );
    }
});