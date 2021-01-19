import praw
import config
import datetime
def log_in():
    reddit= praw.Reddit(
                client_id=config.client_id,
                client_secret=config.client_sec,
                user_agent="Tony's bot",
                username=config.username,
                password=config.password,
                )
    reddit.read_only = True
    return reddit
def get_post(reddit): 
    '''
    Alternative method
    url = "https://www.reddit.com/r/uofm/comments/je44pg/course_selection_and_scheduling_megathread_winter/"
    submission=reddit.submission(url=url)
    for i in submission.comments:
        print(i)
    '''
    url=''
    subreddit=reddit.subreddit('uofm')
    for i in subreddit.hot(limit=10):
        if 'Winter 2021' in i.title:
            url=i.url
    return url
def get_each_comment(url,reddit,course_name):
    submission=reddit.submission(url=url)
 
    submission.comments.replace_more(limit=None)
    sub_list=submission.comments.list()[:]
    count=1
    for comment in sub_list:
        if course_name in comment.body:
            c_time=datetime.datetime.utcfromtimestamp(comment.created_utc)
            print('*Post*',count,comment.author,c_time)
            print('#',comment.body)
            count+=1
            for i in comment.replies:
                r_time=datetime.datetime.utcfromtimestamp(i.created_utc)
                print(i.author,r_time,i.score,'votes')
                print('#','---',i.body)
            print('\n\n')
        
    
def main():
    r= log_in()
    url=get_post(r)
    get_each_comment(url,r,'SI 206')

if __name__ == "__main__":
    main()
