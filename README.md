# Landslide Prediction Service

This service runs continuous landslide predictions for Shirur area every 10 minutes and saves the results to the database.

## Cloud Deployment Options

### Option 1: Railway.app (Recommended for Beginners)
1. Create account at railway.app
2. Install Railway CLI:
   ```bash
   npm i -g @railway/cli
   ```
3. Login and deploy:
   ```bash
   railway login
   railway init
   railway up
   ```

### Option 2: DigitalOcean
1. Create account and get $200 credit
2. Install doctl
3. Create a droplet:
   ```bash
   doctl compute droplet create landslide-predictor \
     --image docker-20-04 \
     --size s-1vcpu-1gb \
     --region blr1
   ```
4. SSH into droplet and clone repo
5. Run with:
   ```bash
   docker-compose up -d
   ```

### Option 3: Google Cloud Platform
1. Create account (get $300 free credit)
2. Install gcloud CLI
3. Deploy to Cloud Run:
   ```bash
   gcloud builds submit --tag gcr.io/PROJECT_ID/landslide-predictor
   gcloud run deploy landslide-predictor \
     --image gcr.io/PROJECT_ID/landslide-predictor \
     --platform managed
   ```

## Features

- 24/7 operation on cloud servers
- Automatic predictions every 10 minutes
- Saves results to Supabase database
- Auto-restarts if the container crashes
- Health monitoring and logging
- Resource-efficient (uses ~256-512MB RAM)

## Monitoring

- Railway/DigitalOcean/GCP dashboard for container health
- `docker logs -f landslide-predictor` on the server
- Supabase dashboard for prediction results

## Environment Variables
Required environment variables:
- `SUPABASE_URL`: Your Supabase project URL
- `SUPABASE_KEY`: Your Supabase API key

## Security Notes
- Keep your API keys secure
- Use environment variables for sensitive data
- Regularly update dependencies
- Monitor server logs for unusual activity

## Troubleshooting

### Railway.app Issues
```bash
railway logs
railway restart
```

### DigitalOcean Issues
```bash
doctl compute droplet list
doctl compute droplet-action reboot
```

### General Docker Issues
```bash
docker logs landslide-predictor
docker-compose restart
docker-compose up -d --build  # For rebuilds
```
