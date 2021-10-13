from random import randint
import logger
import time



# Press the green button in the gutter to run the script.
import pokemon

if __name__ == '__main__':

    for i in range(0,720):
        pokemon.build_stats(i)

    """posted_list = []
    logfile = logger.gen_logfile()
    while True:
        if len(posted_list) != 781:
            national_number = randint(0, 780)

            while national_number in posted_list:
                national_number = randint(0, 720)

            authentification.gen_daily_tweet(national_number, logfile)
            authentification.set_profile_picture(national_number)
            posted_list.append(national_number)
        else:
            api = authentification.get_api()
            api.update_status("I made my job. now I have to leave,thank you everyone for checking on me !")
            break
        time.sleep(43200)"""

