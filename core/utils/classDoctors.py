
class Doctor:
    def __init__(self, name, family, room, count_tickets, week):
        self.name = name
        self.family = family
        self.room = room
        self.count_tickets = count_tickets
        self.week = week
        self.first_day_tickets = 'отсутствует'

    def __call__(self):
        return self.family

    def get_first_dae_tickets(self):
        if self.count_tickets > 0:
            for i in self.week:
                if self.week[i] > 0:
                    self.first_day_tickets = i
                    break
        return self.first_day_tickets
