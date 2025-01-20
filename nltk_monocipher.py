import streamlit as st
import pandas as pd
from collections import Counter
from textblob import TextBlob
import re

# Most common letters in English language (by frequency)
ENGLISH_FREQUENCIES = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'.lower()

def get_frequency_analysis(text):
    # Clean the text and convert to lowercase
    text = re.sub(r'[^a-zA-Z]', '', text.lower())
    
    # Get frequency of each character
    freq = Counter(text)
    
    # Convert to percentage and sort
    total = sum(freq.values())
    freq_percent = {k: (v/total)*100 for k, v in freq.items()}
    freq_sorted = dict(sorted(freq_percent.items(), key=lambda x: x[1], reverse=True))
    
    return freq_sorted

def get_ngrams(text, n):
    # Clean the text and convert to lowercase
    text = re.sub(r'[^a-zA-Z]', '', text.lower())
    
    # Generate n-grams
    ngrams = [text[i:i+n] for i in range(len(text)-n+1)]
    
    # Count frequencies
    freq = Counter(ngrams)
    
    # Sort by frequency
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

def create_mapping(freq_analysis):
    # Get sorted cipher text letters by frequency
    cipher_letters = list(freq_analysis.keys())
    
    # Create initial mapping based on frequency analysis
    mapping = {}
    for i, letter in enumerate(cipher_letters):
        if i < len(ENGLISH_FREQUENCIES):
            mapping[letter] = ENGLISH_FREQUENCIES[i]
    
    return mapping

def decode_text(cipher_text, mapping):
    decoded_text = ''
    for char in cipher_text.lower():
        if char.isalpha():
            decoded_text += mapping.get(char, char)
        else:
            decoded_text += char
    return decoded_text

def main():
    st.title("Cipher Text Analysis and Decoder Tool")
    
    # Input text area
    cipher_text = st.text_area("Enter your cipher text:", height=200)
    
    if cipher_text:
        # Single letter frequency analysis
        st.subheader("Letter Frequency Analysis")
        freq_analysis = get_frequency_analysis(cipher_text)
        
        # Convert to DataFrame for better display
        df_freq = pd.DataFrame(freq_analysis.items(), columns=['Letter', 'Frequency (%)'])
        st.table(df_freq)
        
        # Bi-grams analysis
        st.subheader("Bi-grams Analysis")
        bigrams = get_ngrams(cipher_text, 2)
        df_bigrams = pd.DataFrame(list(bigrams.items())[:10], columns=['Bi-gram', 'Count'])
        st.table(df_bigrams)
        
        # Tri-grams analysis
        st.subheader("Tri-grams Analysis")
        trigrams = get_ngrams(cipher_text, 3)
        df_trigrams = pd.DataFrame(list(trigrams.items())[:10], columns=['Tri-gram', 'Count'])
        st.table(df_trigrams)
        
        # Text statistics using TextBlob
        st.subheader("Text Statistics")
        blob = TextBlob(cipher_text)
        stats = {
            'Word Count': len(blob.words),
            'Character Count': len(cipher_text),
            'Sentence Count': len(blob.sentences)
        }
        df_stats = pd.DataFrame(stats.items(), columns=['Metric', 'Value'])
        st.table(df_stats)
        
        # Decoding section
        st.subheader("Decoded Text (Based on Frequency Analysis)")
        
        # Create initial mapping based on frequency analysis
        mapping = create_mapping(freq_analysis)
        
        # Display current mapping
        st.write("Current Letter Mapping:")
        mapping_df = pd.DataFrame([mapping]).T.reset_index()
        mapping_df.columns = ['Cipher Letter', 'Decoded Letter']
        st.table(mapping_df)
        
        # Allow manual mapping adjustments
        st.write("Adjust Mapping:")
        col1, col2 = st.columns(2)
        with col1:
            cipher_letter = st.text_input("Cipher Letter:", max_chars=1)
        with col2:
            plain_letter = st.text_input("Should Decode To:", max_chars=1)
            
        if cipher_letter and plain_letter:
            mapping[cipher_letter.lower()] = plain_letter.lower()
            st.experimental_rerun()
        
        # Display decoded text
        decoded = decode_text(cipher_text, mapping)
        st.write("Decoded text:")
        st.write(decoded)
        
        # Add a reset mapping button
        if st.button("Reset Mapping"):
            mapping = create_mapping(freq_analysis)
            st.experimental_rerun()

if __name__ == "__main__":
    main()