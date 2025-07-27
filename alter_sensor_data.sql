-- Add new columns for weather and prediction data to sensor_data table
ALTER TABLE sensor_data
ADD COLUMN IF NOT EXISTS rainfall_24h_mm FLOAT8,
ADD COLUMN IF NOT EXISTS rainfall_3h_mm FLOAT8,
ADD COLUMN IF NOT EXISTS soil_type VARCHAR(50),
ADD COLUMN IF NOT EXISTS slope_degrees FLOAT8,
ADD COLUMN IF NOT EXISTS expected_tomorrow_rainfall_24h_mm FLOAT8,
ADD COLUMN IF NOT EXISTS predicted_soil_moisture FLOAT8,
ADD COLUMN IF NOT EXISTS predicted_pore_pressure FLOAT8,
ADD COLUMN IF NOT EXISTS landslide_risk VARCHAR(20),
ADD COLUMN IF NOT EXISTS risk_probability FLOAT8,
ADD COLUMN IF NOT EXISTS alert boolean,
ADD COLUMN IF NOT EXISTS notification TEXT;

-- Add indices for better query performance if they don't exist
CREATE INDEX IF NOT EXISTS idx_timestamp ON sensor_data(timestamp);
CREATE INDEX IF NOT EXISTS idx_alert ON sensor_data(alert);
