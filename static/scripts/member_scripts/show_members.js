// Show all members if we are in the correspondent view:

document.addEventListener("DOMContentLoaded", async function () {
    const membersTable = document.querySelector("#membersTable");
    if (!membersTable) return; // If we are not on the members list page, exit.

    try {
        const response = await fetch("/api/members/all");
        const members = await response.json();

        // Log the raw response from the server for debugging purposes:
        console.log("Respuesta cruda del servidor:", members);
        const tbody = membersTable.querySelector("tbody");

        if (!response.ok) {
            console.error("Error en la respuesta HTTP:", response.status);
            alert("No se pudieron obtener los datos de los socios.");
            return;
        }

        if (!Array.isArray(members)) {
            console.error("Respuesta inesperada: no es un array", members);
            alert("Error: los datos recibidos no son válidos.");
            return;
        }

        members.forEach(member => {
            const row = document.createElement("tr");

            const pamiDisplay = member.pami_number ? member.pami_number : "No es afiliado de PAMI";

            row.innerHTML = `
                <td>${member.dni}</td>
                <td>${member.first_names}</td>
                <td>${member.last_name}</td>
                <td>${pamiDisplay}</td>
                <td>${member.birth_date || ""}</td>
                <td>${member.phone}</td>
                <td>${member.email}</td>
                <td>${member.address}</td>
                <td>${member.status}</td>
                <td>${member.join_date || ""}</td>
            `;

            tbody.appendChild(row);
        });

    } catch (error) {
        alert("Error al obtener los datos de los socios: " + error.message);
    }
});
