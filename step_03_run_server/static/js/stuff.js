$( document ).ready(function() {
    console.log( "ready!" );



    function getBotResponse() {
        var rawText = $("#textInput").val();
        var userHtml = '<p class="userText"><span>' + rawText + '</span></p>';

        $("#textInput").val("");
        $("#chatbox").append(userHtml);

        document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});

        $.get("/get", { msg: rawText }).done(function(data) {
            var response = data.response;
            var serverlog = data.serverlog;
            var botHtml = '<p class="botText"><span>' + response + '</span></p>';

            console.log("response: " +response);
            console.log("serverlog: " +serverlog);

            $("#chatbox").append(botHtml);
            $("#serverlog").html(serverlog);

            document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
            $('#chatbox').scrollTop($('#chatbox')[0].scrollHeight);

        });
    }

    $("#textInput").keypress(function(e) {
        if(e.which == 13) {
            getBotResponse();
        }
    });

    $("#buttonInput").click(function() {
        getBotResponse();
    })

});


