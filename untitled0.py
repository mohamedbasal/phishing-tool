# This code performs spell checking and grammar correction

from bs4 import BeautifulSoup
import re
from spellchecker import SpellChecker
from language_tool_python import LanguageTool


class LanguageCorrectionModule:
    def __init__(self):
        # Initialize spell checker and grammar checker
        self.spell_checker = SpellChecker()
        self.grammar_checker = LanguageTool('en-US')

    def correct_spelling(self, text):
        """
        Corrects the spelling in the given text.

        Parameters:
        - text (str): The text to be corrected.

        Returns:
        - corrected_text (str): The text with corrected spelling.
        """
        corrected_text = ""
        for word in text.split():
            # Skip correction for proper nouns
            if not word.istitle():
                corrected_word = self.spell_checker.correction(word)
            else:
                corrected_word = word
            corrected_text += corrected_word + " "
        return corrected_text.strip()

    def correct_grammar(self, text):
        """
        Corrects the grammar in the given text.

        Parameters:
        - text (str): The text to be corrected.

        Returns:
        - corrected_text (str): The text with corrected grammar.
        - grammar_mistakes (list): List of grammar mistakes.
        """
        # Check grammar and get corrections
        matches = self.grammar_checker.check(text)
        corrected_text = self.grammar_checker.correct(text)

        # Extract grammar mistakes
        grammar_mistakes = [match.ruleId for match in matches]

        return corrected_text, grammar_mistakes


if __name__ == "__main__":

    # Create an instance of LanguageCorrectionModule
    language_correction_module = LanguageCorrectionModule()

    # Process HTML content (assuming it's available from somewhere)
    # Replace this part with your code to get the HTML content
    html_content = """
    <!DOCTYPE html>
    <body>
        <p>This is some text with a spelling error (tehst) and some grammar mistakes (e.g., missing comma).</p>
    </body>
    </html>
    """

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract text from the HTML
    text = soup.get_text(separator='\n', strip=True)

    # Remove extra spaces and line breaks
    text = re.sub(r'\s+', ' ', text)

    # Save the extracted text to a file
    with open("extracted_text.txt", "w") as output_file:
        output_file.write(text)

    # Read the extracted text from the file (simulating the output of the first code)
    with open('extracted_text.txt', 'r') as file:
        original_text = file.read()

    print("Original Text:")
    print(original_text)

    # Correct spelling
    corrected_spelling = language_correction_module.correct_spelling(original_text)
    print("\nCorrected Spelling:")
    print(corrected_spelling)

    # Correct grammar
    corrected_text, grammar_mistakes = language_correction_module.correct_grammar(corrected_spelling)
    print("\nCorrected Grammar:")
    print(corrected_text)

    # Display grammar mistakes
    print("\nGrammar Mistakes:")
    for mistake in grammar_mistakes:
        print("- " + mistake)
