// variable for data file 
var UFO_table = data;


// variable to select tbody in html
var tbody = d3.select("tbody");


// function one 
function pull_data(aliens) {
    tbody.html("");
    console.log(aliens);
    aliens.forEach(function(appending) {
        tbody.append("tr");
        Object.entries(appending).forEach(function([key, value]) {
            tbody.append("td").text(value);
        })
    })
}


//function two 
function filt_data() {
    d3.event.preventDefault();
    var filtered_data = UFO_table;
    // console.log("UFO Sightings");
    var date_input = d3.select("#datetime").property("value");
    console.log(date_input);
    if (date_input) {
        filtered_data = filtered_data.filter(temporary_row => temporary_row.datetime === date_input);
    }
    pull_data(filtered_data);
    console.log(filtered_data);
}

pull_data(UFO_table)

d3.selectAll("#filter-btn").on("click", 

