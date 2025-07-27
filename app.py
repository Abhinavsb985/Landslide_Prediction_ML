from flask import Flask
import threading
from scheduler import run_prediction, main as scheduler_main

app = Flask(__name__)

@app.route('/')
def health_check():
    return {"status": "healthy"}, 200

@app.route('/trigger-prediction')
def trigger():
    run_prediction()
    return {"status": "prediction triggered"}, 200

if __name__ == '__main__':
    # Start the scheduler in a separate thread
    scheduler_thread = threading.Thread(target=scheduler_main, daemon=True)
    scheduler_thread.start()
    
    # Start the Flask app
    app.run(host='0.0.0.0', port=8000)
