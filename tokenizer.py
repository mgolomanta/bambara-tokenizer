import re
from collections import defaultdict

class BambaraTokenizer:
    def __init__(self, lowercase=False, remove_punct=False, custom_stopwords=None,
                 keep_contractions=True, split_compounds=False):
        """
        Bambara Tokenizer with configurable options
        
        Parameters:
        - lowercase: Convert text to lowercase (default: False)
        - remove_punct: Remove punctuation (default: False)
        - custom_stopwords: List of custom stopwords to remove (optional)
        - keep_contractions: Preserve contracted forms (default: True)
        - split_compounds: Split hyphenated compounds (default: False)
        """
        # Existing initialization
        self.lowercase = lowercase
        self.remove_punct = remove_punct
        self.stopwords = set(custom_stopwords) if custom_stopwords else set()
        self.bambara_special = "'’-"
        self.keep_contractions = keep_contractions
        self.split_compounds = split_compounds
        
        # Enhanced regex pattern
        self.word_pattern = re.compile(
            r"""
            ([\w""" + re.escape(self.bambara_special) + r"""]+(?:-\w+)*)  # Improved compound handling
            |([!"#$%&'()*+,./:;<=>?@[\\\]^_`{|}~])  # Punctuation
            |(\d[\d,.]*)  # Number detection
            """, re.UNICODE | re.VERBOSE
        )

        # Language-specific configurations
        self.contraction_map = {
            "n’": "ne",
            "m’": "ma",
            "t’": "te",
            "b’": "be"
        }

    # Existing methods remain here
    
    def split_contractions(self, token):
        """Split and expand common Bambara contractions"""
        if self.keep_contractions:
            return [token]
            
        for contraction, expansion in self.contraction_map.items():
            if token.startswith(contraction):
                return [expansion, token[len(contraction):]]
        return [token]

    def handle_compounds(self, token):
        """Process hyphenated compounds based on configuration"""
        if self.split_compounds and '-' in token:
            return token.split('-')
        return [token]

    def tokenize(self, text):
        """Enhanced tokenization with new features"""
        text = self.preprocess(text)
        tokens = self.word_pattern.findall(text)
        tokens = [t[0] or t[1] or t[2] for t in tokens if any(t)]
        
        processed = []
        for token in tokens:
            # Handle numbers
            if token.isdigit():
                processed.append(f'<NUM_{token}>')
                continue
                
            # Process contractions
            token_parts = self.split_contractions(token)
            
            # Process compounds
            for part in token_parts:
                compound_parts = self.handle_compounds(part)
                processed.extend(compound_parts)
        
        # Existing filtering logic
        processed = [
            t.lower() if self.lowercase else t
            for t in processed
            if t not in self.stopwords and (not self.remove_punct or t.isalpha())
        ]
        
        return processed

    def sentence_tokenize(self, text):
        """Sentence tokenization for Bambara"""
        sentence_end = re.compile(r'([.!?]+\s*)')
        sentences = sentence_end.split(text)
        return [s.strip() for s in sentences if s.strip()]

    def get_word_frequency(self, text):
        """Generate word frequency statistics"""
        tokens = self.tokenize(text)
        freq = defaultdict(int)
        for token in tokens:
            freq[token] += 1
        return freq

    def normalize_diacritics(self, text):
        """Normalize alternative diacritic representations"""
        replacements = {
            'ɛ': 'è',
            'ɔ': 'ò',
            'ɲ': 'ñ'
        }
        for k, v in replacements.items():
            text = text.replace(k, v)
        return text

    def detect_non_bambara(self, tokens):
        """Identify potential non-Bambara words"""
        bambara_chars = re.compile(r'^[\w\'’-]+$', re.UNICODE)
        return [t for t in tokens if not bambara_chars.match(t)]

    def generate_ngrams(self, text, n=2):
        """Generate character n-grams for words"""
        tokens = self.tokenize(text)
        return [''.join(ngram) for token in tokens 
                for ngram in zip(*[token[i:] for i in range(n)])]

    def export_tokens(self, tokens, filename):
        """Export tokens to file"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(tokens))

    def add_domain_words(self, word_list):
        """Add domain-specific vocabulary handling"""
        self.domain_words = set(word_list)
        
    def analyze_morphology(self, token):
        """Basic morphological analysis (stub for extension)"""
        # Common Bambara suffixes
        suffixes = ['-la', '-ma', '-ya', '-w']
        for suffix in suffixes:
            if token.endswith(suffix):
                return {'root': token[:-len(suffix)], 'suffix': suffix}
        return {'root': token, 'suffix': None}

# Example usage of new features
if __name__ == "__main__":
    text = "N’tɛ donni kɛnɛya 1000 la. Aw ye kalo 12 sɔrɔ! Tɔgɔ-ɲuman ye diya ye."
    
    tokenizer = BambaraTokenizer(
        lowercase=True,
        split_compounds=True,
        custom_stopwords=['ye']
    )
    
    print("Enhanced Tokenization:", tokenizer.tokenize(text))
    print("Sentence Tokenization:", tokenizer.sentence_tokenize(text))
    print("Word Frequency:", tokenizer.get_word_frequency(text))
    print("Morphological Analysis:", tokenizer.analyze_morphology("tɔgɔ-ɲuman"))