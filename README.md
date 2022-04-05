# Social-Media-Sentiment-Analysis-During-Early-Stages-of-COVID19

## Part 1: Data Description 

This j.son file is a corpus of various articles posted on social media regarding Coronavirus. This data set was submitted and cited by Ran Geva, but the articles in these files were written by various people. Related policy that this data can be useful for is understanding how the pubic reacts to disasters and the necessary fact-checking/censorship the government needs to pay attention to. The time frame of this corpus is from December 2019 – March 2020 and contains 10,956 entries and 5.2 million posts. The average length of the text is 3341 tokens, and the average number of replies is 1.63 replies. This data set contains data from over 50+ countries and most posted articles come from India, United States, Canada, and Denmark. Even though Coronavirus’s first case was discovered in China, China was surprisingly lower on this list of number of document entries.  

## Interpretation of Dataset Findings 
According to my analysis, the most frequent words are [‘china’, ‘said’, ‘coronavirus’, ‘virus]. I suspect that these are the most frequent words because this data was taken during the early phases of Covid, and the virus has not spread to other countries yet. So, many people were searching up China and how China was handling the outbreak at that time. 

	Bigrams are words that often occur together, I found that words that occur the most together was ‘world’ and ‘health’, ‘coronavirus’ and ‘outbreak’, ‘novel’ and ‘outbreak’, and ‘public’ and ‘health’. Again, this further solidifies my reasoning that this is a new(novel) disease, so people were looking at health information and listening to what health officials had to say about the status of the coronavirus outbreak. 

	PMI measures how much more likely the words in the bigrams are going to occur together rather than be independent from each other. I found that the most common PMI’s are names. These names most likely are the authors of the documents posted on the social media sites. The names that show up first on the list starts with ‘\\u’ . Via internet searching, I learned that these are unicodes for the Hindi alphabet. This is not surprising because the most posted documents come from India. And these results are not surprising because names in articles most likely are full names rather than only putting the a part of the name. 

	For the content word part, I wanted to see the words/similar words that are often related to coronavirus when people search the term. I decided that the best way to approach this is first to find the words in concordance to ‘coronavirus’ and then search up similar words to words near ‘coronavirus’. I searched words ‘coronavirus’, ‘vaccine’, and ‘outbreak’. I will explain what is possibly happening, by analyzing the similar words that result from running the code. When coronavirus is searched, people are searching for the status of its current spread in China and possible pandemic status. When vaccine is being searched, people are interested in the symptoms of Coronavirus and possible cures. And finally, when outbreak is being searched, it shows that the current state of covid is spreading, and people are scared. One analysis that I recommend doing in the future is understanding the type of documents these are. I wonder if these are all scientific articles. If they are not, I am curious about the language difference across different type of media.



	

