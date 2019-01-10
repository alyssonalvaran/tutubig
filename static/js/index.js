var data = {
    labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    datasets: [{
        label: 'Label',
        data: [12, 19, 3, 5, 2, 3],
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
        ],
        borderColor: [
            'rgba(255,99,132,1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1
    }]
};

var options = {
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero:true
            }
        }]
    },
    title: {
        display: true,
        text: 'Title'
    }
};

var ctx = document.getElementById("myLineChart").getContext('2d');
var myLineChart = new Chart(ctx, {
    type: 'line',
    data: data,
    options: options
});

var ctx = document.getElementById("myBarChart").getContext('2d');
var myLineChart = new Chart(ctx, {
    type: 'bar',
    data: data,
    options: options
});

var ctx = document.getElementById("myRadarChart").getContext('2d');
var myLineChart = new Chart(ctx, {
    type: 'radar',
    data: data,
    options: options
});

var ctx = document.getElementById("myPieChart").getContext('2d');
var myPieChart = new Chart(ctx,{
    type: 'pie',
    data: data,
    options: options
});

var ctx = document.getElementById("myPolarAreaChart").getContext('2d');
var myPolarAreaChart = new Chart(ctx,{
    type: 'polarArea',
    data: data,
    options: options
});

var ctx = document.getElementById("myBubbleChart").getContext('2d');
var myBubbleChart = new Chart(ctx,{
    type: 'bubble',
    data: data,
    options: options
});

var ctx = document.getElementById("myScatterChart").getContext('2d');
var myPolarAreaChart = new Chart(ctx,{
    type: 'myScatterChart',
    data: data,
    options: options
});