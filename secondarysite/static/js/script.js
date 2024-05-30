document.getElementById('runCommandButton').addEventListener('click', function() {
    fetch('/run-command', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            document.getElementById('output').textContent = data.output;
        } else {
            document.getElementById('output').textContent = 'Error: ' + data.message;
            console.error('Error Output:', data.error);
        }
    })
    .catch(error => {
        console.error('Fetch Error:', error);
        document.getElementById('output').textContent = 'An error occurred while trying to run the command';
    });
});

