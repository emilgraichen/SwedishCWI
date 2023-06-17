# SwedishCWIdataset

This dataset is a part of the Bachelor's thesis in Cognitive Science at Linköping University. The thesis, named "Context-aware Swedish Lexical Simplification", describes the development of three lexical simplification algorithms where the first step was to train a Random Forest Classifier to identify complex words. This dataset contains words and their annotated complexity level, word lengths, and the frequencies of each word in three corpora. The purpose of the dataset is to facilitate training Complex Word Identification (CWI) systems. The dataset is based on the SwedishCWI dataset developed by Smolenska (2018), who annotated the word complexity levels in the dataset as a part of the Master's thesis "Complex Word Identification for Swedish". Also included in this repository is a Python script to train and save a Random Forest Classifier that assigns complexity levels (ranging from 1-4) to individual words, heavily influenced by the work of Smolenska (2018). 

To read a more detailed description of the project, please follow this link: https://liu.diva-portal.org/smash/get/diva2:1767273/FULLTEXT01.pdf


Other repositories related to this thesis are:

Lexical Simplification System: https://github.com/emilgraichen/SwedishLexicalSimplifier

Lexical Simplification Evaluation Dataset: https://github.com/emilgraichen/SwedishLSdataset



## Structure of the dataset:


![A picture showing the structure of the dataset](images/dataset_structure.png?raw=true "Title")

The first column contains the word, the second column contains the word difficulty annotated by Smolenska (2018), the third, fifth and sixth column the common logarithm of the frequency in the scrambled Stockholm Umeå Corpus, the BloggMix Odat corpus and TwitterMix corpus respectively. The difficulty level ranges between 1-4 where 4 is the most complex level. 



## Links to the resources used:

Stockholm Umeå Corpus X 3.0: https://spraakbanken.gu.se/resurser/sucx3

BloggMix Odat: https://spraakbanken.gu.se/resurser/bloggmix

TwitterMix: https://spraakbanken.gu.se/resurser/twitter


The link to the thesis by Smolenska (2018) is found here: https://www.semanticscholar.org/paper/Complex-Word-Identification-for-Swedish-Smolenska/8728f63b7a08b1c9668bef101ba36a7950aa2432

The link to the original CWI dataset is found here: https://github.com/gsmolenska/CWIdataset/blob/master/SwedishCWI.txt


## References: 
Smolenska, G. (2018). Complex word identification for Swedish. Recieved from: https://www.semanticscholar.org/paper/Complex-Word-Identification-for-Swedish-Smolenska/8728f63b7a08b1c9668bef101ba36a7950aa2432 (2023-05-25)
