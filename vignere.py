import streamlit as st
import numpy as np
from collections import Counter
import string

def find_repeated_sequences(text, seq_length=3):
    """
    Kasiski Examination: Find repeating sequences and their distances
    
    Args:
        text (str): Cipher text
        seq_length (int): Length of sequences to look for
    
    Returns:
        dict: Dictionary of sequences and their positions
    """
    sequences = {}
    for i in range(len(text) - seq_length + 1):
        seq = text[i:i + seq_length]
        if seq in sequences:
            sequences[seq].append(i)
        else:
            sequences[seq] = [i]
    # Filter sequences that appear more than once
    return {k: v for k, v in sequences.items() if len(v) > 1}

def calculate_ioc(text):
    """
    Calculate Index of Coincidence for text
    
    Args:
        text (str): Text to analyze
    
    Returns:
        float: Index of Coincidence
    """
    n = len(text)
    if n < 2:
        return 0
    
    freqs = Counter(text)
    numerator = sum(f * (f - 1) for f in freqs.values())
    denominator = n * (n - 1)
    return numerator / denominator if denominator != 0 else 0

def find_key_length(ciphertext, max_length=20):
    """
    Find most likely key length using IoC
    
    Args:
        ciphertext (str): Cipher text
        max_length (int): Maximum key length to try
    
    Returns:
        int: Most likely key length
    """
    ioc_scores = []
    
    for length in range(1, min(max_length + 1, len(ciphertext))):
        groups = [''.join(ciphertext[i::length]) for i in range(length)]
        avg_ioc = sum(calculate_ioc(group) for group in groups) / length
        ioc_scores.append((length, avg_ioc))
    
    # English text typically has IoC around 0.067
    # Return length with IoC closest to English text
    return max(ioc_scores, key=lambda x: x[1])[0]

def analyze_frequency(text):
    """
    Perform frequency analysis on text
    
    Args:
        text (str): Text to analyze
    
    Returns:
        dict: Letter frequencies
    """
    total = len(text)
    freqs = Counter(text)
    return {char: count/total for char, count in freqs.items()}

def determine_key(ciphertext, key_length):
    """
    Determine the encryption key
    
    Args:
        ciphertext (str): Cipher text
        key_length (int): Length of the key
    
    Returns:
        str: Most likely key
    """
    # English letter frequencies (from most to least common)
    eng_freqs = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    key = ''
    
    # Split text into groups by key position
    for i in range(key_length):
        group = ciphertext[i::key_length]
        freqs = analyze_frequency(group)
        
        # Sort letters by frequency
        sorted_freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
        
        # Assume most frequent letter corresponds to 'E'
        shift = (ord(sorted_freqs[0][0]) - ord('E')) % 26
        key += chr((shift + ord('A')) % 26)
    
    return key

def decrypt_vigenere(ciphertext, key):
    """
    Decrypt Vigenère cipher
    
    Args:
        ciphertext (str): Cipher text
        key (str): Decryption key
    
    Returns:
        str: Decrypted text
    """
    decrypted = ''
    key_length = len(key)
    
    for i, char in enumerate(ciphertext):
        if char in string.ascii_letters:
            # Convert to 0-25 range
            key_shift = ord(key[i % key_length].upper()) - ord('A')
            char_code = ord(char.upper()) - ord('A')
            
            # Decrypt and convert back to letter
            decrypted_code = (char_code - key_shift) % 26
            decrypted += chr(decrypted_code + ord('A'))
        else:
            decrypted += char
            
    return decrypted

def main():
    st.title("Vigenère Cipher Cracker")
    
    # Input
    ciphertext = st.text_area("Enter cipher text:", height=100).upper()
    
    if st.button("Crack Cipher") and ciphertext:
        # Clean input - remove non-letters
        cleaned_text = ''.join(c for c in ciphertext if c in string.ascii_uppercase)
        
        # Step 1: Find repeated sequences
        st.subheader("Step 1: Repeated Sequences")
        sequences = find_repeated_sequences(cleaned_text)
        st.write("Found repeating sequences and their positions:")
        st.write(sequences)
        
        # Step 2: Find key length
        st.subheader("Step 2: Key Length Analysis")
        key_length = find_key_length(cleaned_text)
        st.write(f"Most likely key length: {key_length}")
        
        # Step 3: Frequency Analysis
        st.subheader("Step 3: Frequency Analysis")
        freqs = analyze_frequency(cleaned_text)
        st.bar_chart(freqs)
        
        # Step 4: Determine key
        st.subheader("Step 4: Key Determination")
        key = determine_key(cleaned_text, key_length)
        st.write(f"Probable key: {key}")
        
        # Step 5: Decrypt
        st.subheader("Step 5: Decryption")
        decrypted = decrypt_vigenere(cleaned_text, key)
        st.text_area("Decrypted text:", value=decrypted, height=100)
        
        # Additional Statistics
        st.subheader("Additional Statistics")
        st.write(f"Text length: {len(cleaned_text)}")
        st.write(f"Unique characters: {len(set(cleaned_text))}")
        ioc = calculate_ioc(cleaned_text)
        st.write(f"Index of Coincidence: {ioc:.4f}")

if __name__ == "__main__":
    main()