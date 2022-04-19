#Intermediate Methods and Programming in Digital Linguistics
#Author: George Y.
#Assignment: Main Project - Final Edition
#Number & Semester: #2 Spring 2021
#Encoding: UTF-8

""" Program to simplify sentence (input of str in .txt file) with numbers of proper names, selected lingo
    into easier accessible strings. Simplification through splitting, shortening and clarification with noun definition.
    Furthermore, the converted strings will be compared with easy wikipedia entries through metric 
    score evaluation - done separately through EASSE with separate script and instructions.
    
    Recommendation - use with .txt files with 1-2 sentences. Generates output of text (.txt) file with the simplified
    sentence. Use of multiple tools and packages - WordNet, SpaCy and Regular Expression. Executed through CLI
    interface through ArgParse. """

#Import main tools for simplification:
import sys #in order to read the text files
from argparse import ArgumentParser, FileType #Parser controls to be added at the end
import spacy #Tokenized words will need to be POS tagged in order to remove adjective/adverbs and identify nouns
import re #Replacement of conjuctions with full stops
from nltk.corpus import wordnet as wn #Break down the definition of all nouns to extend clarity
from nltk.tokenize import word_tokenize #Word tokenizer to enable WordNet use.
import nltk.data #Required for nltk and WordNet
import nltk #Import NLTK
from argparse import ArgumentParser, FileType # Argument parser needed for CLI interface

#Main simplying task

# Load the pretrained neural net
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
#Have English SpaCy Language setup - NOTE: Large English language option:
nlp = spacy.load('en_core_web_trf')


#Empty containers:
definitions = {}
finalized = []
done_defined = []
#Empty List to insert materials based on highlighter.py
#Empty list to insert ADJ, ADV:
ad_au = []
#Empty list to insert main final completed text:
final_text = []


#Main Parser for CLI
def get_argument_parser(description) -> ArgumentParser:
    parser = ArgumentParser(description = 'Sentence simplifier for simple text files with 1-2 sentences in English')
    parser.add_argument('filename')
    return parser


#Tokenize the text file
def token_wn(f):
    text = word_tokenize(f)
    return text


#POS tag breakdown of tokens with NLTK POS tagger:
def token_pos(text):
    tagged = nltk.pos_tag(text)
    return tagged


#Connect definition clarification:
def clarify(definition):
    clarified = ' '.join(finalized)
    return clarified


#Functions for Regular Expression to Clean up:
#Remove double commas
def comma_buster(phase_tri):
    remove_comma = re.sub(', ,',',', phase_tri)
    return remove_comma


#Remove parenthesis:
def bracket_buster(clean_one):
    empty_bracket = re.sub(r'\([^)]*\)', '', clean_one)
    return empty_bracket


#Clean up spaces:
def space_cleaner(clean_two):
    spaces_no = re.sub('  ',' ', clean_two)
    return spaces_no


#Get rid of weird surplus punctuations:
def punct_no(clean_three):
    no_fs = re.sub(' \, \.','.', clean_three)
    return no_fs


#Spacy 1: Adjective and Adverb finder:
def adj_adv(doc):
    for token in doc:
        #print(token.text, token.pos_)
        if token.pos_ == 'ADJ':
            #print(token.text)
            ad_au.append(token.text)
        elif token.pos_ == 'ADV':
            ad_au.append(token.text)

    return ad_au


#Final output with removal of ADJ/ADV:
def output_cuts(doc):
    clean_final = ' '
    for elem in doc:
        if elem.text in ad_au:
            pass
        else:
            final_text.append(elem.text)
    return final_text


#Conver the list of the words of the simplified end result:
def listToString(spacy_two):
    str1 = ' '
    return (str1.join(spacy_two))


#Generate external text file with the calculated weights from before:
#Open new file to write
def generated_text(final_simplified):
    with open('simplified_text.txt','w',encoding='utf-8') as new_file_print:
        new_file_print.write(final_simplified)


#Main function of the program
def main():
    # Parse command line arguments
    parser = get_argument_parser(description = 'Sentence simplifier for simple text files with 1-2 sentences in English')
    args = parser.parse_args()
    #Read the file that is typed in the CLI interface, then lower case the whole text
    with open(args.filename, 'r', encoding='utf-8') as f:    
        f = f.read()
        f = f.lower()
        #print(f)
    #Tokenize the words in the text
    maintext = token_wn(f)
    #print(maintext)
    #Attach POS tags to the tokenized words:
    taggedup = token_pos(maintext)
    #print(text)
    #Wordnet Definition extraction:
    for i in range(0,len(maintext)):
        #Use the first definition of interest
        for syns in wn.synsets(maintext[i]):
            if not syns.name().split('.')[0] in definitions:
                if len(taggedup[i][0]) > 1:
                    #Pick out all the noun and nouns that have been tokenized and POS tagged:
                    if taggedup[i][1] == 'NN' or taggedup[i][1] == 'NNS':
                        definitions[syns.name().split('.')[0]] = syns.definition()
                        #print(syns.name().split('.')[0], definitions[syns.name().split('.')[0]])
                        #print('\n')
    #print(definitions)
    #Definition replacement
    for i in range(0,len(maintext)):
        finalized.append(maintext[i])
        if maintext[i] in definitions and maintext[i] not in done_defined:
            finalized.append(', defined as')
            finalized.append(definitions[maintext[i]])
            finalized.append(',')
            done_defined.append(maintext[i])
    phase_tri = clarify(definitions)
    #print(phase_tri)
    #Start of Regular Expression functions used to glean the extended and clarified text:
    clean_one = comma_buster(phase_tri)
    #print(clean_one)
    clean_two = bracket_buster(clean_one)
    #print(clean_two)
    clean_three = space_cleaner(clean_two)
    #print(clean_three)
    clean_final = punct_no(clean_three)
    #print(clean_final)
    #Spacy processing to get rid of Adverbs and Adjectives:
    #Main document for NLP
    doc = nlp(clean_final)
    #adv/adj identified and placed in list:
    spacy_one = adj_adv(doc)
    #print(spacy_one)
    spacy_two = output_cuts(doc)
    #print(spacy_two)
    #Final output of two products:
    #Convert the list to a full string for enabled CLI interface reading:
    final_simplified = listToString(spacy_two)
    #Write text file with naively simplified text:
    print_up = generated_text(final_simplified)
    #Read the final output
    print(final_simplified)
 
 
#def main(input --> text (.txt) file, output --> textfile: str and printed text):
if __name__ == '__main__':
    main()
