function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


$(document).ready(function () {
    var csrftoken = getCookie('csrftoken');
    $('a.answer').click(function (event) {
        console.log($(this).data('id'));
        id = $(this).data('id');
        vote = $(this).data('vote');
        $.ajax({
                beforeSend: function (xhr, settings) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
                type: 'POST',
                data: {'vote': vote},
                url: '/vote/answer/' + id + '/',
                error: function (xhr, status, exception) {
                    var msg = '';
                    if (xhr.status === 0) {
                        msg = 'Not connect.\n Verify Network.';
                    } else if (xhr.status === 404) {
                        msg = 'Requested page not found. [404]';
                    } else if (xhr.status === 500) {
                        msg = 'Internal Server Error [500].';
                    } else if (exception === 'parsererror') {
                        msg = 'Requested JSON parse failed.';
                    } else if (exception === 'timeout') {
                        msg = 'Time out error.';
                    } else if (exception === 'abort') {
                        msg = 'Ajax request aborted.';
                    } else {
                        msg = 'Uncaught Error.\n' + xhr.responseText;
                    }
                    //$('#post').html(msg);
                }
            }
        );
    });
});