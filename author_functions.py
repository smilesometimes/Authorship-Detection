##########  Provided helper function. ############
# Define two helper functions called create_word_list and create_sentence_list
def create_word_list(text):
    """(list of str) -> (list of str)
	
    Precondition: text is non-empty. Text contains at least one word.
	
    Return the average length of all words in text.
	
    >>>text = ['James Fennimore Cooper\n', 'Peter, Paul and Mary\n']
    >>>word_list(text)
    >>>['james', 'fennimore','cooper', 'peter', 'paul', 'and', 'mary']
    """

    token_list = []
    word_list=[]
    for each in text:
        token_list.extend(each.split())   
    for element in token_list:
        s = clean_up(element)
        if(len(s)!=0):
            word_list.append(s)
    return word_list


def create_sentence_list(text):
    
    """(list of str) -> (list of str)
	
    Precondition: text contains at least one sentence.
	
    A sentence is defined as a non-empty string of non-terminating 
    punctuation surrounded by terminating punctuation or beginning or 
    end of file. Terminating punctuation is defined as !?.

    Ruturn the list of  sentences in text.
	
    >>>text = ['The time has come, the Walrus said\n',
         'To talk of many things:ships\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>>sentence_list(text)
    ['The time has come, the Walrus said\nTo talk of many things:ships\nOf cabbages; and kings'
     ,'\nAnd why the sea is boiling hot;\nand whether pigs have wings']
    """
    #Split the text on separators such as '?' ,'!' and '.'
    original_text = ''
    for i in text:
         original_text += i   
    sentence_list = split_on_separators(original_text,'?!.')

    #Delete the end of a file '\n' 
    if sentence_list[-1] == '\n':
        sentence_list.pop()
		
    return sentence_list



def clean_up(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been
    converted to lowercase and punctuation characters have been stripped 
    from both ends. Inner punctuation is left untouched. 

    >>> clean_up('Happy Birthday!!!')
    'happy birthday'
    >>> clean_up("-> It's on your left-hand side.")
    " it's on your left-hand side"
    """
    
    punctuation = """!"',;:.-?)([]<>*#\n\t\r"""
    result = s.lower().strip(punctuation)
    return result


##########  Complete the following functions. ############

def avg_word_length(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the average length of all words in text. 
    
    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul and Mary\n']
    >>> avg_word_length(text)
    5.142857142857143 
    """
    
    # To do: Fill in this function's body to meet its specification.
    word_list = create_word_list(text)
          
    # Cauclate the the number of characters in text
    num_character = 0  
    for element in word_list:
        num_character += len(element)
        
    return num_character/len(word_list)
    

def type_token_ratio(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the Type Token Ratio (TTR) for this text. TTR is the number of
    different words divided by the total number of words.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n',
        'James Gosling\n']
    >>> type_token_ratio(text)
    0.8888888888888888
    """
    
    # To do: Fill in this function's body to meet its specification.
    word_list_once=[]
    word_list = create_word_list(text)
    
    # word_list_once contains all the words that have appeared at least.         
    for element in word_list:
        if  element not in word_list_once:
            word_list_once.append(element)
    
    return len(word_list_once)/len(word_list)
                
def hapax_legomena_ratio(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the hapax legomena ratio for text. This ratio is the number of 
    words that occur exactly once divided by the total number of words.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n',
    'James Gosling\n']
    >>> hapax_legomena_ratio(text)
    0.7777777777777778
    """
 
    # To do: Fill in this function's body to meet its specification.
    num_of_diff_word = 0 
    word_list_once = []
    word_list_twice = []    
    word_list = create_word_list(text)
            
    # word_list_once contains all the words that have appeared at least once.          
    # word_list_twice contains all the words that have appeared at least twice.
    for element in word_list:
        if  element not in word_list_once:
            word_list_once.append(element)
        elif element not in word_list_twice:
            word_list_twice.append(element)
    
    
    return (len(word_list_once)-len(word_list_twice))/len(word_list)
    
    


def split_on_separators(original, separators):
    """ (str, str) -> list of str

    Return a list of non-empty, non-blank strings from original,
    determined by splitting original on any of the separators.
    separators is a string of single-character separators.

    >>> split_on_separators("Hooray! Finally, we're done.", "!,")
    ['Hooray', ' Finally', " we're done."]
    """
    
    # To do: fill in this function's body to meet its specification.
    # You are not required to keep the two lines below but you may find
    # them helpful. (Hint)
    word = ''
    result = []
    
    for char in original:
        if char not in separators:
            word += char
        else:
            if len(word) != 0 :
                result.append(word)
                word = ''
                
    # Append the last word to the result
    if len(word) != 0 :
        result.append(word)            

    return result
                
def avg_sentence_length(text):
    """ (list of str) -> float

    Precondition: text contains at least one sentence.
    
    A sentence is defined as a non-empty string of non-terminating 
    punctuation surrounded by terminating punctuation or beginning or 
    end of file. Terminating punctuation is defined as !?.

    Return the average number of words per sentence in text.   

    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> avg_sentence_length(text)
    17.5
    """
    
    # To do: Fill in this function's body to meet its specification.
    sentence_list = create_sentence_list(text)
    sentence_word_list = create_word_list(sentence_list)
    
    return len(sentence_word_list)/len(sentence_list)
    

def avg_sentence_complexity(text):
    """ (list of str) -> float

    Precondition: text contains at least one sentence.    

    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation or beginning or
    end of file. Terminating punctuation is defined as !?.
    Phrases are substrings of sentences, separated by one or more of ,;:

    Return the average number of phrases per sentence in text.

    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> avg_sentence_complexity(text)
    3.5
    """
    
    # To do: Fill in this function's body to meet its specification.
    sentence_list = create_sentence_list(text)

    phrase_list = []
    for element in sentence_list:
        phrase_list.extend(split_on_separators(element,':,;'))
    
    return len(phrase_list)/len(sentence_list)
    
def compare_signatures(sig1, sig2, weight):
    """ (list, list, list of float) -> float

    Return a non-negative float indicating the similarity of the two 
    linguistic signatures, sig1 and sig2. The smaller the number the more
    similar the signatures. Zero indicates identical signatures.
    
    sig1 and sig2 are 6-item lists with the following items:
    0  : Author Name (a string)
    1  : Average Word Length (float)
    2  : Type Token Ratio (float)
    3  : Hapax Legomena Ratio (float)
    4  : Average Sentence Length (float)
    5  : Average Sentence Complexity (float)

    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.

    >>> sig1 = ["a_string" , 4.4, 0.1, 0.05, 10.0, 2.0]
    >>> sig2 = ["a_string2", 4.3, 0.1, 0.04, 16.0, 4.0]
    >>> weight = [0, 11.0, 33.0, 50.0, 0.4, 4.0]
    >>> compare_signatures(sig1, sig2, weight)
    12.000000000000007
    """
    
    # To do: Fill in this function's body to meet its specification.
    temp_list=[0,0,0,0,0,0]
    for i in range(1,len(sig1)):
        temp_list[i] = abs(sig1[i] - sig2[i]) * weight[i]

    result=sum(temp_list)
    return result
