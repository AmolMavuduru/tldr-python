from tldr_python import __version__
from tldr_python import *


def test_version():

    assert __version__ == '1.0.0'


def test_summary():

	summary = Summary({'summary': 'This is a sample summary.'})
	assert summary.text == 'This is a sample summary.'

def test_keyword():

	keyword = KeyWord(word="keyword", score=10)
	assert keyword.word == "keyword" and keyword.score == 10

def test_keywords_list():

	keywords_list = KeyWordsList([{'keyword': 'start', 'score': 15}, 
								 {'keyword': 'end', 'score': 5}])

	words_match = keywords_list.keywords[0].word == 'start' and keywords_list.keywords[1].word == 'end'
	scores_match = keywords_list.keywords[0].score == 15 and keywords_list.keywords[1].score == 5

	assert words_match and scores_match


def test_sentiment():

	sentiment_object = Sentiment({'sentiment': 'positive', 'polarity': 0.5})
	assert sentiment_object.sentiment == 'positive' and sentiment_object.polarity == 0.5






