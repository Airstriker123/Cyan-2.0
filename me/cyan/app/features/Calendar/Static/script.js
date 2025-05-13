document.getElementById("addForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let name = document.getElementById("name").value;
    let date = document.getElementById("date").value;
    let reminder = document.getElementById("reminder").value;

    fetch("/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, date, reminder })
    }).then(response => response.json())
      .then(data => alert(data.message || data.error))
      .then(() => location.reload());
});

function deleteAssessment(date) {
    fetch("/delete", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ date })
    }).then(() => location.reload());
}

function deleteAll() {
    fetch("/delete_all", { method: "POST" })
    .then(() => location.reload());
}
