def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    words = []
    for sentence in sentences:
      for word in sentence:
        words.append(word)
    
    unique_words = list(set(words))

    word_count = {}

    for unique_word in unique_words:
      count = 0
      for word in words:
        if unique_word.lower() == word.lower():
          count += 1
      word_count[unique_word] = count
    
    return word_count