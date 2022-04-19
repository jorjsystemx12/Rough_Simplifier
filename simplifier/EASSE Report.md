# Module: Intermediate Methods and Programming in Digital Linguistics
# Semester: Spring 2021
# Main Project - EASSE and Research Report

## Table of Contents
- Setup (For EASSE) + Method
- EASSE Experiment Report - Results
- Conclusion
- Bibliography

#### Setep and Method
The other element of this main project involves evaluation of the simplifier output. Based on the NLP-progress website, simplification is generally performed by human in order to simplify text resources while maintaining the context and semantic structure of the input. Furthermore, syntax is still vital in ensuring that the output sentence(s) retain fluency.

Hypothesis: The simplifier output will generate sentences with clarified nouns which are suitable with lexicon that are specialized in a particular field of knowledge, furthermore the cutting of adjective and adverbs will preserve the core definitions and meaning of the sentence.

Dependent variable: EASSE Score (numerical float value)
Independent variable(s): Length of the sentence, number of nouns and complexity of the syntactic structure (presence of Auxilary phrases or multi-component words)

EASSE experimet requires:
- EASSE Installed.
- Original sentence (1 or 2 sentences)
- 'Simplified' sentence genererated by simplifier script.
- 3 human user written reference sentences (refs_sents) which are simplified variants of the original sentence(s) --> must be of the same number of sentences and as closely related to original sentence.

#### Results
corpus_sari(orig_sents=["A vitamin is an organic molecule (or a set of molecules closely related chemically, i.e. vitamers) that is an essential micronutrient which an organism needs in small quantities for the proper functioning of its metabolism."],  
            sys_sents=["a vitamin, defined as any of a group of substances in quantities to metabolism, an molecule, defined as the unit of an element or compound, an micronutrient, defined as a substance needed in amounts for body function, which an organism , defined as a living thing has the ability to act or function , needs in quantities for the functioning , defined as performing or to perform its function , of its metabolism , defined as the processes are for life."], 
            refs_sents=[["A vitamin is a chemical compound that is needed in small amounts for the human body to work correctly."],
                        ["A vitamin is a group of organic essential micronutrient needed for the human organs to function well."],  
                        ["Vitamins are important group of organic molecules for metabolism."]])

Score= 38.16204758470948

corpus_sari(orig_sents=["An unmanned aerial vehicle (UAV) or uncrewed aerial vehicle, also known as unmanned aircraft or uncrewed aircraft (UA), commonly known as a drone, is an aircraft without a human pilot on board."],  
            sys_sents=["an vehicle, defined as a conveyance that transports people or objects, or vehicle, known as aircraft, defined as a vehicle that can fly, or aircraft, known as a drone, defined as male bee in a colony of bees whose function is to mate with the queen, is an aircraft without a pilot, defined as someone who is licensed to operate an aircraft in flight, on board, defined as a committee having powers."], 
            refs_sents=[["An unmanned aerial vehicle, also known as drone, is an aeroplane with no pilot."],
                        ["An unmanned aircraft, commonly called drone, is a type of plane with no on board pilot."],  
                        ["An uncrewed aerial vehicle, also called drone, is an aircraft without a human pilot on board."]])
Score= 39.361479743812474

Test 1: Military sentence with 1 noun = [missile]
The missile can destroy.
corpus_sari(orig_sents=["The missile can destroy."],  
            sys_sents=["the missile, defined as a rocket carrying a warhead of or explosives; may be or directed by control, can destroy."], 
            refs_sents=[["The missile is a rocket that can destroy."],
                        ["A rocket, directed by control or not, is able to destroy."],  
                        ["A missile, which is an explosive rocket, can destroy"]])
Score = 43.613729460503656

Test 2: Medical sentence with 4 nouns = [intake, vitamins, result and disease] --> only 3 nouns extended and clarified!
If intake of vitamins was lacking, the result would be deficiency and disease.
corpus_sari(orig_sents=["If intake of vitamins was lacking, the result would be deficiency and disease."],  
            sys_sents=["if intake, defined as an opening through which fluid is admitted to a tube or container, of vitamins was, the result, defined as something that results, would be deficiency and disease, defined as an impairment of health or a condition of functioning."], 
            refs_sents=[["If not enough vitamins are taken, the result would be lacking and illness."],
                        ["If vitamins are not enough, then the end would be lack of vitamins and disease."],  
                        ["If vitamins are insufficient, then that would result in not enough vitamins and disease."]])

Score = 29.896670167442362

