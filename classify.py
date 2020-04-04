#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:21:40 2020

@author: mac
"""

# Introduction to machine learning
# See the accompanying tutorial at <>
# Gareth Dwyer, January 2019
# dwyer.co.za

# We only need to import two bits of magic from scikit-learn
# The first import is `tree`, which will give us the classifier
# that will learn to classify text from existing data. 
# The second import is a vectorizer, which we'll use to transform texts 
# into a basic numerical representation as computers find it easier 
# to deal with numbers than language
from sklearn import tree
from sklearn.feature_extraction.text import CountVectorizer

# Our existing set of positive texts to learn from
# We already "know" that these are positive, so we 
# can use them as examples to train the machine.
positive_texts = [
    "we love you",
    "they love us",
    "you are good",
    "he is good",
    "they love mary"
]
# Same as above, but negative texts.
negative_texts = [
    "we hate you",
    "they hate us",
    "you are bad",
    "he is bad",
    "we hate mary"
]

# These are the test texts. We pretend that we 
# don't know if these are negative or positive. 
# We'll use them to test our model and see how good
# it is after the training.
test_texts = [
    "they love mary",
    "they are good",
    "why do you hate mary",
    "they are almost always good",
    "we are very bad"
]

# We combine our known positive and negative texts 
# into a combined training set to feed into the classifier 
training_texts = negative_texts + positive_texts

# We also prepare an equivalent set of labels, to tell the machine
# that the first five texts are negative and the second ones are positive. 
# When we feed these into the classifier, it'll use indices to match up 
# the texts, e.g. the first label in the list is "negative", so it'll learn
# to associate the "negative" class with the first text.
training_labels = ["negative"] * len(negative_texts) + ["positive"] * len(positive_texts)

# Here we set up the vectorizer, the first main component of our machine learning solution. 
vectorizer = CountVectorizer()

# This isn't really learning anything difficult yet. We just 
# feed the data we have into our vectorizer so it can keep a 
# consistent mapping. E.g. it might map "bad" to 0, "love" to 1, 
# you to 2, etc.
vectorizer.fit(training_texts)
print(vectorizer.vocabulary_)

# Now we transform all of our training texts into vector form. 
# At this point, each text is represented by a list of numbers,
# showing how often that word occurs in the text.
training_vectors = vectorizer.transform(training_texts)

# We'll do the same to our test texts. Each of these is a list
# of numbers too after this step.
testing_vectors = vectorizer.transform(test_texts)

# Here we create our classifier and train it  by "showing" it the training texts and 
# the associated labels. It will iterate over the data a few times, 
# trying different rules, until it finds a set of rules that works. 
classifier = tree.DecisionTreeClassifier()
classifier.fit(training_vectors, training_labels)

# It's easy to "overfit" -- find a set of rules that works very well
# for the set of data that we show the classifier, but which doesn't 
# work very well on other data, even if it's similar. Here we ask 
# the computer to guess whether our test texts (which it has never 
# seen) are more similar to the positive texts or the negative ones so we can check how well it works.
print(classifier.predict(testing_vectors))

# Then we export the model to a file so that we can visualise it. You can
# copy the content from `tree.dot` to http://www.webgraphviz.com/ to 
# see what the tree looks like
tree.export_graphviz(
    classifier,
    out_file='tree.dot',
    feature_names=vectorizer.get_feature_names(),
)


# We could hand code the rules ourselves. This function 
# does exactly the same thing, but we had to explicitly 
# tell the computer which words were good and which were bad
# instead of leaving it to figure things out for itself.
def manual_classify(text):
    if "hate" in text:
        return "negative"
    if "bad" in text:
        return "negative"
    return "positive"


predictions = []
for text in test_texts:
    prediction = manual_classify(text)
    predictions.append(prediction)
print(predictions)
