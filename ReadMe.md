﻿# MapServer Templates

This repository is used to store notes and tests related to [MS RFC 140: MapServer Homepage](https://mapserver.org/development/rfc/ms-rfc-140.html).

A test application was created to more easily 

## Contents

- [Proposed JSON Structure](json.md)
- [mapserver-index](/mapserver-index/) - test C++ application for experimenting with [inja](https://github.com/pantor/inja) templates. 
- [scripts](/scripts/) - a collection of Python scripts
  - [api-catalog-schema.json](/scripts/api-catalog-schema.json) - a JSON schema for the proposed JSON output
  - [validate.py](/scripts/validate.py) - a Python script for validating output against the JSON schema
- [isric](/isric/) - a more advanced template for [ISRIC](https://www.isric.org/).

Example template outputs:

- [Plain example](https://geographika.github.io/mapserver-templates/output.html)
- [ISRIC example](https://geographika.github.io/mapserver-templates/)

## Test Application Build Steps

First clone [vcpkg](https://github.com/microsoft/vcpkg) and use this to get dependencies.

```
$vcpkg = "D:\GitHub\vcpkg"
cd $vcpkg
git pull

$env:VCPKG_ROOT=$vcpkg
$env:PATH="$env:VCPKG_ROOT;$env:PATH"

.\bootstrap-vcpkg.bat

vcpkg update
vcpkg search inja

vcpkg install inja
vcpkg install nlohmann-json
```

In Visual Studio add the following to Project → Properties → C/C++ → General → Additional Include Directories: `D:\GitHub\vcpkg\installed\x64-windows\include`

Set General → C++ Language Standard → ISO C++17 Standard (/std:c++17).

## CMake Build

A fully working build can also be seen in the [GitHub Actions YAML file](/.github/workflows/build.yml).

```ps1
cd D:\GitHub\mapserver-templates
Remove-Item -Recurse -Force build
mkdir build
cd build

$env:PATH="D:/Tools/cmake-3.22.3-windows-x86_64/bin;" + $env:PATH
# $env:VCPKG_ROOT="D:/GitHub/vcpkg"
cmake .. -DCMAKE_TOOLCHAIN_FILE="$env:VCPKG_ROOT/scripts/buildsystems/vcpkg.cmake" -A x64
cmake --build . --config Debug

.\Debug\mapserver-templates.exe ../template.inja ../data.json
```

## Running the Test Application

```ps1
cd D:\GitHub\mapserver-templates

./build/Debug/mapserver-templates.exe template.inja data.json

./build/Debug/mapserver-templates.exe ./mapserver-index/landing.html ./mapfiles/api-catalog.json

# pipe to file
./build/Debug/mapserver-templates.exe template.inja data.json > output.html

# debug program add following to 
# template.inja data.json > output.html
# mapserver-index/landing.html mapfiles/api-catalog.json
```
