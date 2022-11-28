def unique_in_order(iterable):
    order_list = []
    character = None
    for i in iterable[0:]:
        if i != character:
            order_list.append(i)
            character = i
    return order_list
