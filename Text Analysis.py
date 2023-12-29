from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(wiki_lst) # Create tf-idf feature of the wikipedia dataset
