function getData(){
  ajaxGetRequest("/barChart_graph",plotBar);
  ajaxGetRequest("/pieChart_graph",plotpie);
}

function plotpie(list){
  let data = JSON.parse(list);
  let piedata = [
  {
    values: Object.values(data),
    labels: Object.keys(data),
    type: 'pie'
  }
];

let layout = {
  height: 400,
  width: 500
};

Plotly.newPlot('pieGraph', piedata, layout);

  
}

function plotBar(list){
  let data = JSON.parse(list);
  let plotData = [
  {
    x: Object.keys(data),
    y: Object.values(data),
    type: 'bar'
  }
];

Plotly.newPlot('barGraph', plotData);
  
}

function plotLine(response){
let data = JSON.parse(response);
  
let trace1 = {
  x: Object.keys(data),
  y: Object.values(data),
  mode: 'lines+markers'
};

let variable = [trace1];

let layout = {
  title:'# of incidents ' + document.getElementById("hour")["value"] + " hundred hours"
};

Plotly.newPlot('lineGraph', variable, layout);
}


function getHourData(){
  hrId = document.getElementById("hour");
  hr = hrId["value"];
  dict = {"key" : hr};
  str = JSON.stringify(dict);
  console.log(str);
  ajaxPostRequest("/hour",str,plotLine);
}
