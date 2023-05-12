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
    // Create the search bar.
    let searchBar = document.createElement("input");
    searchBar.setAttribute("type", "text");
    searchBar.setAttribute("id", "teamSearchBar");
    searchBar.setAttribute("placeholder", "Search for a team...");
    searchBar.setAttribute("class", "w-full mt-8 border-2 border-white hover:border-blue-500 focus:border-blue-500 focus:outline-none rounded-md px-4 py-2 mb-4 duration-300 ease-in-out bg-transparent bg-none text-white focus:text-blue-500 hover:text-blue-500");
    // On change, render the teams list.
    searchBar.addEventListener("input", () => {
        let filteredTeams = allTeams.filter(team => team.name.toLowerCase().includes(searchBar.value.toLowerCase()));
        currSearch = searchBar.value;
        renderTeamsList(filteredTeams, trackedTeams);
    });
    // Append the search bar to the container div.
    containerDiv.appendChild(searchBar);

    // Create a div for the teams list.
    let teamsList = document.createElement("div");
    teamsList.setAttribute("id", "teamsList");
    // Append the teams list to the container div.
    containerDiv.appendChild(teamsList);

    // Render the teams list.
    renderTeamsList(teams, selectedTeams);

    // Add a save button, which will create an api request (assume we can call "setTrackedTeams(selectedTeams)"
    let saveButton = document.createElement("button");
    saveButton.setAttribute("class", "bg-white hover:bg-blue-500 text-black font-bold py-2 px-4 rounded duration-300 ease-in-out m-auto text-center");
    saveButton.innerHTML = "Save team selection";
    saveButton.addEventListener("click", () => {
        setTrackedTeams(selectedTeams).then(r => {
            if (r) {
                successNotification("Successfully saved team selection.")
            } else {
                errorNotification("Failed to save team selection. Check console for more details.")
            }
        });
    });
    containerDiv.appendChild(saveButton);
}
function renderTeamsList(teams, trackedTeams) {
    let containerDiv = document.getElementById('teamsList');
    // Wipe everything in the container div.
    containerDiv.innerHTML = "";
    // USe TailwindCSS to create a grid with 3 columns (2 for small screens).
    containerDiv.setAttribute("class", "my-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4");
    // For each team, create a div with the team's name and logo.
    teams.forEach(team => {
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