def co_example(name):
    print 'Entering coroutine %s' % (name)
    my_text = []
    while True:
        txt = (yield)
        my_text.append(txt)
        print my_text


def search_file(filename):
    print 'Searching file %s' % (filename)
    my_file = open(filename, 'r')
    file_content = my_file.read()
    my_file.close()
    while True:
        search_text = (yield)
        search_result = 0
        search_result = file_content.count(search_text)
        print 'Number of matches: %d' % (search_result)
            
        