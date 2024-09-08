Create virtual env
```
python3 -m venv
```

Activate environment
```
source bin/activate
```

Deactivate environment
```
deactivate
```

Run Requirements package
```
pip install -r requirements.txt
```


Run server
````
uvicorn app.main:app --reload --port 8080
````