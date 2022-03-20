import json

with open('api_test.json', encoding='utf8') as f:
    templates = json.load(f)

def CheckInt (item):
    return isinstance(item, int)

def CheckStr(item):
    return isinstance(item, str)

def CheckBool (item):
    return isinstance(item, bool)

def CheckUrl (item) :
    if isinstance(item, str):
        return item.startswith('http://') or item.startswith('https://')
    else:
        return False

def CheckStrValue(item, val):
    if isinstance(item, str):
        return item in val
    else:
        return False

def ErrorLog(item, value, string):
    Error.append({item: f'{value}, {string}'})

listofitems = {'timestamp': 'int', 'item_price': 'int', 'referer': 'url', 'location': 'url', 'item_url': 'url',
            'remoteHost': 'str', 'partyId': 'str', 'sessionId': 'str', 'pageViewId': 'str', 'item_id': 'str',
            'basket_price': 'str', 'userAgentName': 'str', 'eventType': 'val', 'detectedDuplicate': 'bool',
            'detectedCorruption': 'bool', 'firstInSession': 'bool'}

Error = []
for items in templates:
    for item in items:
        if item in listofitems:
            if listofitems[item] == 'int':
                if not CheckInt(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listofItems[item]}')
            elif listofitems[item] == 'str':
                if not CheckStr(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listofItems[item]}')
            elif listofitems[item] == 'bool':
                if not CheckBool(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listofItems[item]}')
            elif listofitems[item] == 'url':
                if not CheckUrl(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {listofItems[item]}')
            elif listofitems[item] == 'val':
                if not CheckStrValue(items[item], ['itemBuyEvent', 'itemViewEvent']):
                    ErrorLog(item, items[item], 'ожидали значение itemBuyEvent или itemViewEvent')
            else:
                ErrorLog(item, items[item], 'неожиданное значение')
        else:
            ErrorLog(item, items[item], 'неожиданная переменная')

if Error == []:
    print('Pass')

else:
    print('Fail')
    print(Error)

