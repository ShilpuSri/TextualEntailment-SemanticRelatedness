# TextualEntailment-SemanticRelatedness
The objective of this project was to determine the textual entailment and measure the semantic relatedness of the SICK dataset (SemEval 2014)

*******************************************Textual Entailment & Semantic Similarity************************************************

The code modules evaluate pairs of sentences from the SICK dataset to determine their textual entailment and semantic relatedness. 
We used deep learning classifiers to train our models. We used the glove vectors file to convert our bag of words of the corpus to the n dimensional vector space.

For textual entailment, we used tensorflow with LSTM to train our model. 

For semantic relatedness, we used keras with LSTM to train our model. We preprocessed the sentences to convert them to lower cases and perform POS tagging. Additionally, we computed the sentence similarities using Wordnet which is 
accomplished in the file "relatedness.py". We majorly use below 2 methods to calculate the scores:
1. We look for contradictory words and determine whether the two sentences oppose each other.
2. We look for nouns, verbs, adverbs and adjectives appearing in the same location in both these sentences.
The model shows a correlation of approximately 62%, and there is scope of improvement to enhance the correlation between these 


Baseline scores: (Evaluated by compute_overlap_baseline.py from the SemEval webpage)
"Entailment: accuracy 54.8%"
"Relatedness: Pearson correlation 0.618398867939626"
"Relatedness: Spearman correlation 0.596216438995913"
"Relatedness: MSE 10.3847841950411"

Our Model's scores:
"Entailment: accuracy 72.6% (7262222222222222)"
"Relatedness: Pearson correlation 0.632175594936926"
"Relatedness: Spearman correlation 0.625280261441653"
"Relatedness: MSE 0.6310967833333334"


Steps to run the code modules:
1. Execute file "Textual Entailment.ipynb"
2. Execute file "Semantic Relatedness.ipynb"
3. Final results are obtained in the file "results.txt"


************************************************************Thank You ************************************************************
