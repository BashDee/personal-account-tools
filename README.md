# Prerequisite
python 3.11

## Setup virtual envorinment

## install dependencies from requirements.txt



## Virtual Environment 
### creating a virtual Env
python -m venv tutorial-env

## Starting Virtual Environmet
venv\Scripts\activate

## Deactivate
deactivate


curl -X POST "http://127.0.0.1:8000/add_asset/?user=test_user" -H "Content-Type: application/json" -d "{\"id\": 1, \"name\": \"Laptop\", \"value\": 1000, \"is_liquid\": 0}"
curl -X DELETE "http://127.0.0.1:8000/remove_asset/1?user=test_user"
curl -X PUT "http://127.0.0.1:8000/modify_asset/1?user=test_user" -H "Content-Type: application/json" -d "{\"name\": \"Gaming Laptop\", \"value\": 1500}"
curl -X GET "http://127.0.0.1:8000/total_value/"
curl -X GET "http://127.0.0.1:8000/list_assets/?user=test_user" -H "Content-Type: application/json"