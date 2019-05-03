ENTRYPOINT="pipenv run python3"
$ENTRYPOINT fetch_data.py
$ENTRYPOINT service.py
