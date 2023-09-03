document.addEventListener("DOMContentLoaded", function() {
    const dashboardTab = document.getElementById("dashboardTab");

    dashboardTab.addEventListener("click", function() {
        const choice = prompt("Choose a page to navigate to: Feedback, Analytics, Process Mapping");

        switch (choice.toLowerCase()) {
            case "feedback":
                window.location.href = "feedback.html";
                break;
            case "analytics":
                window.location.href = "analytics.html";
                break;
            case "process mapping":
                window.location.href = "processMapping.html";
                break;
            default:
                alert("Invalid choice. Please try again.");
                break;
        }
    });
});
