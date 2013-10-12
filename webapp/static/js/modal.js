function showModal(){
    $('#deleteModal').modal();
}

function deleteQuote(url, token) {
    $.post(url, {'csrfmiddlewaretoken': token}, window.location.replace('/'));
}