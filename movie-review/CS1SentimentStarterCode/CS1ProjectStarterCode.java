import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

/*
 * This is code I wrote with students in class to demonstrate how to read from the movie review file.
 * It searches each review for the queried word and just prints out the score of that review along
 * with its text to ensure that we can read the two values and use the .contains() method properly.
 */
public class CS1ProjectStarterCode
{
	public static void main(String[] args) throws FileNotFoundException
	{
		File reviewFile = new File("movieReviews.txt");
		Scanner reviewScanner = new Scanner(reviewFile);
		Scanner keyboard = new Scanner(System.in);

		int reviewScore;
		double wordCount = 0;
		String reviewText;
		String word;
		double reviewAverage;
		double totalScore = 0;
		String fileName;
		ArrayList<String> reviewList = new ArrayList<String>();
		int revScore;
		double wordTracker = 0;
		String revText;
		String wordIn;
		double reviewAve;
		double totScore = 0;
		double combinedScore = 0;
		double uniqueWordCount = 0;
		double combinedAve;
		String sentiment;
		String highestWord = "highest";
		double highestScore = 0;
		String lowestWord = "lowest";
		double lowestScore = 10;

		System.out.println("Enter a word.");
		word = keyboard.nextLine();

		while(reviewScanner.hasNext())
		    {
			    reviewScore = reviewScanner.nextInt();
			    reviewText = reviewScanner.nextLine();
			    reviewList.add(reviewScore + "-" + reviewText);

			    if(reviewText.contains(word))
			    {
			        totalScore = totalScore + reviewScore;
			        wordCount += 1;
				    // System.out.println("Score: "+reviewScore);
				    // System.out.println("Text: "+reviewText);
			    }
		    }
        reviewAverage = totalScore / wordCount;
        System.out.println(word+" Appears "+wordCount+" times.");
        System.out.println("The average score for reviews containing the word "
        + word + " is " + reviewAverage);

        Scanner fileIn = new Scanner(System.in);
        System.out.println(
        "Enter the name of the file with words you want to score: ");
        fileName = fileIn.nextLine();
		File wordFile = new File(fileName);
		Scanner wordScanner = new Scanner(wordFile);

        while(wordScanner.hasNext())
        {
            wordIn = wordScanner.nextLine();
            for (String line : reviewList)
            {
                String[] scoreText = line.split("-");
			    revScore = Integer.parseInt(scoreText[0]);
			    revText = scoreText[1];

			    if(revText.contains(wordIn))
			    {
			        totScore = totScore + revScore;
			        wordTracker += 1;
			    }
		    }
            reviewAve = totScore / wordTracker;
            if (reviewAve > 2.01) {
                 highestScore = reviewAve;
                 highestWord = wordIn;
            }
            if (reviewAve < 1.99) {
                 lowestScore = reviewAve;
                 lowestWord = wordIn;
            }
            combinedScore = combinedScore + reviewAve;
            uniqueWordCount += 1;
        }
        combinedAve = combinedScore / uniqueWordCount;
        if (combinedAve > 2.01) {
                 sentiment = "positive";
             } else {
                 if (combinedAve < 1.99) {
                     sentiment = "negative";
                 } else {
                     sentiment = "neutral";
                 }
             }

        System.out.println("The average score of words in " + fileName
        + " is " + combinedAve + ".");
        System.out.println("The overall sentiment of " + fileName
        + " is " + sentiment + ".");
	}
}
