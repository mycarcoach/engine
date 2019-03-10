(function() {
  // Data visualization
  var ctx = document.getElementById("speedChart");
  var config = {
    type: "line",
    data: {
      labels: mockLabels,
      datasets: [
        {
          label: "Actual",
          // backgroundColor: 'red',
          borderColor: "red",
          //data: mockData.actual,
          fill: false,
          pointStyle: "line",
          pointRadius: 0
        },
        {
          label: "Optimal",
          fill: false,
          // backgroundColor: 'blue',
          borderColor: "blue",
          //data: mockData.optimal
          pointRadius: 0
        }
      ]
    },
    options: {
      responsive: true,
      title: {
        display: true,
        text: "How close are you to the optimal braking curve?",
        fontFamily: "'Ubuntu', sans-serif",
        fontSize: 20,
      },
      tooltips: {
        mode: "index",
        intersect: false
      },
      hover: {
        mode: "nearest",
        intersect: true
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
              fontSize: 20,
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
              lineWidth: 2,
            },
            ticks: {
              fontSize: 18,
              fontFamily: "'Ubuntu', sans-serif",
            },
            scaleLabel: {
              display: true,
              labelString: "Speed",
              fontSize: 24,
              fontFamily: "'Ubuntu', sans-serif",

            }
          }
        ]
      }
    }
  };

  window.speedChart = new Chart(ctx, config);

  // Web Socket
  var ws = new WebSocket("ws://127.0.0.1:7254/");
  console.log("Websocket connect started!");
  ws.onopen = function(event) {
    console.log("Connected successfully!")
  }
  ws.onerror = function(event) {
    console.log("Error occurred")
    console.log(event.data)
  }
  ws.onmessage = function(event) {
    console.log("Got new message")
    var data = JSON.parse(event.data);

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
      borderColor: "red",
      fill: false
    };

    var newIdealDataset = {
      data: optimalData,
      label: "Optimal",
      borderColor: "blue",
      fill: false
    };

    config.data.labels = labels;
    config.data.datasets = [newActualDataset, newIdealDataset];
    window.speedChart.update();
  };
})();
