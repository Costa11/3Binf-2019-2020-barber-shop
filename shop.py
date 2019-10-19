class Shop:
    def __init__(self,address,open_hour,close_hour,min_price,max_price,avg_price,f):
        self.address = address
        self.open_hour = open_hour
        self.close_hour = close_hour
        self.min_price = min_price
        self.max_price = max_price
        self.avg_price = (max_price + min_price) / 2
    def is_open(self, now):
        if now > self.open_hour and now < self.close_hour :
            return True
        else:
            return False