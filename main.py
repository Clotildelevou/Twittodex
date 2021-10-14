from random import randint
import logger
import state

import authentification

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    state_file = state.get_state_file()
    logfile = logger.gen_logfile()
    posted_list = state.get_state(state_file)
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
