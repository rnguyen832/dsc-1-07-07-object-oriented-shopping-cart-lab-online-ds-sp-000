class ShoppingCart():
    # write your code here
    def __init__(self, _employee_discount=None, _total=0, _items=[]):
        self._total = 0
        self._items = []
        self._employee_discount = _employee_discount
    
    def get_total(self):
        return self._total
    def set_total(self, amount):
        self._total += amount
        
    def get_items(self):
        return self._items
    def set_items(self, item):
        self._items.append(item)
        
    def get_employee_discount(self):
        return self._employee_discount
    def set_employee_discount(self, discount):
        self._employee_discount = discount
        
    total = property(get_total,set_total)
    items = property(get_items,set_items)
    employee_discount = property(get_employee_discount, set_employee_discount)
    
    def add_item(self, item, price, quantity=1):
        self._items.append({'item':item,'price':price,'quantity':quantity})
        self._total += price*quantity
        print(self._total)
        
    def mean_item_price(self):
        total_price = 0
        total_quantity = 0
        for i in range(len(self._items)):
            total_price += self._items[i]['price']*self._items[i]['quantity']
            total_quantity += self._items[i]['quantity']
        print(total_price/total_quantity)
        
    def median_item_price(self):
        price_list = []
        for i in range(len(self._items)):
            for q in range(self._items[i]['quantity']):
                price_list.append(self._items[i]['price'])
        price_list = sorted(price_list)
        while len(price_list) > 2:
            price_list.pop(0)
            price_list.pop(-1)
        if len(price_list) == 2:
            median = (price_list[0]+price_list[1])/2
            print(median)
        else:
            print(price_list)   

    def apply_discount(self):
        if self._employee_discount != None:
            print(self._total*(100-self._employee_discount)/100)
        else:
            print('Sorry, there is no discount to apply to your cart :(')
            
    def item_names(self):
        item_list = []
        for i in range(len(self._items)):
            for q in range(self._items[i]['quantity']):
                item_list.append(self._items[i]['item'])
        print(item_list)
        
    def void_last_item(self):
        self._total -= self._items[-1]['price']
        self._items.pop(-1)
