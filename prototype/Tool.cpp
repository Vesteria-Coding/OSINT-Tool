#include <format>
#include <iostream>
#include <string>
#include <cpr/cpr.h>
#include <nlohmann/json.hpp>
#include <limits>

using json = nlohmann::json;

void ip_lookup(std::string ip) {
    std::string url = "http://ip-api.com/json/" + ip;
    cpr::Response r = cpr::Get(cpr::Url{url});
    json json_data = json::parse(r.text);
    std::string result = std::format("IP Address: {}, Country: {}, Region: {}, City: {}, Latitude: {}, Longitude: {}", ip, json_data["country"].get<std::string>(), json_data["regionName"].get<std::string>(), json_data["city"].get<std::string>(), json_data["lat"].get<double>(), json_data["lon"].get<double>());
    std::cout << result << std::endl;
}

int main() {
    int choice = 0;
    std::string placeholder = "";
    std::string ipv4 = "";
    while (true) {
        choice = 0;
        ipv4 = "";
        while (true) {
            try {
                std::cout << "0. Quit\n1. Username Finder (not added yet)\n2. IP Lookup\n3. Domain Lookup (not added yet)\n4.\n5.\n5.\n7.\n8.\n9.\n10." << std::endl;
                std::cout << "Choose an option: ";
                std::cin >> choice;
                if (!std::cin) throw "Invalid input!";
                break;
            }
            catch (const char* msg) {
                std::cout << "Invalid input please input a number 0 - 10" << std::endl;
            }
        }
        if (choice == 0) {
            return 0;
        } else if (choice == 1) {
            // placeholder for doing the username search
        } else if (choice == 2) {
            std::cout << "What ipv4 address do you want to look up?" << std::endl;
            std::cin >> ipv4;
            ip_lookup(ipv4);
        } else if (choice == 3) {
            // placeholder for domain lookup
        } else if (choice == 4) {
            // placeholder
        } else if (choice == 5) {
            // placeholder
        } else if (choice == 6) {
            // placeholder
        } else if (choice == 7) {
            // placeholder
        } else if (choice == 8) {
            // placeholder
        } else if (choice == 9) {
            // placeholder
        } else if (choice == 10) {
            // placeholder
        } else {
            std::cout << "Unknow input ERROR" << std::endl;
            return 1;
        }
        std::cout << "Press enter/return to continue.";
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cin.get();
    }
}
