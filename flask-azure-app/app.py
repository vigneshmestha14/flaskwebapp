from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',
                         title='Flask Azure App',
                         current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/health')
def health():
    return {'status': 'healthy', 'timestamp': datetime.now().isoformat()}

if __name__ == '__main__':
    app.run(debug=True)