# MarriageInTexas
I created a project using Linux, Python, makefile, and matplotlib to identify and visualize possible correlations between race and the age of women at marriage in Texas. I analyzed 40 years and approximately 9 million records of marriage data.
My hypothesis was that Hispanic women in Texas get married younger. I used two data sources. The first one is a list of frequently occurring surnames in the 2010 census and what percentage of each race has that surname (Names_2010Census.csv). The other data source is a list of marriages in Texas which has the names and ages of the brides (AllMarriages.gz). 
To figure out if my hypothesis was correct, I first went through each last name in the 2010 Census and assigned to it the race it is most prevalent in. I called this program lastNames.py. The different races I looked at were White, Black, Asian/Native Hawaiin/Pacific Islander, Indian/Alaska Native, Multi (two or more races), and Hispanic. To simplify things I called the Asian/Native Hawaiin/Pacific Islander group just Asian and the Indian/Alaska Native group just Indian. I put the last names and their races into a file called lastNames.txt. 
Next I took out the names and ages of the brides in AllMarriages.gz. I called this program femaleNames.py. I put the names and ages into a file called femaleNames.txt. 
After this I compared the files lastNames.txt and femaleNames.txt. I called this program compare.py. I made lastNames.txt into a dictionary. I then looped through femaleNames.txt and checked if the last name of the bride was in the dictionary. If it was, I added the corresponding race and age to their lists. I put the races and ages into a file called compare.txt. 
Lastly I found the averages of each race by looping through compare.txt and adding up the ages and totals of each race and dividing the sum of the ages by the sum of the totals. I called this program average.py. I put the averages of each race into a file called average.txt.
I then made a bar graph showing the average age that women of each race get married at in Texas. I also make a makefile.
I found that my hypothesis was incorrect. The average age of Hispanic women is 27, which is actually in the middle of the other averages. Black women had the highest average at 30. Both White women and Asian women had an average of 28 and both Indian and Multi women had an average of 24. 
