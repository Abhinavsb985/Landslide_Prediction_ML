-- First, check if columns exist
DO $$ 
BEGIN
    -- Add model_accuracy if it doesn't exist
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns 
                  WHERE table_name = 'sensor_data' AND column_name = 'model_accuracy') THEN
        ALTER TABLE sensor_data ADD COLUMN model_accuracy FLOAT8;
    END IF;

    -- Add model_mae if it doesn't exist
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns 
                  WHERE table_name = 'sensor_data' AND column_name = 'model_mae') THEN
        ALTER TABLE sensor_data ADD COLUMN model_mae FLOAT8;
    END IF;

    -- Add model_r2 if it doesn't exist
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns 
                  WHERE table_name = 'sensor_data' AND column_name = 'model_r2') THEN
        ALTER TABLE sensor_data ADD COLUMN model_r2 FLOAT8;
    END IF;
END $$;
