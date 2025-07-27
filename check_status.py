from database_connection import get_latest_predictions
from datetime import datetime, timedelta, timezone

def check_service_status():
    """
    Check if the prediction service is running properly by verifying recent predictions
    """
    try:
        # Get the latest prediction
        latest = get_latest_predictions()
        
        if not latest:
            print("❌ No predictions found in database")
            return False
        
        # Parse the timestamp and ensure it's timezone-aware
        latest_time = datetime.fromisoformat(latest['timestamp'].replace('Z', '+00:00'))
        current_time = datetime.now(timezone.utc)
        
        # Check if we have predictions in the last 15 minutes
        time_diff = current_time - latest_time
        
        print("\n=== Service Status Check ===")
        print(f"Current Time (UTC): {current_time}")
        print(f"Latest Prediction: {latest_time}")
        print(f"Time Since Last Prediction: {time_diff}")
        
        if time_diff > timedelta(minutes=15):
            print("⚠️ Warning: No recent predictions found")
            print(f"Last prediction was {time_diff.total_seconds() / 60:.1f} minutes ago")
            return False
        
        print("\n=== Latest Prediction Details ===")
        print(f"Risk Level: {latest['landslide_risk']}")
        print(f"Risk Probability: {latest['risk_probability']:.2f}")
        print(f"Model Accuracy: {latest['model_accuracy']:.2f}")
        print("\n✅ Service is running normally")
        return True
        
    except Exception as e:
        print(f"❌ Error checking service status: {str(e)}")
        return False

if __name__ == "__main__":
    check_service_status()
