import re
from persist_module import *

def search_recent(keyword='game'):
    print('-'*100)
    # get all search result and match regex
    query_result = get_all_row()
    match_result = []
    if len(query_result)>0:
        for element in query_result:
            print('ement', element[0])
            if keyword in element[0]:
                match_result.append(element[0])
    print('match result', match_result)
    return match_result


