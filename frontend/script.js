fetch("/api/users")
    .then(response => response.json())
    .then(users => {
        const table = document.getElementById("users");

        users.forEach(user => {
            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${user.id}</td>
                <td>${user.name}</td>
                <td>${user.role}</td>
            `;

            table.appendChild(row);
        });
    })
    .catch(error => {
        console.error("Error:", error);
    });
