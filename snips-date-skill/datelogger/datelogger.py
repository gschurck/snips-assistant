#coding=utf-8
import datetime
import time
import calendar
import locale
from datetime import date

class DateLogger:
    def __init__(self, locale=None):
        pass
    def sayDate(self):
        today = date.today()
        jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
        mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre","Novembre","Décembre"]
        my_date = str(int(today.day))
        #print "Nous sommes le {} {} {}".format(jours[time.localtime()[6]], my_date, mois[time.localtime()[1]-1])
        return "Nous sommes le {} {} {}".format(jours[time.localtime()[6]], my_date, mois[time.localtime()[1]-1])
    def sayDay(self):
        jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
        now = datetime.datetime(the_year, the_month, the_day)  #year,month,day
        print now.weekday()
        print jours[now.weekday()]
        print now.day

if  __name__ == "__main__":
    heysnips = DateLogger()
    heysnips.sayDate()
    heysnips.sa
