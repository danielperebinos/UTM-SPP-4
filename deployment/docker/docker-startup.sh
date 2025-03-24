echo "Running database migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Start Uvicorn"
exec uvicorn config.asgi:application --host 0.0.0.0 --port 8000 --reload
