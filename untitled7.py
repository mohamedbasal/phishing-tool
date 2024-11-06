from bs4 import BeautifulSoup
import re
from html.parser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc
import joblib
import pandas as pd
from urllib.parse import urlparse
from googlesearch import search
from spellchecker import SpellChecker
from language_tool_python import LanguageTool
import pickle
# Load the saved model and preprocessing steps
model_path = 'saved_model.pkl'
vectorizer_path = 'saved_vectorizer.pkl'

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Load the phishing classifier model
with open('phishing_classifier.pkl', 'rb') as file:
    phishing_classifier = pickle.load(file)

# Define the IP address regex pattern
IP_REGEX = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

# Function to extract features from a URL
def extract_features(url):
    url = url.replace('www.', '')  # Remove 'www.' if present
    url_len = len(url)
    letters_count = sum(1 for char in url if char.isalpha())
    digits_count = sum(1 for char in url if char.isdigit())
    special_chars_count = sum(1 for char in url if char in '@?-=.#%+$!*,//')
    shortened = 1 if re.search(r'bit\.ly|goo\.gl|shorte\.st|tinyurl\.com', url) else 0
    abnormal = 1 if urlparse(url).hostname != url else 0
    secure_https = 1 if urlparse(url).scheme == 'https' else 0
    have_ip = 1 if re.search(IP_REGEX, url) else 0
    google_index = 1 if len(list(search(url, num=1))) > 0 else 0

    features = {
        'url_len': url_len,
        'letters_count': letters_count,
        'digits_count': digits_count,
        'special_chars_count': special_chars_count,
        'shortened': shortened,
        'abnormal': abnormal,
        'secure_https': secure_https,
        'have_ip': have_ip,
        'google_index': google_index
    }
    
    return pd.DataFrame([features])

# Function to make predictions using the loaded model for a list of URLs
def predict_urls(url_list):
    predictions = []
    for url in url_list:
        features_df = extract_features(url)
        prediction = phishing_classifier.predict(features_df.values)
        predictions.append(prediction[0])
    return predictions

class _DeHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()

def dehtml(text):
    try:
        parser = _DeHTMLParser()
        parser.feed(text)
        parser.close()
        return parser.text()
    except Exception as e:
        print_exc(file=stderr)
        return text

def extract_links_from_email(html_content):
    extracted_links = []

    soup = BeautifulSoup(html_content, 'html.parser')
    for link in soup.find_all('a', href=True):
        url = link['href']
        if url.startswith('http'):
            extracted_links.append(url)

    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html_content)
    for url in urls:
        if url not in extracted_links:
            extracted_links.append(url)

    return extracted_links

class LanguageCorrectionModule:
    def __init__(self):
        self.spell_checker = SpellChecker()
        self.grammar_checker = LanguageTool('en-US')

    def correct_spelling(self, text):
        corrected_text = ""
        for word in text.split():
            if word.istitle():
                corrected_word = word
            else:
                corrected_word = self.spell_checker.correction(word)
            if corrected_word is not None:
                corrected_text += corrected_word + " "
            else:
                corrected_text += word + " "
        return corrected_text.strip()

    def correct_grammar(self, text):
        matches = self.grammar_checker.check(text)
        corrected_text = self.grammar_checker.correct(text)
        grammar_mistakes = [match.ruleId for match in matches]
        return corrected_text, grammar_mistakes

def main():
    language_correction_module = LanguageCorrectionModule()
    html_mail = input("Please enter your E-mail\n")
    original_text = dehtml(html_mail)

    corrected_spelling = language_correction_module.correct_spelling(original_text)
    print("\nOriginal Text:")
    print(original_text)
    print("\nCorrected Spelling:")
    print(corrected_spelling)
    
    corrected_text, grammar_mistakes = language_correction_module.correct_grammar(corrected_spelling)
    print("\nCorrected Grammar:")
    print(corrected_text)
    
    print("\nGrammar Mistakes:")
    for mistake in grammar_mistakes:
        print("- " + mistake)
    
    extracted_links = extract_links_from_email(html_mail)
    predictions = predict_urls(extracted_links)

    for i, url in enumerate(extracted_links):
        print(f"Prediction for {url}: {'Good' if predictions[i] == 1 else 'Suspicious'}")

    new_data_transformed = vectorizer.transform([original_text])
    pred = model.predict(new_data_transformed)

    print('Predicted:', 'Phishing text' if pred[0] == -1 else 'Safe text')

if __name__ == '__main__':
    main()
