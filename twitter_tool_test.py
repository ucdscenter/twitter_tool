import twitter_tool as t

d = t.TwitterTool()


d.search(1, 3, 'hashtag', ['nevertrump', 'trump', 'latinosfortrump', 'FreeMelissa', 'trumpaz'], 'testhashtags', '09')
d.graph_format(1, 3, [[]], 'testhashtags', 'testhashtags2.json')
print(d.get_handles('testhandles.csv'))