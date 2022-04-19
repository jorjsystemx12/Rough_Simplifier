# Module: Intermediate Methods and Programming in Digital Linguistics
# Semester: Spring 2021
# Main Project - Final Version ReadMe

## Table of Contents
- Requirement and Packages
- General Info
- Input and Output Guide
- Bibliography

## Requirements
- Python 3.5 and more recent
- NLTK (Natural Language Toolkit) -> Latest version at 3.5
- NLTK - POS Tagger & WordNET
- Text file with 1-2 sentence to simply (.txt format in UTF-8 encoding)
- SpaCy (Latest Version)
- Regular Expression (re)
- Operating System: Windows, Mac OS, Linux
- EASSE installation (provided a master copy in .zip format or to download - link in Bibliography)

## General Info
The following program "simplifier.py" in Python is a naive simplifier. Program to simplify sentences (input of str in .txt file) with numbers of nouns through clarification, removal of adjective/adverbs and brackets. Mix usage of WordNET, SpaCy, NLTK tokenizer and regular expression.
Furthermore, the converted strings will be compared with easy wikipedia entries through metric score evaluation - done separately through EASSE with separate bash terminal with EASSE installed.

#### Input and output Guide
Input: 1x text (.txt) file containing 1-2 sentences (separated with punctuation , or .)
Output: 1x text (.txt) file with the modified/simplified sentence(s).

'''command prompt''' --> C:\Users\File python simplifier.py {text_file_with_1_or_2_sentences_to_simplify.txt}

Example:
Input --> "A vitamin is an organic molecule (or a set of molecules closely related chemically, i.e. vitamers) that is an essential micronutrient which an organism needs in small quantities for the proper functioning of its metabolism."
Output --> "a vitamin, defined as any of a group of substances in quantities to metabolism, an molecule, defined as the unit of an element or compound, an micronutrient, defined as a substance needed in amounts for body function, which an organism , defined as a living thing has the ability to act or function , needs in quantities for the functioning , defined as performing or to perform its function , of its metabolism , defined as the processes are for life."


## Bibliography
- “Simplification.” NLP, NLP-Progress, nlpprogress.com/english/simplification.html. 
- Manchego, Fernando Alva, and Louis Martin. “Feralvam/Easse.” GitHub, 4 Mar. 2019, github.com/feralvam/easse.