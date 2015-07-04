__author__ = 'Paul'
# cosine_similarity_to_compare_text_files.py


import glob
from sklearn.feature_extraction.text import TfidfVectorizer


#Prepare the documents for scikit
documents = []
for f in glob.glob('C:\\Users\\Paul\\PycharmProjects\\\\data_files\\*.txt'):
    with open(f) as myfile:
        documents.append(myfile.read().replace('\n', ''))

tfidf_vectorizer = TfidfVectorizer(strip_accents='unicode', stop_words='english', ngram_range=(1,1))
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
pairwise_similarity = tfidf_matrix * tfidf_matrix.T
print(pairwise_similarity.toarray())