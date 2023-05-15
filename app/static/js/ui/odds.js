let selectedTeams = [];
let teams = [];
let currSearch = "";

function renderTeamsSelector (allTeams, trackedTeams) {
    teams = allTeams;
    let temp = [];
    console.log(trackedTeams);
    console.log(allTeams);
    for (let i = 0; i < trackedTeams.length; i++) {
        for (let j = 0; j < allTeams.length; j++) {
            if (trackedTeams[i].id === allTeams[j].id) {
                temp.push(allTeams[j]);
            }
        }
    }
    selectedTeams = temp;
    // This is a search bar, followed by a series of divs contained in the div specified by container.
    let containerDiv = document.getElementById('teamsContainer');
    // Wipe everything in the container div.
    containerDiv.innerHTML = "";

    // Create a div for the teams list.
    let teamsList = document.createElement("div");
    teamsList.setAttribute("id", "teamsList");
    // Append the teams list to the container div.
    containerDiv.appendChild(teamsList);

    // Render the teams list.
    renderTeamsList(teams, selectedTeams);
}

function renderTeamsList(teams, trackedTeams) {
    let containerDiv = document.getElementById('teamsList');
    // Wipe everything in the container div.
    containerDiv.innerHTML = "";
    // USe TailwindCSS to create a grid with 3 columns (2 for small screens).
    containerDiv.setAttribute("class", "my-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4");
    // For each team, create a div with the team's name and logo.
    trackedTeams.forEach(team => {
        let isTracked = trackedTeams.some(trackedTeam => trackedTeam.id === team.id);
        // This is done in a helper function.
        createTeamDiv('teamsList', team, isTracked);
    });

    // If there are no teams, display a message.
    if (teams.length === 0) {
        let noTeamsMessage = document.createElement("span");
        noTeamsMessage.innerHTML = "No teams found. Try changing your search.";
        noTeamsMessage.setAttribute("class", "text-white text-2xl font-bold");
        containerDiv.appendChild(noTeamsMessage);
    }
}

function createTeamDiv (listContainer, team, isTracked) {
    console.log("Creating team div for " + team.name + " in container " + listContainer);
    // This is a div with the team's name and logo.
    let teamsListContainerEl = document.getElementById(listContainer);
    // Create the div.
    let teamDiv = document.createElement("div");
    teamDiv.setAttribute("class", "p-8 border-2 rounded-lg border-white hover:border-blue-500 duration-300 ease-in-out");
    // Create the team name.
    let teamName = document.createElement("p");
    teamName.innerHTML = team.name;
    teamName.setAttribute("class", "text-center text-white text-2xl font-bold mb-4");
    // If the team is tracked, set the background to blue.
    if (isTracked) {
        teamDiv.setAttribute("class", "p-8 border-2 rounded-lg border-white hover:border-blue-500 bg-blue-500");
    }
    // Create the team logo.
    let teamLogo = document.createElement("img");
    teamLogo.setAttribute("src", team.imgUrl);
    // Use tailwind css to give it a standardized image size.
    teamLogo.setAttribute("class", "h-48 w-48 text-center m-auto");
    // Append the team name and logo to the div.
    teamDiv.appendChild(teamName);
    teamDiv.appendChild(teamLogo);
    // When teamDiv is clicked, toggle the team's tracked status by adding or removing its id from selectedTeams.
    teamDiv.addEventListener("click", () => {
        // if (isTracked) {
        //     console.log("Removing team " + team.name + " from selected teams.")
        //     // Remove the team from selectedTeams.
        //     selectedTeams = selectedTeams.filter(el => el.id !== team.id);
        //     // Set background color to none.
        //     teamDiv.setAttribute("class", "p-8 border-2 rounded-lg border-white hover:border-blue-500 duration-300 ease-in-out bg-none");
        // } else {
        //     console.log("Adding team " + team.name + " to selected teams.")
        //     // Add the team to selectedTeams.
        //     selectedTeams.push(team);
        //     // Set background color to blue.
        //     teamDiv.setAttribute("class", "p-8 border-2 rounded-lg border-white hover:border-blue-500 bg-blue-500 duration-300 ease-in-out");
        // }
        // Re-render the teams list.
        let filteredTeams = allTeams.filter(team => team.name.toLowerCase().includes(currSearch.toLowerCase()));
        renderTeamsList(filteredTeams, selectedTeams);
    });
    // Append the div to the container div.
    teamsListContainerEl.appendChild(teamDiv);
}