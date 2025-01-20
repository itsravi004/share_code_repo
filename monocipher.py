import streamlit as st
from collections import Counter
import re

def analyze_frequency(text):
    """Analyze letter frequencies in the text."""
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_text = re.sub(r'[^a-z]', '', text.lower())
    
    # Count frequencies
    freq = Counter(cleaned_text)
    total = sum(freq.values())
    
    # Convert to percentages
    freq_percent = {char: (count/total)*100 for char, count in freq.most_common()}
    return freq_percent

def find_bigrams(text):
    """Find most common bigrams in the text."""
    cleaned_text = re.sub(r'[^a-z]', '', text.lower())
    bigrams = [cleaned_text[i:i+2] for i in range(len(cleaned_text)-1)]
    return Counter(bigrams).most_common(10)

def find_trigrams(text):
    """Find most common trigrams in the text."""
    cleaned_text = re.sub(r'[^a-z]', '', text.lower())
    trigrams = [cleaned_text[i:i+3] for i in range(len(cleaned_text)-2)]
    return Counter(trigrams).most_common(10)

def decrypt(text, key):
    """Decrypt text using the substitution key."""
    result = ""
    for char in text:
        if char.lower() in key:
            # Preserve case
            if char.isupper():
                result += key[char.lower()].upper()
            else:
                result += key[char.lower()]
        else:
            result += char
    return result

def main():
    st.title("Simple Cipher Analyzer")
    
    # Input area for cipher text
    cipher_text = st.text_area("Enter cipher text:", height=200)
    
    if cipher_text:
        # Analyze frequencies
        frequencies = analyze_frequency(cipher_text)
        bigrams = find_bigrams(cipher_text)
        trigrams = find_trigrams(cipher_text)
        
        # Display analysis
        st.subheader("Analysis")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write("Letter Frequencies")
            for char, freq in frequencies.items():
                st.write(f"{char}: {freq:.2f}%")
                
        with col2:
            st.write("Common Bigrams")
            for bigram, count in bigrams:
                st.write(f"{bigram}: {count}")
                
        with col3:
            st.write("Common Trigrams")
            for trigram, count in trigrams:
                st.write(f"{trigram}: {count}")
        
        # Known substitutions for Gettysburg Address
        key = {
            's': 'a', 'c': 'b', 'd': 'c', 'v': 'd', 'i': 'e',
            'j': 'f', 'g': 'g', 'x': 'h', 't': 'i', 'w': 'j',
            'k': 'k', 'o': 'l', 'm': 'm', 'l': 'n', 'e': 'o',
            'u': 'p', 'n': 'q', 'k': 'r', 'r': 's', 'q': 't',
            'y': 'u', 'h': 'v', 'f': 'w', 'a': 'y', 'b': 'z'
        }
        
        # Decrypt button
        if st.button("Decrypt"):
            decrypted = decrypt(cipher_text, key)
            st.subheader("Decrypted Text")
            st.write(decrypted)

if __name__ == "__main__":
    main()