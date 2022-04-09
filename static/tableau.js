// Place to hold the dash
const vizContainer = document.getElementById('vizContianer');


//URL for the automatic sized dash
const autoURL = "https://public.tableau.com/views/MoviesRecommendations_16489231970320/DashboardOverview2?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link";

let viz;
const options = {
    height: 1000,
    width: 1200,
    onFirstInteractive: () => {
        console.log('Viz Loaded!');
    },
};

//When page loads we want to see the dash
function initViz(){
    viz = new tableau.Viz(vizContainer,autoURL,options);
}

document.addEventListener("DOMContentLoaded", initViz());