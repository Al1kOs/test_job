from flask import Flask, send_file

app = Flask(__name__)

@app.route('/get-log')
def get_log():
    try:
        return send_file('/var/log/nginx/myapp_access.log', as_attachment=False)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)