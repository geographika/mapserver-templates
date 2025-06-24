# ISRIC Template Example


## Build

Within a Developer VS PowerShell:

```ps1
cd D:\GitHub\mapserver-templates

./build/Debug/mapserver-templates.exe isric/landing.html isric/data.json

./build/Debug/mapserver-templates.exe isric/landing.html mapfiles/api-catalog.json > isric/index.html
```

Viewing HTML output:

```ps1
C:\Python313\python -m http.server -d D:\GitHub\mapserver-templates\isric
# http://localhost:8000/
```