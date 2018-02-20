import arrow
"""
intheure = a.hour
intminute = a.minute
heure = str(int(intheure))
minute = str(int(intminute))
"""
class TimeLogger:
    def __init__(self,locale=None):
        pass
    def sayTime(self):
        a = arrow.utcnow().replace(hours=1)
        intheure = a.hour
        intminute = a.minute
        heure = str(int(intheure))
        minute = str(int(intminute))
        if heure == 0:
            if minute == 0:
                print "Il est minuit"
                return "Il est minuit"
            elif minute > 0:
                print  "Il est minuit " + minute
                return "Il est minuit " + minute
        elif minute > 0:
            print "Il est " + heure + " heures" + " " + minute
            return "Il est " + heure + " heures" + " " + minute
        elif minute == 0:
            print heure
            return heure
        else:
            print "Je ne sais pas lire l'heure"
            return "Je ne sais pas lire l'heure"

if  __name__ == "__main__":
    heysnips = TimeLogger()
    #heysnips.sayTime()
