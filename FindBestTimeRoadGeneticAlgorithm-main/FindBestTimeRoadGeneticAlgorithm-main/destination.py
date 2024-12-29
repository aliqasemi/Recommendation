class Destination:

    def __init__(self, name, cost, category, duration, tags=[], placeid=0):
        self.name = name.replace(',', '')
        self.cost = int(cost)
        self.category = category
        self.duration = float(duration)
        self.tags = tags
        self.placeid = placeid
        # self.npeople = int(npeople)
