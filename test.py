class Basic:
    def make_a_call(self):
        print('Can make a call')

class Standart(Basic):
    def send_sms(self):
        print('Can send sms')


class Premium(Standart):
    def serf_internet(self):
        print('Can serf internet')


tarif_1 = Basic()
tarif_2 = Standart()
tarif_3 = Premium()

print('Tarif 1')
tarif_1.make_a_call()
print('Tarif 2')
tarif_2.make_a_call()
tarif_2.send_sms()
print('Tarif 3')
tarif_3.make_a_call()
tarif_3.send_sms()
tarif_3.serf_internet()

