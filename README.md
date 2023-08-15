Text Processing and Analysis

Description:
This project focuses on text processing and analysis using Python and various libraries such as pandas, nltk, and matplotlib. It includes several functions to preprocess text data, generate word counts, filter data based on specific keywords, and visualize the results. This project aims to analyze and visualize data from the processed_data1.xlsx file. The data consists of information related to newsletters and their content. The analysis includes calculating word counts and creating visualizations to understand the distribution of certain keywords.

Preprocess Text Data: The preprocess_text function removes special characters, normalizes text, and converts it to lowercase. It can be applied to a column in a pandas DataFrame using the apply method.
Generate Word Counts: The generate_word_counts function reads an Excel file, tokenizes the text, removes stopwords, lemmatizes words, and counts their occurrences. It returns a DataFrame with the top 200 words and their variations.
Filter Data: The filter_data function filters a DataFrame based on specific keywords in the 'icerik' column. It uses regular expressions to match the keywords and returns the filtered data.
Visualize Word Counts: The visualize_word_counts function reads two Excel files, calculates the word counts for specific keywords, and visualizes the results using a horizontal bar chart. It shows the word counts for each year and the percentage change between them.
