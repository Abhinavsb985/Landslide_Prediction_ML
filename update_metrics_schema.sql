-- Add model performance metrics columns to sensor_data table
ALTER TABLE sensor_data
ADD COLUMN IF NOT EXISTS model_accuracy FLOAT8,
ADD COLUMN IF NOT EXISTS model_mae FLOAT8,
ADD COLUMN IF NOT EXISTS model_r2 FLOAT8;
