from setuptools import setup, find_packages

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
