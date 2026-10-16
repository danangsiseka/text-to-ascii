# Text to ASCII Converter

![C++](https://img.shields.io/badge/C%2B%2B-17-blue?style=flat-square\&logo=cplusplus\&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-success)

A simple C++-based command-line tool that converts text into ASCII decimal codes.

## Features

* Convert text into ASCII decimal codes
* Support words, sentences, and spaces
* Display ASCII codes in a single line
* Convert multiple texts without restarting the program
* Provide a simple interactive command-line interface

## How to Run

Make sure a C++ compiler that supports C++17 is installed on your computer.

Clone the repository:

```bash
git clone https://github.com/danangsiseka/text-to-ascii.git
```

Enter the project directory:

```bash
cd text-to-ascii
```

Compile the program:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic text-to-ascii.cpp -o text-to-ascii
```

Run the program:

**Windows:**

```bash
text-to-ascii.exe
```

**Linux / macOS:**

```bash
./text-to-ascii
```

## Example

```text
========================================
          TEXT TO ASCII CONVERTER
========================================

Enter text: Hello

ASCII Output:
72 101 108 108 111

Convert another text? (y/n): n

Thank you for using the converter!
```

The program converts each input byte into its corresponding numerical value. For standard ASCII characters, these values represent their ASCII decimal codes.

## Project Structure

```text
text-to-ascii/
│
├── text-to-ascii.cpp
├── README.md
├── LICENSE
└── .gitignore
```

## Purpose

This project was created as a practical C++ project for learning programming fundamentals, character processing, functions, and basic command-line application development.

## License

This project is licensed under the MIT License.
