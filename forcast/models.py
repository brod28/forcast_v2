#forcast model
class Forcast(object):
    temperature = ""
    date = ""
    text = ""

    #parser from third party object to forcast model
    def parse(self,condition):
        self.desctiption = condition.text()
        self.date = condition.date()
        self.temperature = condition.temp()+' F'
        return self


