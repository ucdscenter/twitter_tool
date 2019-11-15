import twitter_tool as t

d = t.TwitterTool()


d.search(2, 3, 'hashtag', ['tbt'], 'testhashtags', '/Users/ezraedgerton/Desktop/projects/newtwitter/05')
d.graph_format(2, 3, [[]], 'testhashtags', 'testhashtags2.json')
