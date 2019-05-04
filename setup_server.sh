ENTRYPOINT="python3"
pip freeze > requirements.txt
$ENTRYPOINT test.py
$ENTRYPOINT fetch_data.py
$ENTRYPOINT service.py