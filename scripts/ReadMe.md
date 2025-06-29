# Demo App

```python
cd D:\GitHub\mapserver-templates\scripts
C:\Python312\python -m http.server --directory=. 8006
```

http://localhost:8006/dist

Regenerate JSON output:

```
C:\VirtualEnvs\misc\Scripts\Activate.ps1
cd D:\GitHub\mapserver-templates\scripts
# pip install -e D:\GitHub\mappyfile
python services.py
```

Regenerate HTML output:

```
cd d D:\GitHub\mapserver-templates
./build/Debug/mapserver-templates.exe ./mapserver-index/html-bootstrap4/landing.html ./scripts/dist/api-catalog.json > ./scripts/dist/index.html

./build/Debug/mapserver-templates.exe ./mapserver-index/html-bootstrap4/map.html ./scripts/dist/wmsdemo/api-catalog.json

```