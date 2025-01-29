# Bambara Tokenizer

Advanced tokenization toolkit for the Bambara language (Bamanankan)

## Installation

```bash
pip install -e .


## Basic Usage
from bambara_tokenizer import BambaraTokenizer

text = "N’tɛ donni kɛnɛya 1000 la."
tokenizer = BambaraTokenizer(
    lowercase=True,
    split_compounds=True
)

print(tokenizer.tokenize(text))
# Output: ['ne', 'tɛ', 'donni', 'kɛnɛya', '<NUM_1000>', 'la']
