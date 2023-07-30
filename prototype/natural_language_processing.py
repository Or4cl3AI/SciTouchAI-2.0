import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Shared variables
user_input = ""

def processInput(user_input):
    """
    Function to process the user input using natural language processing techniques
    """
    # Tokenization
    tokens = word_tokenize(user_input)

    # Removing Stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if not word in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    return lemmatized_tokens

def inputError():
    """
    Function to handle input errors
    """
    print("Invalid input. Please try again.")

def outputMessage(lemmatized_tokens):
    """
    Function to display output message
    """
    print("Processed input: ", ' '.join(lemmatized_tokens))