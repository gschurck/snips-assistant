import datetime
import locale
import time

class DayLogger:
    def __init__(self, locale=None):
        pass
    def sayDay(self):
        jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
        now = datetime.datetime(the_year, the_month, the_day)  #year,month,day
        print now.weekday()
        print jours[now.weekday()]
        print now.day
if  __name__ == "__main__":
    heysnips = DayLogger()
    heysnips.sayDay()
