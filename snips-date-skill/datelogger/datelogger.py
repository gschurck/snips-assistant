#coding=utf-8
import datetime
import time
import calendar
import locale
from datetime import date

mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre","Novembre","Décembre"]
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

class DateLogger:
    def __init__(self, locale=None):
        pass
    def sayDate(self):
        today = date.today()
        my_date = str(int(today.day))
        #print "Nous sommes le {} {} {}".format(jours[time.localtime()[6]], my_date, mois[time.localtime()[1]-1])
        return "Nous sommes le {} {} {}".format(jours[time.localtime()[6]], my_date, mois[time.localtime()[1]-1])
    def sayDay(self, year, month, dayNumber):
        the_year = int(str(year))
        the_month = mois.index(month) + 1
        the_day = int(str(dayNumber))
        now = datetime.datetime(the_year, the_month, the_day)  #year,month,day
        return "Le {} {} {} est un {}".format(dayNumber, month, year, jours[now.weekday()])

if  __name__ == "__main__":
    print("hi")
    heysnips = DateLogger()
    """
    heysnips.sayDate()®
    heysnips.sayDay()
    """
