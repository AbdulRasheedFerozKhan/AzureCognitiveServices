```python
import nltk
import re
import unicodedata
import numpy as np
from gensim.summarization import summarize
nltk.download('punkt')
```

    [nltk_data] Downloading package punkt to /home/azureuser/nltk_data...
    [nltk_data]   Unzipping tokenizers/punkt.zip.





    True




```python
def clean_and_parse_document(document):
    document = re.sub('\n', ' ', document)
    document = document.strip()
    sentences = nltk.sent_tokenize(document)
    sentences = [sentence.strip() for sentence in sentences]
    return sentences
```


```python
def summarize_text(text, summary_ratio=None, word_count=30):
    sentences = clean_and_parse_document(text)
    cleaned_text = ' '.join(sentences)
    summary = summarize(cleaned_text, split=True, ratio=summary_ratio, word_count=word_count)
    return summary
```


```python
example_document = """
I was driving down El Camino and stopped at a red light.
It was about 3pm in the afternoon.  
The sun was bright and shining just behind the stoplight.
This made it hard to see the lights.
There was a car on my left in the left turn lane.
A few moments later another car, a black sedan pulled up behind me. 
When the left turn light changed green, the black sedan hit me thinking 
that the light had changed for us, but I had not moved because the light 
was still red.
After hitting my car, the black sedan backed up and then sped past me.
I did manage to catch its license plate. 
The license plate of the black sedan was ABC123. 
"""
```


```python
summarize_text(example_document)
```




    ['When the left turn light changed green, the black sedan hit me thinking  that the light had changed for us, but I had not moved because the light  was still red.',
     'The license plate of the black sedan was ABC123.']




```python

```
