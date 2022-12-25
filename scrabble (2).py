from wordscore import score_word

def run_scrabble(input):
    """
Return two items from the run_scrabble function:
1) The total list of valid Scrabble words that can be constructed from the rack as (score, word) tuples, sorted by the score and then by the word alphabetically as shown in the first example below. All outputted words need to be in upper case.
2) The Total number of valid words as an integer
    """
    with open("sowpods.txt","r") as file:
        raw_input = file.readlines()
        words_data = [raw.strip('\n') for raw in raw_input]
    
    rack = input.upper()
    
    #Handle edge cases and return string
    if len(rack) < 2:
        return "Your input must be between 2-7 characters. Try again."
    elif len(rack) > 7:
        return "Your input must be between 2-7 characters. Try again."
    if (rack.count('?') > 2) or (rack.count('*') > 2):
        return "You have too many special characters. Try again."
        
    words_and_scores = [(score_word(word), word.upper()) for word in find_valid_words(rack, words_data)]
    #handle wildcards
    if '?' in rack or '*' in rack:
        words_and_scores.extend(handle_wildcards(rack, words_data))
        
    #sort alphabetically first then by scores
    sorted_alphabetically = sorted(words_and_scores, key= lambda a: a[1])
    sorted_scores = sorted(sorted_alphabetically, key = lambda b: b[0], reverse=True)
    return sorted_scores, len(sorted_scores)

def handle_wildcards(rack, data):
    #handle three cases for wildcards (maximum of 2)
    #first case is when only ? is present and * is not
    #second case is when only * is present and ? is not
    #third case is when both are present
    #otherwise scrabble works as intended
    import string
    
    good_rack = rack.replace('?', '').replace('*', '')
    valid_words = find_valid_words(good_rack, data)
    words_and_scores = [(score_word(word), word.upper()) for word in valid_words]

    if '?' in rack and '*' not in rack:
        for letter in list(string.ascii_uppercase):
            attempt = rack.replace('?', letter)
            words = find_valid_words(attempt, data)
            words_and_scores.extend([(score_word(word)-score_word(letter), 
                                      word.upper()) for word in words if word not in valid_words])
            valid_words.extend(words)
            valid_words.extend(attempt)
            
    elif '*' in rack and '?' not in rack:    
        for letter in list(string.ascii_uppercase):
            attempt = rack.replace('*', letter)
            words = find_valid_words(attempt, data)
            words_and_scores.extend([(score_word(word)-score_word(letter), 
                                      word.upper()) for word in words if word not in valid_words])
            valid_words.extend(words)
            valid_words.extend(attempt)
            
    elif '?' in rack and '*' in rack:
        for letter in list(string.ascii_uppercase):
            first = rack.replace('?', letter)
            for second_letter in list(string.ascii_uppercase):
                second = first.replace('*', second_letter)
                words = find_valid_words(second, data)
                words_and_scores.extend([(score_word(word)-score_word(second_letter), 
                                          word.upper()) for word in words if word not in valid_words])
                valid_words.extend(words)
                valid_words.extend(second)
    return words_and_scores

def find_valid_words(rack, data):
    
    valid_words = []
    for word in data:
        inputs = list(rack)
        for i, letter in enumerate(word):
            if letter in inputs:
                inputs.remove(letter)
            else:
                break
            if i == len(word) - 1:
                valid_words.append(word)
    return valid_words