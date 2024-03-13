// script.js
document.addEventListener('DOMContentLoaded', function () {
    var table = document.getElementById('data-table');

    // Fetch CSV file
    fetch('Simulator Test - Full Bracket.csv')
        .then(response => response.text())
        .then(text => {
            // Parse CSV data
            var rows = text.trim().split('\n').map(row => row.split(','));
            
            // Populate table with CSV data
            rows.forEach(row => {
                var tr = document.createElement('tr');
                row.forEach(cell => {
                    var td = document.createElement('td');
                    td.textContent = cell;
                    tr.appendChild(td);
                });
                table.appendChild(tr);
            });
        })
        .catch(error => {
            console.error('Error fetching CSV:', error);
        });
});
