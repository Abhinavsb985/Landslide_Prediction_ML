@echo off
echo 🚀 Railway.app Deployment Helper
echo.

echo 📋 Checking if you have the necessary files...
if not exist "app.py" (
    echo ❌ app.py not found! Make sure you're in the right directory.
    pause
    exit /b 1
)

if not exist "requirements.txt" (
    echo ❌ requirements.txt not found!
    pause
    exit /b 1
)

if not exist "Dockerfile" (
    echo ❌ Dockerfile not found!
    pause
    exit /b 1
)

echo ✅ All required files found!
echo.

echo 📝 Next steps to deploy to Railway.app:
echo.
echo 1. 📤 Push your code to GitHub:
echo    git add .
echo    git commit -m "Ready for Railway deployment"
echo    git push
echo.
echo 2. 🌐 Go to railway.app:
echo    - Visit https://railway.app
echo    - Sign up with GitHub
echo    - Click "New Project"
echo    - Select "Deploy from GitHub repo"
echo    - Choose your repository
echo.
echo 3. ⚙️ Railway will automatically:
echo    - Detect your Python app
echo    - Use the Dockerfile we created
echo    - Install dependencies from requirements.txt
echo    - Deploy your app
echo.
echo 4. 🎉 Get your URL:
echo    - Railway will give you a URL like: https://your-app-name.railway.app
echo    - Your app will be live in the cloud!
echo.
echo 📊 Monitor your app:
echo    - Check logs in Railway dashboard
echo    - Visit your app URL to see health status
echo    - Your ML predictions will run every 3 minutes automatically
echo.

echo 🎯 Why Railway.app is perfect for you:
echo ✅ FREE forever (up to $5/month usage)
echo ✅ No complex setup - just push code
echo ✅ Automatic restarts if app crashes
echo ✅ Solves your Ctrl+C problem
echo ✅ 24/7 uptime
echo.

echo 💡 Tips:
echo - Your app will restart automatically if it crashes
echo - No need to worry about Ctrl+C anymore
echo - Check the logs if something goes wrong
echo - Railway handles all the server management
echo.

echo 🚀 Ready to deploy? Follow the steps above!
echo 📚 For detailed instructions, see railway-deploy-guide.md
echo.

pause 