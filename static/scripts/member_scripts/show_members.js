// static/scripts/member_scripts/show_members.js

document.addEventListener("DOMContentLoaded", async function () {
    const membersTable = document.querySelector("#membersTable");
    if (!membersTable) return;

    const kind = "member";
    const urlParams = new URLSearchParams(window.location.search);
    const status = urlParams.get("status") || "ACTIVO";

    const titleMap = {
        "ACTIVO": "SOCIOS ACTIVOS:",
        "SUSPENDIDO": "SOCIOS SUSPENDIDOS:",
        "ELIMINADO": "SOCIOS ELIMINADOS:"
    };
    const titleElement = document.getElementById("members-title");
    if (titleElement) {
        titleElement.textContent = titleMap[status] || "LISTADO DE SOCIOS:";
    }

    try {
        const response = await fetch(`/api/persons/all/${kind}?status=${status}`);
        if (!response.ok) {
            showMessage("Error al obtener los datos de los socios.", false);
            return;
        }

        const members = await response.json();
        const tbody = membersTable.querySelector("tbody");
        tbody.innerHTML = "";

        if (!Array.isArray(members)) {
            showMessage("Error: los datos recibidos no son válidos.", false);
            return;
        }

        members.forEach(member => {
            const pamiDisplay = member.pami_number || "NO AFILIADO";
            const birthDate = member.birth_date?.split('T')[0] || "";
            const joinDate = member.join_date?.split('T')[0] || "";

            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${member.dni}</td>
                <td>${member.last_name}</td>
                <td>${member.first_names}</td>
                <td>${pamiDisplay}</td>
                <!-- <td>${birthDate}</td> -->
                <td>${member.phone}</td>
                <td>${member.email}</td>
                <td>${member.address}</td>
                <!-- <td>${joinDate}</td> -->
                <td>
                    <button class="edit-member-btn" data-id="${member.id}" title="Editar">
                        <i class="fas fa-pen"></i>
                    </button>
                    <button class="delete-person-btn" data-id="${member.id}" data-kind="member" title="Eliminar">
                        <i class="fas fa-trash"></i>
                    </button>
                </td>
            `;
            tbody.appendChild(row);
        });

        // Edit buttons:
        document.querySelectorAll(".edit-member-btn").forEach(btn => {
            btn.addEventListener("click", (e) => {
                e.preventDefault();
                const memberId = e.currentTarget.dataset.id;
                window.location.href = `/api/members/editar_socio/${memberId}`;
            });
        });

    } catch (error) {
        console.error("Error al cargar socios:", error);
        const errorContainer = document.createElement("div");
        errorContainer.className = "alert alert-danger";
        errorContainer.textContent = "Error al cargar la lista de socios. Por favor recargá la página.";
        membersTable.parentNode.insertBefore(errorContainer, membersTable.nextSibling);
    }
});

// ✅ Listen for the delete button globally and reuse:
document.addEventListener("click", async function (event) {
    const button = event.target.closest(".delete-person-btn");
    if (!button) return;

    const personId = button.dataset.id;
    const kind = button.dataset.kind;

    showConfirmation("¿Estás segura/o de que querés eliminar este socio?", async () => {
    // Proceed with deletion:
    try {
        const response = await fetch(`/api/persons/delete_person/${kind}/${personId}`, {
            method: 'PATCH'
        });

        const result = await response.json();

        if (response.ok) {
            showMessage("Socio eliminado correctamente", true);
            setTimeout(() => {
                window.location.reload();  // Refresh the current view.
            }, 4000);
        } else {
            showMessage("Error: " + (result.error || "No se pudo eliminar."), false);
        }

        } catch (error) {
            console.error("Error en la eliminación:", error);
            showMessage("Error: " + (error.message || "Error de red o del servidor."), false);
        }
    });
});
