import re

def search_recent(keyword='game'):
    # get all search result and match regex
    query_result = ['game', 'game of throne', 'sacred game', 'nodejs']
    match_result = []
    for element in query_result:
        if keyword in element:
            match_result.append(element)
    return match_result
