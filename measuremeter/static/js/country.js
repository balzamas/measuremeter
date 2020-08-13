     	var config_cases;
     	var config_death;
     	var avg_desc;
     	var avg_peak_desc;

      function LoadCountryData(country_id)
      {
          var data = $.ajax({
          url: "/measuremeterdata/countries/?pk="+country_id,
          dataType: "json",
          async: false
          }).responseText;
          var jsonData = JSON.parse(data);

          LoadMeasures(country_id);


          document.getElementById('worldometer').innerHTML = '<p><a href= "' + jsonData[0].link_worldometer + '" target="_blank">Link World-o-meter</a></p>';
          document.getElementById('gov').innerHTML = '<p><a href="' + jsonData[0].link_gov + '" target="_blank">Link Government</a></p>' ;
          if (Number(jsonData[0].average_death_per_day)>0)
          {
            $('#source_death').show();
            $('#deaths_description').show();
            avg_desc = "Deaths Average: " + jsonData[0].avg_desc +"";
            avg_peak_desc = "Deaths Peak: " + jsonData[0].avg_peak_desc+"";
            document.getElementById('source_death').innerHTML = "<p>Source total deaths: <a href='" + jsonData[0].source_death +"'> Link</a></p>";

          }
          else
          {
            $('#source_death').hide();
            $('#deaths_description').hide();
           }
          return [jsonData[0].average_death_per_day, jsonData[0].average_death_per_day_peak];
      }

      function LoadMeasures(country_id)
      {
            var d = new Date();
            today = formatDate(d);


          var data = $.ajax({
          url: "/measuremeterdata/measures/?country="+country_id.toString()+"&start="+today.replace('-', '\-')+"&end="+today.replace('-', '\-'),
          dataType: "json",
          async: false
          }).responseText;
          var jsonData = JSON.parse(data);

            var current_content = ''

            current_content +=`<div class="ui link cards">`
           $.each(jsonData, function(id, line) {
                if (line['level'] > 0)
                {
                    var tooltip = ''
                    var color_symbol = 'white'
                    if (line['level'] == 1 )
                    {
                        tooltip = line['type']['tooltip_partial']
                        color_symbol = 'orange'
                    }
                    else if (line['level'] == 2 )
                    {
                        tooltip = line['type']['tooltip_nonpartial']
                        color_symbol = 'red'
                    }

                    var start_str = line['start']
                    if (line['start'] == null)
                    {
                         start_str = 'undefined'
                    }

                    var end_str = line['end']
                    if (line['end'] == null)
                    {
                         end_str = 'undefined'
                    }

                    var details='';
                    if (line['comment'] != '')
                    {
                    details = `                        <div class="ui accordion">
                          <div class="active title">
                            <i class="dropdown icon"></i>
                            Details
                          </div>
                          <div class="active content">
                                                `+ line['comment'] +`
                          </div>
                          </div>`
                          }

                   current_content +=` <div class="card" style="min-width:420px">
                    <div class="content">
                      <div class="header"><font size='5em'>`+ line['type']['name'] +`</font></div>
                      <div class="meta">
                        <a><i class="ban big icon" style='color:`+ color_symbol +`'></i><font size='5em'>&nbsp;`+ tooltip +`</font></a>
                      </div>
                      <div class="description" >
                        <font size='5em'>`+ details +`</font>
                      </div>
                    </div>
                    <div class="extra content">

                      <span class="right floated">
                        `+ end_str +`
                      </span>
                      <span>
                        <i class="calendar alternate outline icon"></i>
                        `+ start_str +`
                      </span>
                      <span> until </span>
                      <span><br><font size='1rem'>Last updated: `+ line['updated'] +`</font></span>

                    </div></div>`


                }
                });

           current_content += '</div>'

          document.getElementById('current').innerHTML = current_content

      }

      function drawLineChart(country, avg_values, startdate, endate)
      {

          lastdate_x = formatDate(endate);
          firstdate_x = formatDate(startdate);

          var data = $.ajax({
          url: "/measuremeterdata/casesdeaths/?country="+country+"&date_after=2020-02-20&date_before="+lastdate_x,
          dataType: "json",
          async: false
          }).responseText;
          var jsonData = JSON.parse(data);

        var dataset_cases = new Array()
        var dataset_deaths = new Array()
        var label_array = new Array()

        var dataset_data_cases = new Array()
        var dataset_data_deaths = new Array()

        var dataset_data_total = new Array()
        var dataset_data_avg = new Array()
        var dataset_data_peak = new Array()

        rowsCases = new Array();
        rowsDeaths = new Array();

        $.each(jsonData, function(id, line) {

            label_array.push(line['date'])

            dataset_data_cases.push(line['cases']);

              if (Number(avg_values[0] > -1))
              {
                dataset_data_deaths.push(line['deaths']);
                dataset_data_total.push(line['deathstotal']);
                dataset_data_avg.push(Number(avg_values[0]));
                dataset_data_peak.push(Number(avg_values[1]));
              }
              else
              {
                dataset_data_deaths.push(line['deaths'])
              }
        });

        color = '#ff0000'
        dataset_cases.push({"label": "Cases", fill: false, backgroundColor: color, borderColor: color, data: dataset_data_cases})

        color = '#ff6600'
        dataset_deaths.push({"label": "Covid", fill: false, backgroundColor: color, borderColor: color, data: dataset_data_deaths})
        if (Number(avg_values[0] > 0))
        {
            color = '#0000ff'
            dataset_deaths.push({"label": "Total", fill: false, backgroundColor: color, borderColor: color, data: dataset_data_total})
            color = '#00ff00'
            dataset_deaths.push({"label": avg_desc, fill: false, backgroundColor: color, borderColor: color, data: dataset_data_avg})
            color = '#ff0000'
            dataset_deaths.push({"label": avg_peak_desc, fill: false, backgroundColor: color, borderColor: color, data: dataset_data_peak})


        }


            config_cases = {
                type: 'line',

                data: {
                    labels: label_array,
                    datasets: dataset_cases
                },
                options: {
                    legend:{display: true,labels:{fontSize:20}},
                    responsive: true,
                    title: {
                        display: true,
                        text: 'Positive tests',
                        fontSize: 25

                    },
                    tooltips: {
                        mode: 'index',
                        intersect: false,
                    },
                    hover: {
                        mode: 'nearest',
                        intersect: true
                    },
                    scales: {
                        x: {
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: 'Day'
                            }
                        },
                        y: {
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: 'Positive tests'
                            }
                        }
                    },
                    }
                    }

            annotations = new Array();
            if (avg_values[0] > 0)
            {
               console.log("......")
                annotations.push({
						type: 'line',
						mode: 'horizontal',
						scaleID: 'y-axis-0',
						value: avg_values[0],
						borderColor: 'blue',
						borderWidth: 2,
						label: {
							backgroundColor: 'red',
							content: avg_desc,
							fontSize: 19,
							enabled: true
						},
					})
				annotations.push({
						type: 'line',
						mode: 'horizontal',
						scaleID: 'y-axis-0',
						value: avg_values[1],
						borderColor: 'blue',
						borderWidth: 2,
						label: {
							backgroundColor: 'red',
							content: avg_peak_desc,
                            fontSize: 19,
							enabled: true
						},
					})

            }

            config_death = {
                type: 'line',

                data: {
                    labels: label_array,
                    datasets: dataset_deaths
                },
                options: {
                    legend:{display: true,labels:{fontSize:20}},
                    responsive: true,
                    title: {
                        display: true,
                        text: 'Deaths per day',
                        fontSize: 25

                    },
                    tooltips: {
                        mode: 'index',
                        intersect: false,
                    },
                    hover: {
                        mode: 'nearest',
                        intersect: true
                    },
                    scales: {
                        x: {
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: 'Day'
                            }
                        },
                        y: {
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: 'Covid deaths per day'
                            }
                        }
                    },
               //     annotation: {
				//	 annotations: annotations
				//}

                 }
            }
      }




      function LoadPanelsFiltered()
      {
            if ($('#countries_dd').dropdown('get value') != null)
            {
                avg_values = LoadCountryData($('#countries_dd').dropdown('get value'));
                var datesft = drawTimeline(2,$('#countries_dd').dropdown('get value'));
                drawLineChart($('#countries_dd').dropdown('get value'),avg_values, datesft[0], datesft[1]);

			    var ctx = document.getElementById('casesChart').getContext('2d');
			    window.myLine = new Chart(ctx, config_cases);

  			    var ctx = document.getElementById('deathChart').getContext('2d');
			    window.myLine = new Chart(ctx, config_death);
             }
      }

      $(window).on('load', function() {
         $("#countries_dd").change(function() {
               LoadPanelsFiltered()
            });

            $('.ui.accordion')
                 .accordion()
            ;

            $('#param').hide();

            if ($('#param').text() != '')
            {
                $('#countries_dd').dropdown('set selected',$('#param').text());
            }
            else
            {
                var rnd_country = Math.floor(Math.random() * 43) + 1;

                $('#countries_dd').dropdown('set selected',rnd_country);
            }
      });
