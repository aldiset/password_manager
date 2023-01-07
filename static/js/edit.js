function updateData(id) {
    var endpoint = `/account/update/${id}`
    fetch(endpoint, {
    method: 'PUT',
    body: JSON.stringify({
        name : document.getElementById("name"),
        username : document.getElementById("username"),
        password : document.getElementById("password")
    }),
    headers: {
        'Content-Type': 'application/json'
    }
    })
    .then(response => response.json())
    .then(data => {
    console.log(data); // menampilkan data yang diperbarui
    });
}