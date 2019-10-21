makeCharts = function (data) {

    var cancerData = data.filter(d => d.group == 'Cancer');
    var motorVehicleAccidentData = data.filter(d => d.group == 'Motor Vehicle Accident');
    var drugUseData = data.filter(d => d.group == 'Drug Use');
    var records = {
        $schema: 'https://vega.github.io/schema/vega-lite/v4.0.0-beta.10.json',
        transform: [
            {
                bin: { step: 5 },
                field: "age",
                as: "Age"
            }
        ],
        data: {
            values: data
        },
        mark: {
            type: "bar",
            tooltip: true
        },
        encoding: {
            x: {
                bin: { binned: true, step: 5 },
                field: "Age",
                type: "quantitative",
                title: "Age"
            },
            x2: { field: "Age_end" },
            y: {
                aggregate: "count",
                type: "quantitative"
            }
        },
        height: 300,
        width: 800

    };

    vegaEmbed('#vis', records);
    records.data.values = cancerData;
    vegaEmbed('#cancer', records);
    records.data.values = motorVehicleAccidentData;
    vegaEmbed('#mva', records);
    records.data.values = drugUseData;
    vegaEmbed('#drugs', records);
}
d3.csv('./death_causes.csv')
    .then(makeCharts);

makeUncertaintyChart = function (data) {
    var records = {
        $schema: 'https://vega.github.io/schema/vega-lite/v4.0.0-beta.10.json',
        data: {
            values: data.values
        },
        mark: {
            type: "bar",
            tooltip: true
        },
        encoding: {
            y: {
                field: "percentage",
                type: "quantitative",
            },
            x: {
                field: "name",
                type: "ordinal",
                sort: "-y",
                title: "Cause of Death",
                axis: { labelAngle: 0, labelFontSize: 8, labelOverlap: false }
            }
        },
        height: 300,
        width: data.values.length * 100
    };

    vegaEmbed('#response', records);
}

var slider = document.getElementById("age");
var output = document.getElementById("demo");
output.innerHTML = 'Age: ' + slider.value;



var apiCall = function () {

    var age = slider.value;
    var genderEle = document.getElementById('gender');
    var gender = genderEle.options[genderEle.selectedIndex].value;
    var ethnicityEle = document.getElementById('ethnicity');
    var ethnicity = ethnicityEle.options[ethnicityEle.selectedIndex].value;
    var mEle = document.getElementById('mstatus');
    var mstatus = mEle.options[mEle.selectedIndex].value;
    var eduEle = document.getElementById('education');
    var edu = eduEle.options[eduEle.selectedIndex].value;



    const Http = new XMLHttpRequest();
    const url = 'http://localhost:5000/deaths';
    var cat = [ethnicity, gender, mstatus, edu];
    var num = [age];
    var params = "cat=" + cat + "&num=" + num + "&";
    Http.open("POST", url, true);
    Http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    Http.send(params);

    Http.onreadystatechange = (e) => {
        var response = JSON.parse(Http.responseText);
        makeUncertaintyChart(response);
    }
}

slider.oninput = function () {
    output.innerHTML = 'Age: ' + this.value;
}

apiCall();