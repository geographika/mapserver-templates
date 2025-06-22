#include <inja/inja.hpp>
#include <nlohmann/json.hpp>
#include <filesystem>
#include <fstream>
#include <sstream>
#include <iostream>
#include <set>
#include <vector>
#include <string>


int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <template.inja> <data.json>\n";
        return 1;
    }

    std::filesystem::path template_path(argv[1]);
    std::filesystem::path json_path(argv[2]);

    // set environment with template directory
    // ensure trailing separator for the env path, otherwise:
    // Unexpected error : [inja.exception.file_error] failed accessing file at 'mapserver-indexheader.html'
    std::string template_dir = template_path.parent_path().string();
    if (!template_dir.empty() && template_dir.back() != std::filesystem::path::preferred_separator) {
        template_dir += std::filesystem::path::preferred_separator;
    }

    inja::Environment env(template_dir);


    // Read template file
    std::ifstream template_file(template_path);
    if (!template_file) {
        std::cerr << "Error: Cannot open template file: " << template_path << "\n";
        return 1;
    }
    std::stringstream buffer;
    buffer << template_file.rdbuf();
    std::string template_string = buffer.str();

    // Read JSON file
    std::ifstream json_file(json_path);
    if (!json_file) {
        std::cerr << "Error: Cannot open JSON file: " << json_path << "\n";
        return 1;
    }
    nlohmann::json data;
    try {
        json_file >> data;
    }
    catch (const std::exception& e) {
        std::cerr << "Error parsing JSON: " << e.what() << "\n";
        return 1;
    }

    // Render with error handling
    try {
        std::string result = env.render(template_string, data);
        std::cout << result;
    }
    catch (const inja::RenderError& e) {
        std::cerr << "Template render error: " << e.what() << "\n";
        return 1;
    }
    catch (const std::exception& e) {
        std::cerr << "Unexpected error: " << e.what() << "\n";
        return 1;
    }

    return 0;
}
