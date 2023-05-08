let allTeams = null;
let trackedTeams = null;

// Fetch list of all teams.
(async () => {
    // Fetch all teams.
    try {
        allTeams = await getTeams();
    } catch (err) {
        console.log(err.stack);
        errorNotification("Something went wrong while fetching all teams. Please try again later or check console for more details.");
    }

    // Fetch tracked teams.
    try {
        trackedTeams = await getTrackedTeams();
    } catch (err) {
        console.log(err.stack);
        errorNotification("Something went wrong while fetching tracked teams. Please try again later or check console for more details.");
    }

    // If both are fetched, send a success notification.
    if (allTeams && trackedTeams) {
        successNotification("Successfully fetched all teams.");
    }

    // Now render the teams list.
    renderTeamsList('teamsContainer', allTeams, trackedTeams);
})();