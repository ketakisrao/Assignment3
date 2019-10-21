var makeUncertaintyChart = function (data, id) {
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

    vegaEmbed(id, records);
}

var slider = document.getElementById("age");
var output = document.getElementById("demo");
output.innerHTML = 'Age: ' + slider.value;



var apiCall = function (cat, num, id) {
    const Http = new XMLHttpRequest();
    const url = 'http://localhost:5000/deaths';

    var params = "cat=" + cat + "&num=" + num + "&";
    Http.open("POST", url, true);
    Http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    Http.send(params);

    Http.onreadystatechange = (e) => {
        var response = JSON.parse(Http.responseText);
        makeUncertaintyChart(response, id);
    }
}
var makeUncertaintyChart1 = function (data, id) {
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

    vegaEmbed(id, records);
}
var makeUncertaintyChart2 = function (data, id) {
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

    vegaEmbed(id, records);
}
var uncertainity = function (data, i, mainData) {
    switch (i) {
        case 0: makeUncertaintyChart(data, "#miles");
            break;
        case 1: makeUncertaintyChart1(data, "#jonas", mainData);
            break;
        case 2: makeUncertaintyChart2(data, "#alma");
            break;
    }
}


getPersonaPrediction = function (cat, num, i, mainData) {

    const url = 'http://localhost:5000/deaths';


    const Http = new XMLHttpRequest();
    Http.open("POST", url, true);
    Http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    var params = "cat=" + cat + "&num=" + num + "&";
    Http.send(params);

    Http.onreadystatechange = (e) => {
        var response = JSON.parse(Http.responseText);
        uncertainity(response, i, mainData);
    }
}


var getPrediction = function () {
    var age = slider.value;
    var genderEle = document.getElementById('gender');
    var gender = genderEle.options[genderEle.selectedIndex].value;
    var ethnicityEle = document.getElementById('ethnicity');
    var ethnicity = ethnicityEle.options[ethnicityEle.selectedIndex].value;
    var mEle = document.getElementById('mstatus');
    var mstatus = mEle.options[mEle.selectedIndex].value;
    var eduEle = document.getElementById('education');
    var edu = eduEle.options[eduEle.selectedIndex].value;

    var cat = [ethnicity, gender, mstatus, edu];
    var num = [age];
    apiCall(cat, num, "#response");
}


makeCharts = function (data) {

    var cancerData = data.filter(d => d.group == 'Cancer');
    var motorVehicleAccidentData = data.filter(d => d.group == 'Motor Vehicle Accident');
    var drugUseData = data.filter(d => d.group == 'Drug Use');
    var heartDiseaseData = data.filter(d => d.group == 'Heart Disease');
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

    var customChart = {
        $schema: "https://vega.github.io/schema/vega-lite/v4.0.0-beta.10.json",
        data: { values: data },
        transform: [
            { filter: "datum.group == 'Heart Disease' || datum.group == 'Cancer' || datum.group == 'Asthma' || datum.group == 'Drug Use'" },
            {
                bin: { step: 10 },
                field: "age",
                as: "Age",}
        ],
        mark: { type: "bar", tooltip: true },
        encoding: {
            column: {
                field: "Age", type: "ordinal", spacing: 10
            },
            y: {
                aggregate: "count", field: "age", type: "quantitative",
                // "axis": { "title": "age", "grid": false }
            },
            x: {
                field: "group", type: "nominal",
                "axis": { "title": "" }
            },
            color: {
                field: "group", type: "nominal",
                scale: { range: ["#003f5c", "#58508d", "#bc5090", "#ff6361"] }
            }
        },
        config: {
            view: { "stroke": "transparent" },
            axis: { "domainWidth": 1 }
        }
    }

    vegaEmbed('#vis', records);
    records.data.values = cancerData;
    vegaEmbed('#cancer', records);
    records.data.values = motorVehicleAccidentData;
    vegaEmbed('#mva', records);
    records.data.values = drugUseData;
    vegaEmbed('#drugs', records);
    vegaEmbed('#custom', customChart);

    var categorical = [['Black', 'M', 'Single', 6], ['White', 'M', 'Widowed', 3], ['Hawaiian', 'F', 'Married', 5]];
    var numeric = [[20], [72], [36]];
    for (i = 0; i < categorical.length; i++) {
        getPersonaPrediction(categorical[i], numeric[i], i, data);
    }
}
d3.csv('./death_causes.csv')
    .then(makeCharts);



slider.oninput = function () {
    output.innerHTML = 'Age: ' + this.value;
}

getPrediction();


