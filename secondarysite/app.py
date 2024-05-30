from flask import Flask, render_template, jsonify, request
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
            ['bash', '-c', 'ifconfig'],
            stdout=subprocess.PIPE,  # Capture stdout
            stderr=subprocess.PIPE,  # Capture stderr
            text=True  # Return stdout and stderr as strings
        )
        stdout, stderr = process.communicate()  # Communicate with the process to get the output and error

        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, process.args, output=stdout, stderr=stderr)

        return jsonify({
            'status': 'success',
            'output': stdout,  # Command output
            'error': stderr  # Command error output
        })
    except subprocess.CalledProcessError as e:
        return jsonify({
            'status': 'error',
            'message': f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.",
            'output': e.output,
            'error': e.stderr
        }), 500
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=1221)

