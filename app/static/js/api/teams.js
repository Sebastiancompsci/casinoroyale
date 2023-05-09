// Profile API wrapper.

async function getTeams() {
    // Get the teams.
    const response = await fetch('/api/teams', {
        method: 'GET', headers: {
            'Content-Type': 'application/json'
        }
    });

    // Parse the response.
    const data = await response.json();

    // Return the teams list. This is found in data.teams.
    return data.teams;
}

async function getTrackedTeams() {
    // Get the tracked teams.
    const response = await fetch('/api/profile/tracked_teams', {
        method: 'GET', headers: {
            'Content-Type': 'application/json'
        }
    });

    // Parse the response.
    const data = await response.json();

    // Return the tracked teams list. This is found in data.teams.
    return data.teams;
}