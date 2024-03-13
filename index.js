// Function to generate the bracket
function generateBracket() {
    const regions = ['East', 'West', 'South', 'Midwest'];
    const bracket = {};
    for (let region of regions) {
        const regionTeams = [];
        for (let i = 1; i <= 16; i++) {
            regionTeams.push({ name: `${region} Team ${i}`, seed: i });
        }
        bracket[region] = { Round1: generateMatchups(regionTeams) };
    }
    console.log(bracket);
}

// Function to generate matchups for a round
function generateMatchups(teams) {
    const matchups = [];
    const numMatches = teams.length / 2;
    for (let i = 0; i < numMatches; i++) {
        matchups.push([teams[i], teams[teams.length - 1 - i]]);
    }
    return matchups;
}

// Call the generateBracket() function when the page loads
window.onload = generateBracket;
