## Basic Usage
from bambara_tokenizer import BambaraTokenizer

text = "N’tɛ donni kɛnɛya 1000 la."
tokenizer = BambaraTokenizer(
    lowercase=True,
    split_compounds=True
)

print(tokenizer.tokenize(text))