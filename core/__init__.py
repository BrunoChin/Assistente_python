import datetime

class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'São {} e {} minutos'.format(now.hour,now.minute)
        return answer

    def get_date():
        now = datetime.datetime.now()
        answer = 'Hoje é dia {} de {} de {}'.format(now.day, now.strftime("%B"), now.year)
        return answer