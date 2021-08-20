import twitter_tool as t

d = t.TwitterTool()


d.search(14, 15, 'hashtag', ['twitter', 'lol'], 'loltags', '/Users/ezraedgerton/Desktop/twitter_tool/03')
d.graph_format(14, 15, [[]], 'loltags', 'loltags.json')
