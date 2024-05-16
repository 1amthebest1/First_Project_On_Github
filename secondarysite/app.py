from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-command', methods=['POST'])
def run_command():
    try:
        # Run the shell command in a new shell process
        process = subprocess.Popen(
            ['bash', '-c', 'gobuster dir -u https://bahria.edu.pk -w /usr/share/wordlists/dirb/big.txt --wildcard -k'],
            stdout=subprocess.PIPE,  # Capture stdout
            stderr=subprocess.PIPE,  # Capture stderr
            text=True  # Return stdout and stderr as strings
        )
        stdout, stderr = process.communicate()  # Communicate with the process to get the output and error

        return jsonify({
            'status': 'success',
            'output': stdout,  # Command output
            'error': stderr  # Command error output
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=1221)
