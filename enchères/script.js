document.addEventListener('DOMContentLoaded', function() {
    fetch('enchere_data.json')
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById('enchereTable');
        const table = document.createElement('table');
        let header = table.createTHead();
        let headerRow = header.insertRow(0);
        let headers = ["Phase", "Enchères"];
        headers.forEach(text => {
            let cell = headerRow.insertCell();
            cell.outerHTML = `<th>${text}</th>`;  // Ajouter des en-têtes au tableau
        });

        let tbody = table.createTBody();

        data.enchere.forEach((item, index) => {
            let row = tbody.insertRow();
            let phaseCell = row.insertCell();
            phaseCell.innerHTML = item.nom;  // Nom de la phase
            let bidsCell = row.insertCell();
            bidsCell.innerHTML = item.encheres.join(", ");  // Liste des enchères par phase
        });

        // Ajouter une ligne pour l'enchère gagnante
        if (data["enchere gagnante"]) {
            let gagnanteRow = tbody.insertRow();
            let gagnanteCell = gagnanteRow.insertCell();
            gagnanteCell.colSpan = 2;  // Fusionner les cellules pour une meilleure visibilité
            gagnanteCell.innerHTML = `<strong>Enchère gagnante:</strong> ${data["enchere gagnante"]} (Position: ${data['Liste des cartes detecter au total'].indexOf(data["enchere gagnante"]) + 1})`;
        }

        container.appendChild(table);
    })
    .catch(error => console.error('Erreur lors du chargement des données:', error));
});
