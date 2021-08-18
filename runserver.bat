set log_file=%date%.log
echo Writing to %log_file%
python manage.py runserver >> %log_file% 2>&1