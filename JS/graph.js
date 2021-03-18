var months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
var rowTracker = {};
var colTracker = [];

top3();



function top3(){

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      top3input = JSON.parse(this.responseText)
      // console.log(JSON.parse(this.responseText));
      // console.log(Object.keys(top3input));
      header = {};
      header[0] = "Dates";
      n=1;
      for (i in Object.keys(top3input)){
        header[n] = Object.keys(top3input)[i];
        colTracker.push(Object.keys(top3input)[i]);
        n+=1;
        adddltrow(Object.keys(top3input)[i]);
      }
      body = [];
      // console.log(Object.values(header));
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var body = new Array(Object.values(header));
        addRowLabels(body,top3input);
        // console.log(body);
        window.data = google.visualization.arrayToDataTable(body);
        window.options = {
          title: 'Rules Matched',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        window.chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
        chart.draw(data, options);
      }
    }
  };
  xhttp.open("POST", "http://10.1.83.57:5000/api/entries/rules/top3", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send();

}

function graphrule(id){

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      end =data.getNumberOfColumns();
      update = JSON.parse(this.responseText);
      // console.log(update);
      data.insertColumn(end,'number',[update[0]]);
      colTracker.push(update[0]);
      adddltrow(update[0]);
      addcells(end,update[1]);
      chart.draw(data, options);
    }
  };
  xhttp.open("POST", "http://10.1.83.57:5000/api/entries/rules/graph", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("id="+id);
}

function addRowLabels(body,full){
  today = new Date();
  yesterday = new Date(today);
  var dateOffset = (24*60*60*1000)
  for(i=0;i<30;i++){
    yesterday.setTime(today.getTime()-(dateOffset*(30-i)));
    body.push([months[yesterday.getMonth()]+"-"+yesterday.getDate(),0,0,0]);
    rowTracker[months[yesterday.getMonth()]+"-"+yesterday.getDate()]=i;
  }
  counter = 1;
  for(i in full){
    for(ii in full[i]){
      // console.log(full[i][ii]["Date"]);
      // console.log(full[i][ii]["Count"]);
      compareDate = new Date(full[i][ii]["Date"]);
      if(today.getTime()-(dateOffset*30)<compareDate.getTime()){
        // console.log(months[compareDate.getMonth()]+"-"+compareDate.getDate());
        // console.log(body);
        // console.log(counter);
        // console.log(full[i][ii]["Count"]);
        body[rowTracker[months[compareDate.getMonth()]+"-"+compareDate.getDate()]][counter] =  full[i][ii]["Count"];
      }
    }

      counter+=1;
    }
  }

function addcells(y,update){
  today = new Date();
  var dateOffset = (24*60*60*1000)
  for(i=0;i<30;i++)
    data.setValue(i,y,0);

  for(i in update){
    compareDate = new Date(update[i]["Date"]);
    if(today.getTime()-(dateOffset*30)<compareDate.getTime()){
      data.setValue(rowTracker[months[compareDate.getMonth()]+"-"+compareDate.getDate()],y,update[i]["Count"]);
    }
  }

}

function adddltrow(input){
    document.getElementById("dlttable").innerHTML += '<div class="row dltRow" id=\"'+(colTracker.indexOf(input)+1)+'\"onclick=\'dltGraphpoint("'+input+'")\'>'+input+'</div>';
}

function dltGraphpoint(input){
    console.log(input);
    data.removeColumn(colTracker.indexOf(input)+1);
    $("#"+(colTracker.indexOf(input)+1)).remove();
    colTracker.splice(colTracker.indexOf(input),1);
    chart.draw(data, options);
}
