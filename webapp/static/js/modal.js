function showDeleteModal(){
    $('#deleteModal').modal();
}

function showLogoutModal() {
    $('#logoutModal').modal();
}

function doPost(url, token) {
    $.post(url, {'csrfmiddlewaretoken': token}, window.location.replace('/'));
}
