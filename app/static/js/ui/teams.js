var trackTeam = document.getElementById("trackTeam")
trackTeam.innerText = 'track this team'

trackTeam.addEventListener('click',()=>{
    alert('Oh, you clicked me!')
})

function renderTeamsSelector (container, allTeams, trackedTeams) {
    // This is a search bar, followed by a series of divs contained in the div specified by container.
    let containerDiv = document.getElementById(container);
    // Wipe everything in the container div.
    containerDiv.innerHTML = "";
    // Create the search bar.
    let searchBar = document.createElement("input");
    searchBar.setAttribute("type", "text");
    searchBar.setAttribute("id", "teamSearchBar");
    searchBar.setAttribute("placeholder", "Search for a team...");
    // On change, render the teams list.
    searchBar.addEventListener("change", () => {
        let filteredTeams = allTeams.filter(team => team.name.toLowerCase().includes(searchBar.value.toLowerCase()));
        renderTeamsList('teamsList', filteredTeams, trackedTeams);
    });
    // Append the search bar to the container div.
    containerDiv.appendChild(searchBar);

    // Create a div for the teams list.
    let teamsList = document.createElement("div");
    teamsList.setAttribute("id", "teamsList");
    // Append the teams list to the container div.
    containerDiv.appendChild(teamsList);

    // Render the teams list.
    renderTeamsList('teamsList', allTeams, trackedTeams);
}

function renderTeamsList (container, teams, trackedTeams) {
    let containerDiv = document.getElementById(container);
    // Wipe everything in the container div.
    containerDiv.innerHTML = "";
    // For each team, create a div with the team's name and logo.
    teams.forEach(team => {
        let isTracked = trackedTeams.some(trackedTeam => trackedTeam.id === team.id);
        // This is done in a helper function.
        createTeamDiv(container, team, isTracked);
    });

    // If there are no teams, display a message.
    if (teams.length === 0) {
        let noTeamsMessage = document.createElement("p");
        noTeamsMessage.innerHTML = "No teams found. Add some to the database, in the teams table.";
        containerDiv.appendChild(noTeamsMessage);
    }
}

function createTeamDiv (container, team, isTracked) {
    // This is a div with the team's name and logo.
    let containerDiv = document.getElementById(container);
    // Create the div.
    let teamDiv = document.createElement("div");
    teamDiv.setAttribute("class", "teamDiv");
    // Create the team name.
    let teamName = document.createElement("p");
    teamName.innerHTML = team.name; 
    // Create the team logo.
    let teamLogo = document.createElement("img");
    teamLogo.setAttribute("src", team.imgUrl);
    teamLogo.setAttribute("class", "teamLogo");
    // Append the team name and logo to the div.
    teamDiv.appendChild(teamName);
    teamDiv.appendChild(teamLogo);
    // Append the div to the container div.
    containerDiv.appendChild(teamDiv);
}