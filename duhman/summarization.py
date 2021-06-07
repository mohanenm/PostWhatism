
import urllib.request
from collections import defaultdict
from heapq import nlargest
from string import punctuation

import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


class FrequencySummarizer:

    def __init__(self, min_cut=0.1, max_cut=0.9):
        """
         Words that have a frequency term lower than min_cut
         or higer than max_cut will be ignored.
         ==> set min cut, max cut to chop off outliers
        """
        self._min_cut = min_cut
        self._max_cut = max_cut
        self._stopwords = set(stopwords.words('english') + list(punctuation))

    def _compute_frequencies(self, word_sent):
        """
          frequency of each of word.
          Input: a list of sentences already tokenized.
          Output: freq, dict = freq[w] -- >  frequency of w.

        """
        freq = defaultdict(int)
        for s in word_sent:
            for word in s:
                if word not in self._stopwords:
                    freq[word] += 1
        # frequencies normalization and fitering
        m = float(max(freq.values()))
        for w in freq.keys():
            freq[w] = freq[w] / m
            if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
                del freq[w]
        return freq

    def summarize(self, text, n):
        """
         return the summary, finnaly -- > we decide n, based on how long of a summary we want to generate:
         n = number of sentences!
        """
        sents = sent_tokenize(text)
        assert n <= len(sents)
        word_sent = [word_tokenize(s.lower()) for s in sents]
        self._freq = self._compute_frequencies(word_sent)
        ranking = defaultdict(int)
        for i, sent in enumerate(word_sent):
            for w in sent:
                if w in self._freq:
                    ranking[i] += self._freq[w]
        sents_idx = self._rank(ranking, n)
        return [sents[j] for j in sents_idx]

    def _rank(self, ranking, n):
        """
        return the number of sentences we decided on with the highest ranking, most related to our text!

        """
        return nlargest(n, ranking, key=ranking.get)


def get_only_text(url):
    url_open = urllib.request.urlopen(url)
    page = url.read(url_open).decode('utf8')
    soup = BeautifulSoup(page)
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return soup.title.text, text

    ### THIS IS WHERE WE PUT OUR TWEETS


url = 'http://www.gutenberg.org/files/55443/55443-h/55443-h.htm'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
feed = BeautifulSoup(response.read().decode('utf-8'), "html5lib")
to_summarize = [(map(lambda p: p.text, feed.find_all('guid')))
                fs = FrequencySummarizer()
for article_url in to_summarize[:5]:
    title, text = get_only_text(article_url)
print('----------------------------------')
print(title)
for s in fs.summarize(text, 2):
    print('*', s)
