function checkAdmin() {
    console.log("Function called");  // Debugging line
    const username = document.getElementById('username').value;
    console.log("Username: ", username);  // Debugging line
    
    if (username === "admin") {
        window.location.href = "admin.html";  // Replace 'nextPage.html' with the actual page you want to navigate to
    }
}
