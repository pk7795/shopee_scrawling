# from getCategories import getList
import pymongo


def getAPIs():
    client = pymongo.MongoClient()
    mydb = client['Shopee_Data']
    Categories = mydb['categories']
    Locations = mydb['locations']
    columm3 = mydb['APIs']

    by = [
        'price',
        'ctime',
        'pop',
        'sales'
    ]
    sort = [
        'desc',
        'asc'
    ]

    locations = []
    # lấy list địa chỉ
    for locat in Locations.find():
        locations.append(locat['code'])

    # https://shopee.vn/api/v4/search/search_items?by=(BY)&locations=(LOCATED)&categoryids=(CATEGORYID)
    # &limit=60&match_id=(MATCHID)&newest=(VALUESNUMBER)&order=(SORT)&page_type=search&scenario=PAGE_OTHERS&version=2
    for categoryList in Categories.find():  # lấy parent_catid
        for category in categoryList['children']:  # lấy catid từng chỉ mục con
            for locate in locations:
                for b in by:
                    api_list = []
                    if b != "price":
                        for i in range(60, 100):
                            api_list.append({
                                # 'matchid': categoryList['matchid'],
                                'category_id_p': categoryList['parent_catid'],
                                'category_id': category['catid'],
                                # 'display_name': categoryList['parent_display_name'],
                                # 'name': categoryList['parent_name'],
                                'link': 'https://shopee.vn/api/v4/search/search_items?by=' + b + '&locations=' + locate + '&categoryids=' +
                                        str(category['catid']) + '&limit=60&match_id=' + str(
                                    categoryList['parent_catid']) + '&newest=' + str(i) +
                                        '&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2'
                            })
                    else:
                        for i in range(60, 100):
                            api_list.append({
                                # 'matchid': categoryList['matchid'],
                                # 'display_name': categoryList['parent_display_name'],
                                # 'name': categoryList['parent_name'],
                                'category_id_p': categoryList['parent_catid'],
                                'category_id': category['catid'],
                                'link': 'https://shopee.vn/api/v4/search/search_items?by=' + 'price' + '&locations=' + locate + '&categoryids=' +
                                        str(category['catid']) + '&limit=60&match_id=' + str(
                                    categoryList['parent_catid']) + '&newest=' + str(i) +
                                        '&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2'
                            })
                            api_list.append({
                                # 'matchid': categoryList['matchid'],
                                # 'display_name': categoryList['parent_display_name'],
                                # 'name': categoryList['parent_name'],
                                'category_id_p': categoryList['parent_catid'],
                                'category_id': category['catid'],
                                'link': 'https://shopee.vn/api/v4/search/search_items?by=' + 'price' + '&locations=' + locate + '&categoryids=' +
                                        str(category['catid']) + '&limit=60&match_id=' + str(
                                    categoryList['parent_catid']) + '&newest=' + str(i) +
                                        '&order=asc&page_type=search&scenario=PAGE_OTHERS&version=2'
                            })
                    # them api vao mongodb 
                    for index, api in enumerate(api_list, start=1):
                        try:
                            columm3.insert_one(api)
                            print("ghi thanh cong ban ghi thu: " + str(index))
                        except:
                            print("ban ghi thu " + str(index) + " bi loi")