Test 3: Military sentence with 5 nouns = [Photographers, cameras, drones, photography and maps]
The Photographer can mount a camera on the drone for an aerial photograph and to capture a map.
corpus_sari(orig_sents=["The Photographer can mount a camera on the drone for an aerial photograph and to capture a map."],  
            sys_sents=["the photographer, defined as someone who takes photographs, can mount a camera, defined as equipment for taking photographs, on the drone, defined as male bee in a colony of bees whose function is to mate with the queen, for an photograph , defined as a representation of a person or scene in the form of a print or slide; recorded by a camera on light - material, and to capture a map, defined as a representation of the earth's surface."], 
            refs_sents=[["The photographer, can place a camera on a flying vehicle to capture air photos and map."],
                        ["The person who takes photos, can put a camera on a flying aircraft to take an aerial photo and a map."],  
                        ["The photographer can place a photocamera on a flying device to take a photo and capture map in the air."]])

Score = 31.80148292981521

Test 4: Medical sentence with 7 nouns = [disease, symptoms, skin, area, pain, fever and vomit] --> Warning: a proper name is in the sentence!
Necrotizing fasciitis, also known as flesh-eating disease, has symptoms such as red or purple skin in the affected area, severe pain, fever, and vomit.
corpus_sari(orig_sents=["Necrotizing fasciitis, also known as flesh-eating disease, has symptoms such as red or purple skin in the affected area, severe pain, fever, and vomiting."],  
            sys_sents=["fasciitis , known as flesh - eating disease , defined as an impairment of health or a condition of functioning , has symptoms as or skin , defined as a body covering and site of the sense of touch , in the affected area , defined as a region of boundary , pain , defined as a symptom of some hurt or disorder , fever , defined as a rise in the temperature of the body ; a symptom of infection , and vomit , defined as the matter ejected in vomiting."], 
            refs_sents=[["Necrotizing fasciitis, also called flesh-eating sickness, has effects such as red or puple skin in area, pain, fever and cause vomit."],
                        ["Necrotizing fasciitis, also known as flesh-eating disease, can cause the conditions of red or purple skin, bad pain, rise of temperature and matter ejection."],  
                        ["Necrotizing fasciitis, also named as flesh-eating disease, can produce red or purple skin, strong pain, high temperature and ejection of matter by vomit."]])

Score = 29.6068232936654

***External Excel Document with graph to display results available with this package.

#### Observation/Conclusion
In conclusion, the simplifier produced still has substantial drawbacks but it still operates in terms of simplifying by increasing the ease of understanding of particular words and reduction of removal of some 'non-mandatory' syntactical elements such as adverbs and adjectives. The scores generated through EASSE fluctuate between 29-43. This demonstrates that there are glaring weaknesses with the simplification output compared to the reference sentences. The main core issues stem with the WordNET definitions that occassionally are not the correct meaning in the specific context. For example, 'bones' in the medical samples refer to the plural variants of white hard tissue of living organisms but the definition extracted by the program refers to "Spanish musical instrument". This should show that polysemic words can be sources of ambiguity and relying on the first definition of encountered nouns are a potential source of liability. Additionally, the removal of select words can affect the syntax and grammar. For example "An exemplar student" with the adpositions removed --> "An student" would result in a ungrammatical output. This can compromise the ease of understanding of the sentence. From the NLP progress website, the efficiency of simplifiers are evaluated dependent not only on language or algorithms applied but scores are also dependent on BLEU with SARI scores. Application of algorithms to understand semantics and context are vital to counter polysemic words but application of probability algorithms to ensure the most likely word POS tags (words with multiple POS can be a source of issues) depending on previous word tag (direct reference to Markov probabilities) are needed to be observed in the development of simplification systems against ambiguity challenges. The excel graph with the selected number of sentences demonstrates that as the number of noun increases, the EASSE score decreases with simpler and shorter sentences proving to output better scores than longer and more complex sentences with multiple elements to clarify.

## Bibliography
- “Simplification.” NLP, NLP-Progress, nlpprogress.com/english/simplification.html. 
- Manchego, Fernando Alva, and Louis Martin. “Feralvam/Easse.” GitHub, 4 Mar. 2019, github.com/feralvam/easse.
- “Necrotizing Fasciitis.” Wikipedia, Wikimedia Foundation, 19 May 2021, en.wikipedia.org/wiki/Necrotizing_fasciitis.  
- “Unmanned Aerial Vehicle.” Wikipedia, Wikimedia Foundation, 25 May 2021, en.wikipedia.org/wiki/Unmanned_aerial_vehicle.
- “Unmanned Aerial Vehicle.” Wikipedia, Wikimedia Foundation, 6 Feb. 2021, simple.wikipedia.org/wiki/Unmanned_aerial_vehicle. 
- “Vitamin.” Wikipedia, Wikimedia Foundation, 24 Feb. 2021, simple.wikipedia.org/wiki/Vitamin. 
- “Vitamin.” Wikipedia, Wikimedia Foundation, 5 May 2021, en.wikipedia.org/wiki/Vitamin.  