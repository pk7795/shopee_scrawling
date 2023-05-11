import pymongo, requests, json
from rawCategory import sellerData

def getSellerCategory():

    for seller in sellerData:
        children = []
        for child in seller['children']:
            if child['has_children'] == False:
                children.append({
                    'display_name': child['display_name'],
                    'name': child['name'],
                    'catid': child['id']
                })
            else:
                for child1 in child['children']:
                    if child1['has_children'] == False:
                        children.append({
                            'display_name': child1['display_name'],
                            'name': child1['name'],
                            'catid': child1['id']
                        })
                    else:
                        for child2 in child1['children']:
                            children.append({
                                'display_name': child2['display_name'],
                                'name': child2['name'],
                                'catid': child2['id']
                            })

        yield{
            'name': seller['name'],
            'catid': seller['id'],
            'children': children
        }

def getList():
    response = requests.get(
        'https://shopee.vn/api/v4/pages/get_homepage_category_list')

    rawData = json.loads(response.text)

    for raw in rawData['data']['category_list']:
        for Seller in getSellerCategory():
            if raw['name'] == Seller['name']:
                print(Seller['catid'])
                yield{
                    'parent_display_name': raw['display_name'],
                    'parent_name': raw['name'],
                    'matchid': raw['catid'],
                    'parent_catid': Seller['catid'],
                    'children': Seller['children']
                }


def inserttoMongo():
    client= pymongo.MongoClient()
    mydb= client['Shopee_Data']
    columm = mydb['categories']
    for index, list in enumerate(getList(), start=1):
        try:
            columm.insert_one(list)
            print("ghi thanh cong ban ghi thu: "+str(index))
        except:
            print('ban ghi thu '+str(index)+" bi loi ")
inserttoMongo()
