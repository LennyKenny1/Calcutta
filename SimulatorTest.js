// SimulatorTest.js
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
                row.forEach((cell, index) => {
                    var td = document.createElement('td');
                    if (index === COLUMN_INDEX_WITH_DROPDOWN) {
                        // If it's the column with dropdown, create select element
                        var select = document.createElement('select');
                        var options = cell.split('|'); // Assuming dropdown options are separated by '|'
                        options.forEach(option => {
                            var optionElement = document.createElement('option');
                            optionElement.textContent = option;
                            select.appendChild(optionElement);
                        });
                        td.appendChild(select);
                    } else {
                        td.textContent = cell;
                    }
                    tr.appendChild(td);
                });
                table.appendChild(tr);
            });
        })
        .catch(error => {
            console.error('Error fetching CSV:', error);
        });
});
