// Creating dropdown for genre selection
function dropdown() {
    var selector = d3.selct('#selDataset'); //TAG FOR DATASET SELECTION

    //Using the data from the json file to populate the dashboard
    d3.json('data.json').then((data) => {
        var movieNames = data.title; //Let user select data based on title

        movieNames.forEach((title) => {
            selector
                .append("title")
                .text(title)
                .property("Value", title);
        });

        //Use first title in the list to build the initial plots on the webpage
        var firstTitle = movieNames[0];
        buildCharts(firstTitle); //MIGHT CHANGE
        buildMetadata(firstTitle); //MIGHT CHANGE
    });
}

//Initialize the dashboard
dropdown();

//Get new data whenever a new title is selected
function optionChanged(newTitle) {
    // Fetch new data each time a new sample is selected
    buildMetadata(newTitle);
    buildCharts(newTitle);
}

//Movie Information Panel
function buildMetadata(movieTitle) {
    d3.json("data.json").then((data) => {
      var movieID = data.movieid; //get movieID
      // Filter the data for the object with the desired sample number
      var resultArray = metadata.filter(sampleObj => sampleObj.id == sample); //INVESTIGATE
      var result = resultArray[0];
      // Use d3 to select the panel with id of `#sample-metadata`
      var PANEL = d3.select("#sample-metadata");
  
      // Use `.html("") to clear any existing metadata
      PANEL.html("");
  
      // Use `Object.entries` to add each key and value pair to the panel
      // Hint: Inside the loop, you will need to use d3 to append new
      // tags for each key-value in the metadata.
      Object.entries(result).forEach(([key, value]) => {
        PANEL.append("h6").text(`${key.toUpperCase()}: ${value}`);
      });
  
    });
  }