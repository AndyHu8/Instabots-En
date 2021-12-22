from instapy import InstaPy
from instapy import smart_run
import schedule
import time

#Anmeldedaten
my_username = 'testbot_chn'
my_password = 'WoJiaoChina1803%%'

def job():
    #Mach eine neue Session
    session = InstaPy(username = my_username,
                      password = my_password,
                      headless_browser = False)

    with smart_run(session):
        #Braucht man nicht unbedingt
        session.set_relationship_bounds(enabled = True,
                                        delimit_by_numbers = True,
                                        max_followers = 500,
                                        min_followers = 30,
                                        min_following = 50)

        session.set_do_follow(True, percentage = 100) #Follow alle Seiten (100%)
        #session.set_dont_like(['nsfw', 'kia', 'ford']) #Nicht diese followern

        session.like_by_tags(['china', 'programmer', 'developer', 'bot'], amount = 10) #Diese followern
        target_users = session.target_list('nicknames.txt')
        session.follow_by_list(target_users, times = 1, sleep_delay = 600) #Insta nicknames

        #session.follow_by_locations(['214512512/dusseldorf-germany/'], amount = 5)

schedule.every().day.at("13:50").do(job)
schedule.every().day.at("18:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(10)