
def extract_command_ctx(ctx):
    command_content = ctx.message.content
    print('Command to run :', command_content)
    split_command = command_content.split(' ')
    if len(split_command) > 1:
        search_keyword = split_command[1:]
        search_str = ' '.join(search_keyword)
        print('searching google for keyword', search_str)
        return search_str
    else:
        return None
