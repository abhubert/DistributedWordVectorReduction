# DistributedWordVectorReduction

## Table of contents
* [Intro](#intro)
* [Technologies](#technologies)
* [Structure](#structure)

## Intro
This project was submitted for my final project in LSE's ST446 Distributed Computing course. It was a self chosen topic that focussed on reducing the dimension of word vectors on a distributed system and measured their effectiveness when the dimensions were reduced. Overall I found that even with a small dataset reducing the dimensions of the word vectors still allowed for the word vectors to be useful in NLP tasks with a small loss of effectiveness according to Carnegie Mellon QVEC scores.
	
## Technologies
Project is created with:
* Google Cloud Platform
* Python 3.6
* pyspark 2.4
	
## Structure
The `src` folder contains code for cleaning the wikipedia text dump while the experiements were ultimately done on a different dataset do to credit constraints this is kept for future testing. The writeup contains the instructions for setting up the code and tests on the *GCP*. The notebook titled `projectNotebook` is the code needed to process the text data and create the word vectors as well as perform the dimensionality reduction.