# Bambara Tokenizer

Advanced tokenization toolkit for the Bambara language (Bamanankan)

Name="bambara-tokenizer",

Version="1.0.0",

Author="Mahamadou Golomanta",

Author_email="pelengana1@example.com",

Description="Advanced tokenizer for the Bambara language",

url="https://github.com/mgolomanta/bambara-tokenizer",

Programming Language :: Python :: 3,

License :: OSI Approved :: MIT License,

Operating System :: OS Independent,

python_requires='>=3.6',

keywords='nlp bambara tokenizer african-languages',

## Basic Usage
from bambara_tokenizer import BambaraTokenizer

text = "N’tɛ donni kɛnɛya 1000 la."
tokenizer = BambaraTokenizer(
    lowercase=True,
    split_compounds=True
)

print(tokenizer.tokenize(text))
# Output: ['ne', 'tɛ', 'donni', 'kɛnɛya', '<NUM_1000>', 'la']
