# The Challenge
Sentiment Analysis is a Big Data problem which seeks to determine the general attitude of a writer given some text they have written. For instance, we would like to have a program that could look at the text “The film was a breath of fresh air” and realize that it was a positive statement while “It made me want to poke out my eye balls” is negative. 

One algorithm that we can use for this is to assign a numeric value to any given word based on how positive or negative that word is and then score the statement based on the values of the words. But, how do we come up with our word scores in the first place?

That’s the problem that we’ll solve in this assignment. You are going to search through a file containing movie reviews from the Rotten Tomatoes website which have both a numeric score as well as text. You’ll use this to learn which words are positive and which are negative.

Note that each review starts with a number 0 through 4 with the following meaning:
0 : negative
1 : somewhat negative
2 : neutral
3 : somewhat positive
4 : positive

1. (30 points) For the base assignment, you will ask the user to enter a word, and then you will search every movie review for that word. If you find it, add the score for that review to the word’s running score total (i.e., an accumulator variable). You also will need to keep track of how many appearances the word made so that you can report the average score of reviews containing that word back to the user.

2. (10 points) For an additional 10 points, ask the user to give you the name of a file containing a series of words, one-per-line, and compute the score of every word in the file. Report back to the user the average score of the words in the file. This will allow you to predict the overall sentiment of the phrase represented by words in the file. Consider an average word score above 2.01 as an overall positive sentiment and consider average score below 1.99 to have an overall negative sentiment.

3. (10 points) For an additional 10 points, ask the user to give you the name of a file containing a series of words, one-per-line, and compute the score of every word in the file. Report back to the user which word was the most positive and which was the most negative.