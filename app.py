from flask import Flask
import threading
import time
from datetime import datetime
import landslide_prediction

app = Flask(__name__)

def run_prediction_loop():
    while True:
        try:
            print(f"\n[{datetime.now()}] Starting landslide prediction...")
            landslide_prediction.main()
            print(f"[{datetime.now()}] Prediction completed successfully")
        except Exception as e:
            print(f"[{datetime.now()}] Error in prediction: {str(e)}")
        time.sleep(300)  # 300 seconds = 5 minutes

# Start prediction thread
prediction_thread = threading.Thread(target=run_prediction_loop, daemon=True)
prediction_thread.start()

@app.route('/')
def health_check():
    return {"status": "alive", "last_check": str(datetime.now())}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
