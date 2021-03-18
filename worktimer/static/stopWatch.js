//Define vars to hold time values
let seconds = 0;
let minutes = 0;
let hours = 0;

//Define vars to hold "display" value
let displaySeconds = 0;
let displayMinutes = 0;
let displayHours = 0;

//Define var to hold setInterval() function
let interval = null;

//Define var to hold stopwatch status
let status = "pause";

//Stopwatch function (logic to determine when to increment next value, etc.)
function stopWatch() {

    seconds++;

    //Logic to determine when to increment next value
    if (seconds / 60 === 1) {
        seconds = 0;
        minutes++;

        if (minutes / 60 === 1) {
            minutes = 0;
            hours++;
        }

    }

    //If seconds/minutes/hours are only one digit, add a leading 0 to the value
    if (seconds < 10) {
        displaySeconds = "0" + seconds.toString();
    }
    else {
        displaySeconds = seconds;
    }

    if (minutes < 10) {
        displayMinutes = "0" + minutes.toString();
    }
    else {
        displayMinutes = minutes;
    }

    if (hours < 10) {
        displayHours = "0" + hours.toString();
    }
    else {
        displayHours = hours;
    }

    //Display updated time values to user
    document.getElementById("display").innerHTML = displayHours + ":" + displayMinutes + ":" + displaySeconds;

}



function startPause() {

    if (status === "pause") {

        //Start the stopwatch (by calling the setInterval() function)
        interval = window.setInterval(stopWatch, 1000);
        document.getElementById("startPause").innerHTML = "Pause";
        status = "started";

    }
    else {

        window.clearInterval(interval);
        document.getElementById("startPause").innerHTML = "Start";
        status = "pause";

    }

    if (status === "started") {
        let stopBtn = document.getElementById("save");
        //Check if button stop not already created
        if (stopBtn == null) {
            //create a button for stop if stopwatch started
            var btn = document.createElement("button");
            btn.setAttribute("id", "save");
            btn.setAttribute("type", "button");
            btn.setAttribute("class", "btn btn-success");
            btn.innerHTML = "Save";
            //btn.addEventListener('click',storeTime)
            btn.onclick = storeTime;
            btn.setAttribute("data-toggle", "modal");
            btn.setAttribute("data-target", "#timeWorkedModal")
            var div = document.getElementsByClassName("saveDiv");
            div[0].appendChild(btn);
        }
    }
}


//store time in datatabase
function storeTime() {
    workTime = displayHours + ":" + displayMinutes + ":" + displaySeconds;
    var popUpText = document.getElementsByClassName("modal-body");
    popUpText[0].innerHTML = "<p id = 'modal-para'>" + workTime + "</p>";
    reset();

    $.ajax({
        type: "POST",
        contentType: "application/json;charset=utf-8",
        url: "/saveTime",
        traditional: "true",
        data: JSON.stringify({ workTime }),
        dataType: "json",
        success: function (response) {
            console.log(response);
            //window.location = 'http://127.0.0.1:5000/summary';
        },
        error: function (error) {
            console.log(error);
        }
    });
}


//Function to reset the stopwatch
function reset() {

    window.clearInterval(interval);
    seconds = 0;
    minutes = 0;
    hours = 0;
    document.getElementById("display").innerHTML = "00:00:00";
    document.getElementById("save").remove();
    document.getElementById("startPause").innerHTML = "Start";
    status = "pause";
}

//Convert time to H:M:S
$(document).ready(function () {
    $('#formTime').submit(function (e) {
        //var url = "{{ url_for('details.convertTime') }}"; // send the form data here.
        timeInput = $('#timeInput').val();
        $.ajax({
            type: "POST",
            contentType: "application/json;charset=utf-8",
            url: '/convertTime',
            traditional: "true",
            data: JSON.stringify({ timeInput }),
            dataType: "json",
            success: function (response) {
                $('#outputTime').attr('placeholder', response)
            },
            error: function (error) {
                console.log(error);
            }
        });
        e.preventDefault(); // block the traditional submission of the form.
    });
});
