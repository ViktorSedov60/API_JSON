# import turtle
#
# turtlePen = turtle.Turtle()
# window = turtle.Screen()
#
# window.bgcolor("black")
#
#
# def polygon(n, size=80):
#     if n > 4:
#         angle = 360 / n
#
#         for n in range(0, n):
#             turtlePen.color(colors[n % 5])
#             turtlePen.left(angle)
#             turtlePen.forward(size)
#
#
# turtlePen.speed(0)
#
# colors = ['orange', 'cyan', 'blue', 'green', 'red']
#
# size = 5
#
# for i in range(0, 40):
#     turtlePen.color(colors[i % 5])
#     polygon(6, size)
#     turtlePen.left(5)
#     size += 3
#
# window.mainloop()

# class Product:
#     def __init__(self, name, category, quantity_in_stock):
#         self.name = name
#         self.category = category
#         self.quantity_in_stock = quantity_in_stock
#
#     def is_available(self):
#         return True if self.quantity_in_stock > 0 else False
#
# eggs = Product("eggs", "food", 5)
# brad = Product("brad", "food", 5)
# eg = Product("eg", "food", 5)
# fack = Product("fack", "food", 0)
# print(fack.is_available())



#  два метода обработки объекта с классом
# class Event:
#     def __init__(self, timestamp, event_type, session_id):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id

# class Event:
#     def __init__(self, timestamp=0, event_type="", session_id=""):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
#
#     def init_from_dict(self, event_dict):
#         self.timestamp = event_dict.get("timestamp")
#         self.type = event_dict.get("type")
#         self.session_id = event_dict.get("session_id")
# events = [
#     {
#      "timestamp": 1554583508000,
#      "type": "itemViewEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1555296337000,
#      "type": "itemViewEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1549461608000,
#      "type": "itemBuyEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
# ]
#
# # for event in events:
# #     event_obj = Event(timestamp=event.get("timestamp"),
# #                       event_type=event.get("type"),
# #                       session_id=event.get("session_id"))
# #     print(event_obj.timestamp)
#
# for event in events:
#     event_obj = Event()
#     event_obj.init_from_dict(event)
#     print(event_obj.timestamp)
#



class Event:
    def __init__(self, timestamp=0, event_type="", session_id=""):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")

    def show_description(self):
        print("This is generic event.")


class ItemViewEvent(Event):
    type = "itemViewEvent"

    def __init__(self, timestamp=0, session_id="", number_of_views=0):
        self.timestamp = timestamp
        self.session_id = session_id
        self.number_of_views = number_of_views

    def show_description(self):
        print("This event means someone has browsed an item.")


if __name__ == "__main__":
    test_view_event = ItemViewEvent(timestamp=1549461608000, session_id="0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct", number_of_views=6)
    test_view_event.show_description()
    print(test_view_event.type)