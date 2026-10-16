#include <iostream>
#include <string>
#include <cctype>

using namespace std;

// --------------------------------------------------
// Display Helpers
// --------------------------------------------------

void printHeader() {
    cout << "\n";
    cout << "========================================\n";
    cout << "          TEXT TO ASCII CONVERTER\n";
    cout << "========================================\n";
}

// --------------------------------------------------
// Conversion
// --------------------------------------------------

void convertToASCII(const string& text) {
    cout << "\nASCII Output:\n";

    for (unsigned char character : text) {
        cout << static_cast<int>(character) << " ";
    }

    cout << "\n";
}

// --------------------------------------------------
// Main Program
// --------------------------------------------------

int main() {
    string text;
    char choice;

    do {
        printHeader();

        cout << "\nEnter text: ";
        getline(cin, text);

        convertToASCII(text);

        cout << "\nConvert another text? (y/n): ";
        cin >> choice;
        cin.ignore(10000, '\n');

        choice = static_cast<char>(
            tolower(static_cast<unsigned char>(choice))
        );

    } while (choice == 'y');

    cout << "\nThank you for using the converter!\n";

    return 0;
}

