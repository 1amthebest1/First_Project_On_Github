document.getElementById('runCommandButton').addEventListener('click', function() {
    fetch('/run-command', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output').textContent = data.output || data.message;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('output').textContent = 'An error occurred';
    });
});
