# Bambara Tokenizer

Advanced tokenization toolkit for the Bambara language (Bamanankan)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bambara-tokenizer",
    version="1.0.0",
    author="Mahamadou Golomanta",
    author_email="pelengana1@example.com",
    description="Advanced tokenizer for the Bambara language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mgolomanta/bambara-tokenizer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords='nlp bambara tokenizer african-languages',
)



## Basic Usage
from bambara_tokenizer import BambaraTokenizer

text = "N’tɛ donni kɛnɛya 1000 la."
tokenizer = BambaraTokenizer(
    lowercase=True,
    split_compounds=True
)

print(tokenizer.tokenize(text))
# Output: ['ne', 'tɛ', 'donni', 'kɛnɛya', '<NUM_1000>', 'la']
