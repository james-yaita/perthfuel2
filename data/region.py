import urllib.parse

region_list = [
    {"region_id": 25, "region_name": "Metro : North of River"},
    {"region_id": 26, "region_name": "Metro : South of River"},
    {"region_id": 27, "region_name": "Metro : East &amp; Hills"},
    {"region_id": 15, "region_name": "Albany"},
    {"region_id": 28, "region_name": "Augusta / Margaret River"},
    {"region_id": 30, "region_name": "Bridgetown / Greenbushes"},
    {"region_id": 1, "region_name": "Boulder"},
    {"region_id": 2, "region_name": "Broome"},
    {"region_id": 16, "region_name": "Bunbury"},
    {"region_id": 3, "region_name": "Busselton (Townsite)"},
    {"region_id": 29, "region_name": "Busselton (Shire)"},
    {"region_id": 19, "region_name": "Capel"},
    {"region_id": 4, "region_name": "Carnarvon"},
    {"region_id": 33, "region_name": "Cataby"},
    {"region_id": 5, "region_name": "Collie"},
    {"region_id": 34, "region_name": "Coolgardie"},
    {"region_id": 35, "region_name": "Cunderdin"},
    {"region_id": 31, "region_name": "Donnybrook / Balingup"},
    {"region_id": 36, "region_name": "Dalwallinu"},
    {"region_id": 6, "region_name": "Dampier"},
    {"region_id": 20, "region_name": "Dardanup"},
    {"region_id": 37, "region_name": "Denmark"},
    {"region_id": 38, "region_name": "Derby"},
    {"region_id": 39, "region_name": "Dongara"},
    {"region_id": 7, "region_name": "Esperance"},
    {"region_id": 40, "region_name": "Exmouth"},
    {"region_id": 41, "region_name": "Fitzroy Crossing"},
    {"region_id": 17, "region_name": "Geraldton"},
    {"region_id": 21, "region_name": "Greenough"},
    {"region_id": 22, "region_name": "Harvey"},
    {"region_id": 42, "region_name": "Jurien"},
    {"region_id": 8, "region_name": "Kalgoorlie"},
    {"region_id": 43, "region_name": "Kambalda"},
    {"region_id": 9, "region_name": "Karratha"},
    {"region_id": 44, "region_name": "Kellerberrin"},
    {"region_id": 45, "region_name": "Kojonup"},
    {"region_id": 10, "region_name": "Kununurra"},
    {"region_id": 18, "region_name": "Mandurah"},
    {"region_id": 32, "region_name": "Manjimup"},
    {"region_id": 58, "region_name": "Meckering"},
    {"region_id": 46, "region_name": "Meekatharra"},
    {"region_id": 47, "region_name": "Moora"},
    {"region_id": 48, "region_name": "Mt Barker"},
    {"region_id": 61, "region_name": "Munglinup"},
    {"region_id": 23, "region_name": "Murray"},
    {"region_id": 11, "region_name": "Narrogin"},
    {"region_id": 49, "region_name": "Newman"},
    {"region_id": 50, "region_name": "Norseman"},
    {"region_id": 60, "region_name": "North Bannister"},
    {"region_id": 12, "region_name": "Northam"},
    {"region_id": 62, "region_name": "Northam (Shire)"},
    {"region_id": 13, "region_name": "Port Hedland"},
    {"region_id": 51, "region_name": "Ravensthorpe"},
    {"region_id": 57, "region_name": "Regans Ford"},
    {"region_id": 14, "region_name": "South Hedland"},
    {"region_id": 53, "region_name": "Tammin"},
    {"region_id": 24, "region_name": "Waroona"},
    {"region_id": 54, "region_name": "Williams"},
    {"region_id": 55, "region_name": "Wubin"},
    {"region_id": 59, "region_name": "Wundowie"},
    {"region_id": 56, "region_name": "York"}
]


item_id = "region_id"
item_name = "region_name"
item_default_id = 25


def find_id(searchText):
    i = 0
    length = len(region_list)
    region_ID = None
    if searchText is None or type(searchText) != str:
        return region_ID

    while (not region_ID and i < length):
        parsed_text = urllib.parse.unquote_plus(searchText)
        parsed_text = parsed_text.replace('&', '&amp;')

        if(region_list[i]['region_name'] == parsed_text):
            region_ID = region_list[i]['region_id']
        i += 1

    return region_ID


def find_desc(searchText):
    region_desc = None

    try:
        if searchText is None or type(searchText) != str:
            raise ValueError
        region_id = int(searchText)
    except ValueError:
        return region_desc

    i = 0
    length = len(region_list)

    while (not region_desc and i < length):

        if(region_list[i]['region_id'] == region_id):
            region_desc = region_list[i]['region_name']
        i += 1

    return region_desc
