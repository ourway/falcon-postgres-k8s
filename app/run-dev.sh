sleep 1
alembic upgrade head
sleep 1
gunicorn app -b 0.0.0.0:80 --reload --log-level debug
