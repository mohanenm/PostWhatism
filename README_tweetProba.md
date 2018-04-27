
### Probability of test tweets belonging to freud, nietzsche


#### Procedure:
1. ##### Get tweets, using 'TwitterSearch' library; get 20 pages of tweets, with quotation marks and '#nietzsche', '#freud' 
   ##### present in the text of the tweet
2. #### Put tweets - and handle - into a pandas dataframe ==> concat both authors dataFrames - mark, annotate respectively
3. #### Generate one long string of tweets and ngrams using tfid vectorizer - generate 'summaries' + ngrams
4. #### Clean the text using NLTK & Textacy 
5. #### generate y axis for further use --> Extract features, again, using TFID vectorizer
6. #### perform a search(grid) for optimal parameters: logistic regression & grid used - sci kit
7. #### train by inserting tweets from Twitter Search into model, return confusion matrix
8. #### output most likely tweets with quotes and hashtag for each author!
     * #### Max, Min: 
     * #### Freud: We can see that Max Likelihood are tweets with vocab freud employs frequently; min are somewhat unrelated
         * #### MAX: #Freud seems to need the link between neurotic #angst and the #nonhuman 
         * #### MIN: Loving it, may b I get more in-jokes than most of, the few of my followers or following
      * #### Max, Min: 
      * #### Nietzsche: Sames goes for the likelihood of nietzsche tweets
         * #### MAX: 
         * #### MIN: 
  

```python

n_test = [ "To live is to suffer, to survive is to find some meaning in the suffering."]


     Proba_nietzsche  Proba_freud  
0           0.959248     0.040752  
0           0.959248     0.040752  
1           0.944313     0.055687  
1           0.944313     0.055687  
2           0.945296     0.054704  
2           0.945296     0.054704  
3           0.962375     0.037625  
3           0.962375     0.037625  
4           0.961653     0.038347  
4           0.961653     0.038347  
5           0.945259     0.054741  
5           0.945259     0.054741  
6           0.947093     0.052907  
7           0.961653     0.038347  
8           0.954907     0.045093  
9           0.952281     0.047719  
10          0.946402     0.053598  
11          0.947093     0.052907  
12          0.944180     0.055820  
13          0.962375     0.037625  
14          0.961653     0.038347  
15          0.944197     0.055803  
16          0.962375     0.037625  
17          0.955729     0.044271  
18          0.952740     0.047260  
19          0.962375     0.037625  
20          0.945288     0.054712  
21          0.952281     0.047719  
22          0.942989     0.057011  
23          0.954907     0.045093  
..               ...          ...  
130         0.958361     0.041639  
131         0.958403     0.041597  
132         0.944410     0.055590  
133         0.947596     0.052404  
134         0.947596     0.052404  
135         0.946034     0.053966  
136         0.945210     0.054790  
137         0.945245     0.054755  
138         0.944749     0.055251  
139         0.946804     0.053196  
140         0.944197     0.055803  
141         0.944586     0.055414  
142         0.944313     0.055687  
143         0.953463     0.046537  
144         0.944375     0.055625  
145         0.944197     0.055803  
146         0.944778     0.055222  
147         0.947682     0.052318  
148         0.947682     0.052318  
149         0.942025     0.057975  
150         0.945346     0.054654  
151         0.946804     0.053196  
152         0.942306     0.057694  
153         0.945746     0.054254  
154         0.953362     0.046638  
155         0.955729     0.044271  
156         0.951439     0.048561  
157         0.944197     0.055803  
158         0.947056     0.052944  
159         0.958403     0.041597  
```