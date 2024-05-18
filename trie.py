from flask import Flask, request, jsonify, render_template
from googletrans import Translator
import json 

app = Flask(__name__)

class PrefixTreeMain:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        self.weight = 0
        self.word_count = {}
        self.langs = []

        self.lang_codes = {
            'English': 'en',
            'German': 'de',
            'Spanish': 'es',
            'French': 'fr',
            'Italian': 'it',
            'Danish': 'da',
            'Romanian': 'ro',
            'Dutch': 'nl'
        }

    def insert(self, word, lang):
        translated_word = self.translate_word(word, lang)
        translated_word = translated_word.lower()
        translated_word = ''.join(filter(str.isalpha, translated_word))  # Filter out non-alphabetic characters
        node = self

        for c in translated_word:
            index = ord(c) - ord('a')
            if not 0 <= index < 26:
                continue  # Skip non-alphabetic characters
            if not node.children[index]:
                node.children[index] = PrefixTreeMain()
            node = node.children[index]
            node.weight += 1  # Increment the weight of the current node

        node.isEnd = True

        # Store languages as a list and ensure uniqueness
        if lang not in node.langs:
            node.langs.append(lang)


    def translate_word(self, word, lang):
        translator = Translator()
        translation = translator.translate(word, dest=self.lang_codes[lang])
        return translation.text

    def get_similar_words(self, min_weight=1):
        result = {}
        self.get_similar_words_helper(self, "", result, min_weight)
        return result

    def get_similar_words_helper(self, node, path, result, min_weight):
        if node.isEnd and node.weight >= min_weight:
            for lang in node.langs:
                if node.weight not in result:
                    result[node.weight] = {}
                if lang not in result[node.weight]:
                    result[node.weight][lang] = []
                result[node.weight][lang].append(path)
        for i in range(26):
            if node.children[i]:
                c = chr(ord('a') + i)
                self.get_similar_words_helper(node.children[i], path + c, result, min_weight)






@app.route('/translate', methods=['GET', 'POST'])
def translate():
    if request.method == 'GET':
        word = request.args.get('word')
    elif request.method == 'POST':
        data = request.json
        word = data['word']
    else:
        return jsonify({'error': 'Invalid request method'})
    
    trie = PrefixTreeMain()
    langs = ['English', 'German', 'Spanish', 'French', 'Italian', 'Danish', 'Romanian', 'Dutch']
    
    # Insert translated words into the trie for each language
    for lang in langs:
        trie.insert(word, lang)

    similar_words = trie.get_similar_words(min_weight=1)
    
    # Prepare response
    response_data = {'similar_words': similar_words}
    
    return jsonify(response_data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    # Retrieve the similar_words data from the query parameters
    similar_words = request.args.get('similar_words')
    if similar_words:
        similar_words = json.loads(similar_words)
    else:
        similar_words = {}
    
    # Render the result.html template with the similar_words data
    return render_template('result.html', similar_words=similar_words)

if __name__ == "__main__":
    app.run(debug=True)
