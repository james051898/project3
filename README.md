James Morgan
Project 3: CEO Activism 
CSC 2053
This project is for CSC 2053. I used Python to scrape twitter from CEOs within the S&P 100 to compare their number of followers and total statuses to the compounding annual growth rate of their respective stocks. In addition, I created a Python program to upload GOOGLEFINANCE code to sheets in order to partially automate the process. I published my findings on my web portfolio found at http://webster.csc.villanova.edu/~plapro13/lab4/ under the CEO activisim tab. This project was made possible by using the google API and twitter developer API.

	The first portion of this project included gaining access to a twitter development account and installing Python. After a short correspondence, I was able to get developer access. Thereafter, I searched online about which Python IDE I should use. I decided it would be best to use Eclipse’s Pydev because I have a lot of experience with Eclipse already. In addition to this, I made sure that I could download various packages using PIP and my computer’s terminal.
	
	Twitter Scraper:
	My first hurdle was learning how to use Oauth1 verification to get access to the Tweepy API. After installing Tweepy with PIP, I spent a good amount of time learning to connect to twitter with Oauth1 verification. From there, I created my Python application using various websites to learn to create pandas dataframes and export my findings to a CSV. I also identified the screen names and CEOs that had twitter accounts in the S&P 100. 
	
	Finance APIs:
	The next portion of my project was to find an appropriate method to aggregate some sort of performance data using Python. There were many websites that offered this service at a cost and I searched for a free version for quite some time. I spend some time trying to use Beautiful Soup to download data directly from Yahoo finance and other websites. In addition, I went to the finance lab to find some raw data but ultimately decided it would be best to use the GOOGLEFINANCE function in sheets to calculate CAGR. 
	
	GOOGLEFINANCE:
	I created a google developer account and installed the appropriate packages to get access to my google spreadsheet. My google developer account gave me access to the sheets API using an Oauth2 authentication. The google sheets API was much easier to use as you could just keep your keys in your local directory and use pygsheets’ authorize() command. I used a sequence of for loops to input the GOOGLEFINANCE code directly. Pygsheets has a set_dataframe method, however, I had a lot of trouble importing it horizontally.
	
	Web Portfolio:
	The final portion of my project was to publish my findings on my web portfolio. After aggregating my data in excel, I was able to save the file as an htm document and upload it directly to my web portfolio. 
	
