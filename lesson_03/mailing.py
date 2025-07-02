class Mailing:  # почтовое отправление
    def __init__(self, to_address, from_address, cost, track):
        # to_address (тип данных Address), from_address (тип данных Address),
        # cost (тип данных число), track (тип данных строка)
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Отправление {self.track} из {self.from_address} "
                f"в {self.to_address}. Стоимость {self.cost} рублей.")
