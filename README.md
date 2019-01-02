##Downloading and unzipping##
###Downoad###
Go to the archive.org twitter stream https://archive.org/details/twitterstream and download the month(s) you wish to explore.
This will take a long time depending on your internet connection, as these tend to be about 40gb files. They are organized by day, then by hour then json files are stored for each minute. 
###Unzip###
Move this month folder you have downloaded into the twitter-network-creator folder. Now unzip the files for the days your are interested in, generally to save space only unzip the range of days you plan on exploring. 

To do this, open the unzipper file and make the following edits:
* On line 3 change the '09' to whatever the name of the month folder you downloaded is. 
* On line 4 change the COUNTER=1 to COUNTER=(your start date)
* On line 5 change the '31' to one greater than your end date

Now in terminal, change directories into the twitter-network-creator folder and run 'bash unzipper'. It should start unzipping all of the files we will need. Bear in mind some of these archive months are incomplete, so you may see a number of bzip no such file errors; for the most part these can be ignored. 


##Searching and Formatting##
Once you have unzipped your files, we can search them for relevant terms/users and store them separately for network creation and visualization. To do this, you need to import the twitter_tool module in a python script, or you can just edit the twitter_tool_test.py file. 

Here are the  twitter_tool module functions and their parameters:
###search: searches the unzipped archive files for a supplied list of terms and stores those filtered tweets in a new folder###
twitter_tool.search(start_day, end_day, type_of_search, array_of_terms, write_folder_name, read_folder_name)
* start_day - first day in the range you want to search
* end_day - one greater than your end date
* type_of_search - either 'username', 'text', or 'hashtag'. Specifies which field of the tweet to search for terms. 
* array_of_terms - a python list of strings, each of them a term that you want to search the tweets for.
* write_folder_name - the name of the folder where you would like to store the search folder results.
* interactions - whether or not to include all tweets that are retweeted/mentioned/replied to/quoted. For most complete graphs do  this, but with large groups of popular users as search terms, sometimes doing this cleans up the graph and makes it more efficient.

###graph_format: takes as input the path to the filtered files created from search, and formats it for the d3 vis. ###
twitter_tool.graph_format(start_day, end_day, groups, read_folder_name, write_file_name)
* start_day - first day in the range you want to search
* end_day - one greater than your end date
* groups - a python list of lists. Each of the lists consists of a number of twitter usernames. Each of these lists of usernames will be grouped by node color in the vis. If a list consisting of another empty list is provided, then all of the nodes will be in the same group. This is for some advanced functionality with hiding groups.
* read_folder_name - name of the folder where the filtered files are stored
* write_file_name - name of the .json file where the formatted data will be stored.

###get_handles: takes the list of handles of nodes generated from the graph_format function and writes them as csv###
twitter_tool.get_handles(write_file_name) 
can only be called after graph format has been called, otherwise the nodes list will be empty. This should be used to pull handle lists for advanced graphs with groups.
* write_file_name - name of csv file where handles will be written.


an example of these functions in use is:

import twitter_tool as t

d = t.TwitterTool()


d.search(1, 3, 'hashtag', ['nevertrump', 'trump', 'latinosfortrump', 'FreeMelissa', 'trumpaz'], 'testhashtags', '09', interactions=True)
d.graph_format(1, 3, [[]], 'testhashtags', 'testhashtags2.json')
d.get_handles('testhandles.csv')



##Visualizing##
To visualize, open up newd3.html and add the name of the json file you created to the array in line 245. 

Now, go to terminal and make sure you're in the twitter-network-creator folder. run python -m SimpleHTTPServer(if on python 2) or python -m http.server (if on python 3)

Open up your browser and go to http://0.0.0.0:8000/newd3.html and you'll be able to see the graph you created!
##Advanced##
###Adding groups###
To create graphs with multiple different groups of nodes, pass a list of lists of twitter handles (as strings) into the third parameter of graph_format.
If you want to generate a list of users automatically and store them, after running the graph_format function you can call get_handles with a write file name to save every twitter handle in a network in a csv file. You can load that file and pass it in as one of the lists of lists.
###Adding remove groups###
To add removal functionality to groups in the vis, first create a csv file of twitter handles in a group formatted in the same way as what is returned from a call to get_handles. Once you have those csv files and the .json network file, you can open newd3.html and change line 299 to await d3.csv('your file here.csv')

###Generating key users, first and second level user lists###

To combine all of these functions, we can create isolated networks of users after building exploratory networks. 
1. Create a general network by searching with a set of hashtags that interest you.
2. After visualizing, you can sort the side table by betweeenness to see the most influential users in the network. Now we must isolate them and use these most important users as seeds. 
3. Run the search function again with the list of users you are interested in as your search terms and your search type as username and interactions as True. run the graph_format function. This network is your first level network, with seeds and everyone who interacted with them. If you want to go another level deeper, you can run the get_handles function and use that list of users as the search terms for the search function once again. 





note: all these directions are for mac os.