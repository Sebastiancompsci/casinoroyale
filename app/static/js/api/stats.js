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
async function setTrackedTeams(trackedTeams) {
    // Turn array of objects with ids into array of ids.
    trackedTeams = trackedTeams.map(team => team.id);

    // Set the tracked teams.
    const response = await fetch('/api/profile/tracked_teams', {
        method: 'POST', headers: {
            'Content-Type': 'application/json'
        }, body: JSON.stringify({ teams: trackedTeams })
    });

    // Parse the response.
    const data = await response.json();

    // If data.success is true, return true. Otherwise, return false.
    return data.success;
}