fetch('historique_jeu.json')
    .then(response => response.json())
    .then(data => {
        const tbody = document.getElementById('historyTable').getElementsByTagName('tbody')[0];

        Object.entries(data.mains).forEach(([player, hand]) => {
            const row = tbody.insertRow();
            const carte_jouee = data.cartes_jouees.find(p => p.joueur === player)?.carte || 'No card played';
            const enchere = data.encheres.find(e => e.joueur === player)?.enchere || 'No bid';
            const evaluation = data.evaluations[player];
            const conseil = data.conseils[player];

            row.innerHTML = `<td>${player}</td>
                             <td>${hand.join(', ')}</td>
                             <td>${carte_jouee}</td>
                             <td>${enchere}</td>
                             <td>${evaluation}</td>
                             <td>${conseil}</td>`;
        });
    })
    .catch(error => console.error('Error loading the game history:', error));
