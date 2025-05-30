echo "Running database migrations..."
python manage.py migrate

echo "Start Uvicorn"
exec uvicorn config.asgi:application --host 0.0.0.0 --port 8000
