console.log("Bracket JavaScript file loaded.");

// Function to create a team
function createTeam(name, seed) {
    return {
        name: name,
        seed: seed
    };
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

// Function to generate teams for a region
function generateRegion(regionName) {
    const regionTeams = [];
    for (let i = 1; i <= 16; i++) {
        regionTeams.push(createTeam(regionName + ' Team ' + i, i));
    }
    return regionTeams;
}

// Function to generate the bracket
function generateBracket() {
    const regions = ['East', 'West', 'South', 'Midwest'];
    const bracket = {};
    for (let i = 0; i < regions.length; i++) {
        const regionName = regions[i];
        const regionTeams = generateRegion(regionName);
        bracket[regionName] = { Round1: generateMatchups(regionTeams) };
    }
    // Log the bracket object to the console
    console.log(bracket);
}

// Call the generateBracket() function when the page loads
window.onload = generateBracket;
