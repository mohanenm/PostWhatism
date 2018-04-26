# from https://glowingpython.blogspot.com/2014/09/text-summarization-with-nltk.html AND NLTK DOCUMENTATION!

import Twitter
import bot_bot_bot.py



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

    ### THIS IS WHERE WE PUT OUR TWEETS

    def get_only_text(url):
        """
         "return the title and the text of the article
         at the specified url"

         We can ultimately decide what we want to release here !!
        """
        page = urllib2.urlopen(url).read().decode('utf8')
        soup = BeautifulSoup(page)
        text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
        return soup.title.text, text
