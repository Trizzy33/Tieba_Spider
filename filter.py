# filter function.
# the function must accept 5 args(id, title, author, reply_num, good)
# and return True(if you would like to store this thread..) or False (or not)


# ex:

def thread_filter(id, title, author, reply_num, good):
    return "吧" in title or "规" in title
    
    
# > scrapy run hadoop hadoop -f thread_filter
# only threads which have more than 30 replies will be stored.