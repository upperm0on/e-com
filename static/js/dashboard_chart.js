// Load the Google Charts library
google.charts.load('current', {'packages':['line']});

// Set a callback function to run when the Google Charts library is loaded
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    try {
        // Get the JSON data passed from Django
        var dataElement = document.getElementById('revenue-data');
        if (!dataElement) {
            throw new Error('Data element not found');
        }

        var data = JSON.parse(dataElement.textContent);

        // Check if data is valid
        if (!Array.isArray(data)) {
            throw new Error('Data is not in the expected format');
        }

        // Prepare data in the format Google Charts expects
        var chartData = [['Month', 'Revenue']];
        data.forEach(function(item) {
            if (item && item.month && item.value !== undefined) {
                chartData.push([item.month, item.value]);
            } else {
                console.warn('Invalid data item:', item);
            }
        });

        // Create the DataTable object
        var dataTable = new google.visualization.DataTable();
        dataTable.addColumn('string', 'Month');  // Month as string
        dataTable.addColumn('number', 'Revenue'); // Revenue as number
        dataTable.addRows(chartData.slice(1));    // Skip header row

        // Set chart options
        var options = {
            chart: {
                title: 'Monthly Revenue',
                subtitle: 'Revenue by Month'
            },
            width: 900,
            height: 500,
            hAxis: {
                title: 'Month',
                slantedText: true, // Rotate month labels for better readability
                slantedTextAngle: 45
            },
            vAxis: {
                title: 'Revenue'
            }
        };

        // Instantiate and draw the chart
        var chart = new google.charts.Line(document.getElementById('chart_div'));
        chart.draw(dataTable, google.charts.Line.convertOptions(options));
    } catch (error) {
        // Handle and log errors
        console.error('An error occurred while drawing the chart:', error);
        document.getElementById('chart_div').innerHTML = '<p>Chart could not be rendered. Please try again later.</p>';
    }
}

 google.charts.load('current', {'packages':['corechart']});
  google.charts.setOnLoadCallback(drawChart);

  function drawChart() {
    var dataElement = document.getElementById('category-revenue-data');
    var data = JSON.parse(dataElement.textContent);
    // Prepare data in the format Google Charts expects

    var data = google.visualization.arrayToDataTable([['Category', 'Revenue']];
    data.forEach(function(item) {
        if (item && item.category && item.value !== undefined) {
            chartData.push([item.category, item.value]);
        } else {
            console.warn('Invalid data item:', item);
        }
    });

    var data = google.visualization.arrayToDataTable([
      ['Category', 'Revenue'],
      ['Work',     11],
      ['Eat',      2],
      ['Commute',  2],
      ['Watch TV', 2],
      ['Sleep',    7]
    ]);

    var options = {
      title: 'My Daily Activities'
    };

    var chart = new google.visualization.PieChart(document.getElementById('piechart'));

    chart.draw(data, options);
  }
