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

# add following to Project → Properties 
# C/C++ → General → Additional Include Directories
D:\GitHub\vcpkg\installed\x64-windows\include

# General → C++ Language Standard → ISO C++17 Standard (/std:c++17)

# Running the Program

cd D:\GitHub\mapserver-templates

./x64/Debug/mapserver-templates.exe template.inja data.json

./x64/Debug/mapserver-templates.exe ./mapserver-index/landing.html ./mapserver-index/data.json

# pipe to file
./x64/Debug/mapserver-templates.exe template.inja data.json > output.html

# debug program add following to 
# template.inja data.json > output.html
# mapserver-index/landing.html mapserver-index/data.json


C:\Python313\python -m http.server -d D:\GitHub\mapserver-templates\isric
http://localhost:8000/test2.html


## CMake Build

```
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