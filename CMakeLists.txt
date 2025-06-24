cmake_minimum_required(VERSION 3.15)  # Adjust version if needed
project(MapServerTemplates)           # Project name

# Set C++ standard (C++17 recommended for nlohmann-json/inja)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Tell CMake to use vcpkg (critical for dependency resolution)
set(CMAKE_TOOLCHAIN_FILE "$ENV{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake" CACHE STRING "")

# Find packages via vcpkg (inja and nlohmann-json)
find_package(inja CONFIG REQUIRED)
find_package(nlohmann_json CONFIG REQUIRED)

# Verify targets exist (debugging)
if(TARGET pantor::inja)  # Use the correct target name
    message(STATUS "Found inja: pantor::inja")
else()
    message(FATAL_ERROR "inja target (pantor::inja) not found!")
endif()

if(NOT TARGET nlohmann_json::nlohmann_json)
    message(FATAL_ERROR "nlohmann_json target not found!")
endif()

# Add executable
add_executable(mapserver-templates src/main.cpp)

# Link dependencies
target_link_libraries(mapserver-templates PRIVATE pantor::inja nlohmann_json::nlohmann_json)

# Copy template/data files to build directory (optional)
# configure_file(template.inja ${CMAKE_CURRENT_BINARY_DIR}/template.inja COPYONLY)
# configure_file(data.json ${CMAKE_CURRENT_BINARY_DIR}/data.json COPYONLY)