$(".button-collapse").sideNav();
$('select').material_select();
$('.collapsible').collapsible();

$(document).ready(function() {
    var heights = $(".infoDiv").map(function() {
        return $(this).height();
    }).get(),

    maxHeight = Math.max.apply(null, heights);

    $(".infoDiv").height(maxHeight);

});
// using jQuery
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
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$('#add-amount-btn').on('click', function(event){
	event.preventDefault();
	increase();
})

function increase() {
    console.log("balance is working!") // sanity check
    $.ajax({
        url : "/statistics/all/ajax/", // the endpoint
        type : "POST", // http method
        data : { the_balance : $('#balance_in').val() }, // data sent with the post request
        
        success : function(json) {
            $('#balance_in').val('0.00'); // remove the value from the input
            var obj = $.parseJSON(json);
            $('#user-bal').html('Your balance: ' + obj['balance'])
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log("Error")
        }
    });
};

