import praw, requests, os,sys
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
def get_post(reddit,name,count): 
    '''
    Alternative method
    url = "https://www.reddit.com/r/uofm/comments/je44pg/course_selection_and_scheduling_megathread_winter/"
    submission=reddit.submission(url=url)
    for i in submission.comments:
        print(i)
    '''
    url_lst=[]
    subreddit=reddit.subreddit(name)
    page=subreddit.hot(limit=count)
    
    for i in page:
        print(str(i.url))
        url=str(i.url)
        if 'png' in url or 'jpeg' in url or 'jpg' in url:
            url_lst.append(url)
    for c,i in enumerate(url_lst):
        response = requests.get(i)
        with open('img'+str(c)+'.png', 'wb') as f:
                f.write(response.content)
def main(argv):
    r= log_in()
    get_post(r,argv[0],int(argv[1]))
    #print(argv[0],argv[1])

if __name__ == "__main__":
    main(sys.argv[1:])
