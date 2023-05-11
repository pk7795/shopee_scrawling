import pymongo, requests, json
from unidecode import unidecode

client = pymongo.MongoClient()
mydb = client['Shopee_Data']
columm1 = mydb['APIs']
columm2 = mydb['Items']

def getItems(a,b):

    # https://shopee.vn/api/v4/item/get?itemid=14703541008&shopid=357627062
    for index, api in enumerate(columm1.find(), start=0):
        if index >=a and index<b:
            response = requests.get(api['link'])
            rawData = json.loads(response.text)
            for index2, raw in enumerate(rawData['items'], start=1):
                # if index2 ==2:
                description = getDescription(raw['itemid'], raw['shopid'])
                name_lowercase= raw['item_basic']['name'].lower()
                item = {
                    'name': raw['item_basic']['name']   ,
                    'itemid': raw['itemid'],
                    'category_id': api['category_id'],
                    'category_id_p': api['category_id_p'],
                    'description': description,
                    'name_lowercase': name_lowercase,
                    'name_removemark': unidecode(name_lowercase)
                }
                try:
                    columm2.insert_one(item)
                    print("ghi thanh cong ban ghi thu: "+str(index2))
                except:
                    print("loi o ban ghi"+str(index2))
            print('xong api thu: '+str(index+1))



def getDescription(itemid, shopid):
    resItems = requests.get('https://shopee.vn/api/v4/item/get?itemid=' +
                            str(itemid)+'&shopid=' + str(shopid))
    itemData = json.loads(resItems.text)
    return itemData['data']['description']


# getItems(382,2000)
# getItems(1000,2000)
