window.addEventListener('load', () => {
    plot1 = document.getElementById('plot1');
    plot2 = document.getElementById('plot2');
    plot3 = document.getElementById('plot3');

    appointments_array_y = [1, 2, 15, 7, 5, 9, 10];
    financial_y = [4650, 2000, 2400, 800, 300, 1000, 2000];
  visits_y = [440, 567, 1000, 2345, 2000, 1000, 200];

    var trace1 = {
        x: [1,2,3,4,5,6,7],
        y: appointments_array_y,
        mode: 'lines+markers',
        name: 'Week Appointments',
        
        marker: {
            color: 'rgba(0,0,255,1)',
            size: 8
          },
          line: {
            color: 'rgba(0,0,255,0.5)',
            width: 1
          }
      };
      
      var trace2 = {
        x: [1,2,3,4,5,6,7],
        y: financial_y,
        mode: 'lines+markers',
        name: 'Week Appointments',
        
        marker: {
            color: 'rgba(123,217,52,1)',
            size: 8
          },
          line: {
            color: 'rgba(123,217,52,0.5)',
            width: 1
          }
      };

      var trace3 = {
        x: [1,2,3,4,5,6,7],
        y: visits_y,
        mode: 'lines+markers',
        name: 'Week Appointments',
        
        marker: {
            color: 'rgba(255,0,255,1)',
            size: 8
          },
          line: {
            color: 'rgba(255,0,255,0.5)',
            width: 1
          }
      };

      let max_dates_per_week = 20;
      let max_cash_per_week = 3000;
      let max_visits_per_week = 5000;

      var layout1 = {
        title:'Appointments',
        
        font: {
            family: 'Courier New, monospace',
            size: 18
        },

        xaxis: {
            fixedrange: true,
            autorange: true,
            range: [1,7],
            type: 'linear',

            title: {
                text: 'Date',
                font: {
                  family: 'Courier New, monospace',
                  size: 15,
                  color: '#7f7f7f'
                }
              },

          },
          yaxis: {
            fixedrange: true,
            autorange: true,
            range: [0, max_dates_per_week],
            type: 'linear',

            title: {
                text: 'Appointments',
                font: {
                  family: 'Courier New, monospace',
                  size: 15,
                  color: '#7f7f7f'
                }
              },

          }
      };

      var layout2 = {
        title:'Financial status',
        
        font: {
            family: 'Courier New, monospace',
            size: 18
        },

        xaxis: {
            fixedrange: true,
            autorange: true,
            range: [1,7],
            type: 'linear',

            title: {
                text: 'Date',
                font: {
                  family: 'Courier New, monospace',
                  size: 15,
                  color: '#7f7f7f'
                }
              },

          },
          yaxis: {
            fixedrange: true,
            autorange: true,
            range: [0, max_cash_per_week],
            type: 'linear',

            title: {
                text: 'Cash',
                font: {
                  family: 'Courier New, monospace',
                  size: 15,
                  color: '#7f7f7f'
                }
              },

          }
      };

      var layout3 = {
        title:'Visits',
        
        font: {
            family: 'Courier New, monospace',
            size: 18
        },

        xaxis: {
            fixedrange: true,
            autorange: true,
            range: [1,7],
            type: 'linear',

            title: {
                text: 'Date',
                font: {
                  family: 'Courier New, monospace',
                  size: 15,
                  color: '#7f7f7f'
                }
              },

          },
          yaxis: {
            fixedrange: true,
            autorange: true,
            range: [0, max_visits_per_week],
            type: 'linear',

            title: {
                text: 'Number of visits',
                font: {
                  family: 'Courier New, monospace',
                  size: 15,
                  color: '#7f7f7f'
                }
              },

          }
      };
      
      var defaultPlotlyConfiguration = {displayModeBar: false, responsive:true };

      Plotly.newPlot(plot1, [trace1], layout1, defaultPlotlyConfiguration);
      Plotly.newPlot(plot2, [trace2], layout2, defaultPlotlyConfiguration);
      Plotly.newPlot(plot3, [trace3], layout3, defaultPlotlyConfiguration);
      


});