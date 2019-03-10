(function() {

  // Data visualization
  var ctx = document.getElementById("speedChart");
  var config = {
    type: "line",
    data: {
      labels: [],
      datasets: []
    },
    options: {
      responsive: true,
      title: {
        display: true,
        text: "Instant Feedback",
        fontFamily: "'Ubuntu', sans-serif",
        fontSize: 36,
        fontColor: "white",
      },
      tooltips: {
        mode: "index",
        intersect: false
      },
      hover: {
        mode: "nearest",
        intersect: true
      },
      legend: {
        labels: {
          fontSize: 16,
          fontFamily: "'Ubuntu', sans-serif",
          fontColor: "white",
        }
      },
      scales: {
        xAxes: [
          {
            display: true,
            gridLines: {
              display: false,
            },
            scaleLabel: {
              display: true,
              labelString: "Time",
              fontSize: 30,
              fontColor: "white",
        fontFamily: "'Ubuntu', sans-serif",
            },
            ticks: {
              display: false,
            },
          }
        ],
        yAxes: [
          {
            display: true,
            gridLines: {
              display: false,
              lineWidth: 2,
              color: "#efefef",
            },
            ticks: {
              display: false,
              fontSize: 18,
              fontFamily: "'Ubuntu', sans-serif",
              fontColor: "white",
            },
            scaleLabel: {
              display: true,
              labelString: "Acceleration",
              fontSize: 30,
              fontColor: "white",
              fontFamily: "'Ubuntu', sans-serif",

            }
          }
        ]
      }
    }
  };

  window.speedChart = new Chart(ctx, config);

  var timer = 10;
  var hasData = false;

  // Web Socket
  var ws = new WebSocket("ws://127.0.0.1:7254/");
  console.log("Websocket connect started!");

  ws.onopen = function(event) {
    console.log("Connected successfully!");
  }
  ws.onerror = function(event) {
    console.log("Error occurred");
    console.log(event.data);
  }
  ws.onmessage = function(event) {
    console.log("Got new message");
    var data = JSON.parse(event.data);
    hasData = true;
    window.setTimeout(() => { hasData = false; console.log('time is over'); }, 10000);

    var optimalData = [];
    var actualData = [];
    var labels = [];
    for (var i = 0; i < Object.keys(data.optimal).length; i++) {
        labels.push(i);
        optimalData.push(data.optimal[i]);
        actualData.push(data.actual[i]);
    }

    var newActualDataset = {
      data: actualData,
      label: "Actual",
      borderColor: "#282078",
      fill: false,
      pointRadius: 0,
      borderWidth: 5,
    };

    var newIdealDataset = {
      data: optimalData,
      label: "Optimal",
      borderColor: "#e4e4e4",
      fill: false,
      pointRadius: 0,
      borderWidth: 5,
      borderDash: [10, 3],
    };

    config.data.labels = labels;
    config.data.datasets = [newActualDataset, newIdealDataset];
    window.speedChart.update();
  };
})();
