import streamlit as st
import re

def count_vowels(text: str) -> int:
    """Returns the count of vowels in a given text."""
    return sum(1 for char in text if char.lower() in "aeiou")

def analyze_text(text: str) -> dict:
    """Performs text analysis and returns key statistics."""
    words = text.split()
    total_words = len(words)
    total_chars = len(text)
    vowels_count = count_vowels(text)
    
    avg_word_length = round(total_chars / total_words, 2) if total_words > 0 else 0
    contains_python = "Python" in text

    return {
        "total_words": total_words,
        "total_chars": total_chars,
        "vowels_count": vowels_count,
        "avg_word_length": avg_word_length,
        "contains_python": contains_python
    }

def text_analyzer():
    """Streamlit app for text analysis."""
    st.title("📊 Advanced Text Analyzer")
    st.write("Analyze your text with detailed statistics and transformations.")

    text = st.text_area("Enter a paragraph:", "")

    search_word = st.text_input("Word to search:", key="search_word")
    replace_word = st.text_input("Word to replace it with:", key="replace_word")

    if st.button("Analyze Text"):
        if not text.strip():
            st.warning("Please enter a valid paragraph.")
            return

        stats = analyze_text(text)

        st.subheader("🔍 Text Statistics")
        st.write(f"**Total Words:** {stats['total_words']}")
        st.write(f"**Total Characters:** {stats['total_chars']}")
        st.write(f"**Number of Vowels:** {stats['vowels_count']}")
        st.write(f"**Average Word Length:** {stats['avg_word_length']}")
        st.write(f"**Contains 'Python'?** {'✅ Yes' if stats['contains_python'] else '❌ No'}")

        modified_text = re.sub(rf"\b{re.escape(search_word)}\b", replace_word, text) if search_word else text

        st.subheader("📝 Modified Paragraph")
        st.text_area("Updated Text:", modified_text, height=150)

        st.subheader("🔠 Text Transformations")
        st.text_area("Uppercase:", text.upper(), height=100)
        st.text_area("Lowercase:", text.lower(), height=100)

if __name__ == "__main__":
    text_analyzer()
