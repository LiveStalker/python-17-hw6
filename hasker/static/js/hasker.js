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
        $.ajax({
                beforeSend: function (xhr, settings) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
                type: 'POST',
                url: '/vote/answer/' + id + '/'
            }
        );
    });
});