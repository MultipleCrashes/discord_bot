
def extract_command_ctx(ctx):
    command_content = ctx.message.content
    print('Command to run :', command_content)
    split_command = command_content.split(' ')
    if len(split_command) > 2:
        return None
    search_keyword = split_command[-1]
    return search_keyword