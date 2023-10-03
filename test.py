class Basic:

    def __init__(self):
        self.minutes = 100
        self.sms = 0
        self.gb = 0
    def make_a_call(self):
        print('Can make a call')

class Standart(Basic):
    def __init__(self):
        self.minutes = 200
        self.sms = 100
        self.gb = 0

    def send_sms(self):
        print('Can send sms')


class Premium(Standart):
    def __init__(self):
        self.minutes = 500
        self.sms = 200
        self.gb = 10
    def serf_internet(self):
        print('Can serf internet')


tarif_1 = Basic()
tarif_2 = Standart()
tarif_3 = Premium()

print('Tarif 1')
tarif_1.make_a_call()
print(tarif_1.minutes, tarif_1.sms, tarif_1.gb)
print('Tarif 2')
tarif_2.make_a_call()
tarif_2.send_sms()
print(tarif_2.minutes, tarif_2.sms, tarif_2.gb)
print('Tarif 3')
tarif_3.make_a_call()
tarif_3.send_sms()
tarif_3.serf_internet()
print(tarif_3.minutes, tarif_3.sms, tarif_3.gb)

