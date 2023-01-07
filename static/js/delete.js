function deleteData(id) {
    if (confirm("Apakah Anda yakin ingin menghapus data ini?")) {
      // Fetch the delete endpoint from the data attribute
      var endpoint = `/account/delete/${id}`
      // Send a DELETE request to the endpoint
      fetch(endpoint, {
        method: "GET"
      })
        .then(response => {
          // If the response is successful, refresh the page
          if (response.ok) {
            window.location.reload();
          }
        })
        .catch(error => {
          console.error("Error:", error);
        });
    }
  }
  