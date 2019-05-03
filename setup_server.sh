ENTRYPOINT="python3"
pip freeze > requirements.txt
$ENTRYPOINT fetch_data.py
$ENTRYPOINT service.py