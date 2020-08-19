
from bs4 import BeautifulSoup
import lxml
import requests

'''
#web_addr = 'https://www.aliexpress.com/item/33043374087.html?spm=a2g0o.productlist.0.0.3a8515edISTQYw&algo_pvid=249b661d-a5f2-4df9-857d-94777cfac56a&algo_expid=249b661d-a5f2-4df9-857d-94777cfac56a-17&btsid=0ab50f0815828556698318140ee757&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_'
web_addr = 'https://www.aliexpress.com/item/33029913386.html?spm=a2g0o.productlist.0.0.3c12147dGCFTEg&algo_pvid=ab265f78-3d75-4f1c-84a0-e4a245306875&algo_expid=ab265f78-3d75-4f1c-84a0-e4a245306875-2&btsid=0ab50f4915844994677292177e5add&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_'
#web_addr = 'https://www.aliexpress.com/item/32984246341.html?spm=a2g0o.productlist.0.0.65c759c1cMxivv&algo_pvid=5a193fe8-61c4-4439-ba9c-cb99f3f184e3&algo_expid=5a193fe8-61c4-4439-ba9c-cb99f3f184e3-16&btsid=0ab6d69515844993957806142efbb9&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_'

#web_addr = input("Enter address: ")
'''

class Aex:
    def __init__(self, url):
        self.url = url
        self.web_resource = requests.get(url)
        self.soup = BeautifulSoup(self.web_resource.text, 'lxml')

    def get_title(self): # Title text
        title = self.soup.title.text
        title_space_loc = title.find("|")
        return title[:title_space_loc]

    def get_script(self):
        script_txt = self.soup.find_all('script')
        ext_scr_txt = script_txt[15].text  # wanted text located in 16th script
        return ext_scr_txt

    def scan_str(self, full_str, st_str, end_str):
        loc0 = full_str.find(st_str)
        loc1 = full_str.find(end_str, loc0)
        len_st_str = len(st_str)
        extr_str = full_str[loc0 + len_st_str + 3 : loc1]
        return extr_str

    def get_seller(self):
        return self.scan_str(self.get_script(), 'storeName', '","storeNum')

    def get_price(self):
        return self.scan_str(self.get_script(), 'totalValue', '"\n')





if __name__ == "__main__":
    store = Aex('https://www.aliexpress.com/item/32984246341.html?spm=a2g0o.productlist.0.0.65c759c1cMxivv&algo_pvid=5a193fe8-61c4-4439-ba9c-cb99f3f184e3&algo_expid=5a193fe8-61c4-4439-ba9c-cb99f3f184e3-16&btsid=0ab6d69515844993957806142efbb9&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_')
    print(store.get_title())
    print(store.get_seller())
    print(store.get_price())

