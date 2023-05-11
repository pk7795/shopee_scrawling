import pymongo, requests, json

class Locations:
    # lay ma tinh thanh tren url
    def splitUrl(self):
        urlList = [
            # a->g
            'https://shopee.vn/Qu%E1%BA%A7n-cat.11035639.11035648?locations=An%2520Giang%2CBi%25CC%2580nh%2520Thu%25C3%25A2%25CC%25A3n%2CB%25C3%25ACnh%2520%25C4%2590%25E1%25BB%258Bnh%2CB%25E1%25BA%25AFc%2520Ninh%2CB%25C3%25A0%2520R%25E1%25BB%258Ba%2520-%2520V%25C5%25A9ng%2520T%25C3%25A0u%2CB%25E1%25BA%25A1c%2520Li%25C3%25AAu%2CB%25E1%25BA%25BFn%2520Tre%2CB%25C3%25ACnh%2520D%25C6%25B0%25C6%25A1ng%2CB%25E1%25BA%25AFc%2520Giang%2CB%25C3%25ACnh%2520Ph%25C6%25B0%25E1%25BB%259Bc%2CB%25E1%25BA%25AFc%2520K%25E1%25BA%25A1n%2CCao%2520B%25E1%25BA%25B1ng%2CC%25C3%25A0%2520Mau%2CC%25E1%25BA%25A7n%2520Th%25C6%25A1%2CGia%2520Lai&page=0&sortBy=ctime',
            # h->k
            'https://shopee.vn/Qu%E1%BA%A7n-cat.11035639.11035648?locations=Huy%25E1%25BB%2587n%2520B%25C3%25ACnh%2520Ch%25C3%25A1nh%2CHuy%25E1%25BB%2587n%2520Thanh%2520Tr%25C3%25AC%2CH%25C3%25A0%2520Nam%2CH%25C6%25B0ng%2520Y%25C3%25AAn%2CHuy%25E1%25BB%2587n%2520Gia%2520L%25C3%25A2m%2CHuy%25E1%25BB%2587n%2520Th%25C6%25B0%25E1%25BB%259Dng%2520T%25C3%25ADn%2CH%25C3%25A0%2520N%25E1%25BB%2599i%2CH%25E1%25BA%25A3i%2520D%25C6%25B0%25C6%25A1ng%2CHuy%25E1%25BB%2587n%2520Ho%25C3%25A0i%2520%25C4%2590%25E1%25BB%25A9c%2CHuy%25E1%25BB%2587n%2520%25C4%2590%25C3%25B4ng%2520Anh%2CH%25C3%25A0%2520T%25C4%25A9nh%2CH%25E1%25BA%25A3i%2520Ph%25C3%25B2ng%2CHuy%25E1%25BB%2587n%2520Thanh%2520Oai%2CH%25C3%25A0%2520Giang%2CH%25C3%25B2a%2520B%25C3%25ACnh%2CH%25E1%25BA%25ADu%2520Giang%2CKh%25C3%25A1nh%2520H%25C3%25B2a%2CKi%25C3%25AAn%2520Giang%2CKon%2520Tum&page=0&sortBy=ctime',
            # l,n,p
            'https://shopee.vn/Qu%E1%BA%A7n-cat.11035639.11035648?locations=Lai%2520Ch%25C3%25A2u%2CLong%2520An%2CL%25C3%25A0o%2520Cai%2CL%25C3%25A2m%2520%25C4%2590%25E1%25BB%2593ng%2CL%25E1%25BA%25A1ng%2520S%25C6%25A1n%2CNam%2520%25C4%2590%25E1%25BB%258Bnh%2CNgh%25E1%25BB%2587%2520An%2CNinh%2520B%25C3%25ACnh%2CNinh%2520Thu%25E1%25BA%25ADn%2CN%25C6%25B0%25E1%25BB%259Bc%2520Ngo%25C3%25A0i%2CPh%25C3%25BA%2520Th%25E1%25BB%258D%2CPh%25C3%25BA%2520Y%25C3%25AAn&page=0&sortBy=ctime',
            # q->Quan cau giay
            'https://shopee.vn/Qu%E1%BA%A7n-cat.11035639.11035648?locations=Qu%25E1%25BA%25A3ng%2520B%25C3%25ACnh%2CQu%25E1%25BA%25A3ng%2520Nam%2CQu%25E1%25BA%25A3ng%2520Ng%25C3%25A3i%2CQu%25E1%25BA%25A3ng%2520Ninh%2CQu%25E1%25BA%25A3ng%2520Tr%25E1%25BB%258B%2CQu%25E1%25BA%25ADn%25201%2CQu%25E1%25BA%25ADn%252010%2CQu%25E1%25BA%25ADn%252011%2CQu%25E1%25BA%25ADn%252012%2CQu%25E1%25BA%25ADn%25202%2CQu%25E1%25BA%25ADn%25203%2CQu%25E1%25BA%25ADn%25206%2CQu%25E1%25BA%25ADn%25207%2CQu%25E1%25BA%25ADn%25208%2CQu%25E1%25BA%25ADn%25209%2CQu%25E1%25BA%25ADn%2520Ba%2520%25C4%2590%25C3%25ACnh%2CQu%25E1%25BA%25ADn%2520B%25C3%25ACnh%2520Th%25E1%25BA%25A1nh%2CQu%25E1%25BA%25ADn%2520B%25C3%25ACnh%2520T%25C3%25A2n%2CQu%25E1%25BA%25ADn%2520B%25E1%25BA%25AFc%2520T%25E1%25BB%25AB%2520Li%25C3%25AAm%2CQu%25E1%25BA%25ADn%2520C%25E1%25BA%25A7u%2520Gi%25E1%25BA%25A5y&page=0&sortBy=ctime',
            # govap->son la
            'https://shopee.vn/Qu%E1%BA%A7n-cat.11035639.11035648?locations=Qu%25E1%25BA%25ADn%2520G%25C3%25B2%2520V%25E1%25BA%25A5p%2CQu%25E1%25BA%25ADn%2520Hai%2520B%25C3%25A0%2520Tr%25C6%25B0ng%2CQu%25E1%25BA%25ADn%2520Ho%25C3%25A0n%2520Ki%25E1%25BA%25BFm%2CQu%25E1%25BA%25ADn%2520Ho%25C3%25A0ng%2520Mai%2CQu%25E1%25BA%25ADn%2520H%25C3%25A0%2520%25C4%2590%25C3%25B4ng%2CQu%25E1%25BA%25ADn%2520Long%2520Bi%25C3%25AAn%2CQu%25E1%25BA%25ADn%2520Nam%2520T%25E1%25BB%25AB%2520Li%25C3%25AAm%2CQu%25E1%25BA%25ADn%2520Ph%25C3%25BA%2520Nhu%25E1%25BA%25ADn%2CQu%25E1%25BA%25ADn%2520Thanh%2520Xu%25C3%25A2n%2CQu%25E1%25BA%25ADn%2520T%25C3%25A2n%2520B%25C3%25ACnh%2CQu%25E1%25BA%25ADn%2520T%25C3%25A2n%2520Ph%25C3%25BA%2CQu%25E1%25BA%25ADn%2520T%25C3%25A2y%2520H%25E1%25BB%2593%2CQu%25E1%25BA%25ADn%2520%25C4%2590%25E1%25BB%2591ng%2520%25C4%2590a%2CS%25C3%25B3c%2520Tr%25C4%2583ng%2CS%25C6%25A1n%2520La&page=0&sortBy=ctime',
            # t->dong thap. het
            'https://shopee.vn/Qu%E1%BA%A7n-cat.11035639.11035648?locations=Thanh%2520H%25C3%25B3a%2CTh%25C3%25A1i%2520B%25C3%25ACnh%2CTh%25C3%25A1i%2520Nguy%25C3%25AAn%2CTh%25E1%25BB%25A7%2520%25C4%2590%25E1%25BB%25A9c%2CTh%25E1%25BB%25ABa%2520Thi%25C3%25AAn%2520Hu%25E1%25BA%25BF%2CTi%25E1%25BB%2581n%2520Giang%2CTp.%2520H%25E1%25BB%2593%2520Ch%25C3%25AD%2520Minh%2CTr%25C3%25A0%2520Vinh%2CTuy%25C3%25AAn%2520Quang%2CT%25C3%25A2y%2520Ninh%2CV%25C4%25A9nh%2520Long%2CV%25C4%25A9nh%2520Ph%25C3%25BAc%2CY%25C3%25AAn%2520B%25C3%25A1i%2C%25C4%2590i%25E1%25BB%2587n%2520Bi%25C3%25AAn%2C%25C4%2590%25C3%25A0%2520N%25E1%25BA%25B5ng%2C%25C4%2590%25E1%25BA%25AFk%2520L%25E1%25BA%25AFk%2C%25C4%2590%25E1%25BA%25AFk%2520N%25C3%25B4ng%2C%25C4%2590%25E1%25BB%2593ng%2520Nai%2C%25C4%2590%25E1%25BB%2593ng%2520Th%25C3%25A1p&page=0&sortBy=ctime'
        ]
        self.locateList = []
        for url in urlList:
            url1 = url.split('=')
            url2 = url1[1][:-5].split("%2C")
            for u in url2:
                self.locateList.append(u)

    def getItemslist(self):
        response = requests.get(
            'https://shopee.vn/api/v4/search/location_filter')
        self.locationData = []
        nameLocation = []
        rawLocationdata = json.loads(response.text)
        for raw in rawLocationdata['data']:
            for r in raw['locations']:
                nameLocation.append(r)

        for index_n, n in enumerate(nameLocation, start=1):
            for index_l, l in enumerate(self.locateList, start=1):
                if index_n == index_l:
                    self.locationData.append({
                        "name": n,
                        "code": l
                    })

    def inserttoMongo(self):
        client = pymongo.MongoClient()
        mydb = client['Shopee_Data']
        columm = mydb['locations']
        for index, list in enumerate(self.locationData, start=1):
            try:
                columm.insert_one(list)
                print("ghi thanh cong ban ghi thu: "+str(index))
            except:
                print("ban ghi thu "+str(index)+" bi loi")
l= Locations()
l.splitUrl()
l.getItemslist()
l.inserttoMongo()