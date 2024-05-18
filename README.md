# Prefix Tree Translator

## Description
The Prefix Tree Translator is a Python program that implements a prefix tree (trie) data structure to translate words into multiple languages using the Google Translate API. It allows users to input words in English and translates them into various languages, storing and displaying the translated words along with their weights and paths in the prefix tree.

## Features
- Prefix Tree Implementation: Utilizes a prefix tree to efficiently store translated words and their metadata.
- Translation: Translates words from English into multiple languages using the Google Translate API.
- Word Weight Calculation: Calculates the weight of each word based on its frequency in the translations.
- Language Support: Supports translation into multiple languages, including English, German, Spanish, French, Italian, Danish, Romanian, and Dutch.
- Web Interface: Provides a web interface for users to input words and view translation results.

## Usage
1. Enter a word in English into the input field on the web interface.
2. Click the "Translate" button to initiate the translation process.
3. View the translation results, including the translated words, their weights, paths in the prefix tree, and the target languages.
4. Click the "Go Back" button to return to the input form and translate another word.

## Requirements
- Python 3.x
- Flask
- googletrans library

## Installation
1. Clone the repository: `git clone https://github.com/your_username/prefix-tree-translator.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the Flask application: `python trie.py`
4. Access the web interface in your browser at `http://localhost:5000`