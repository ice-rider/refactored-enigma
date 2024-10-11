import time
import json
import random

import requests
import cianparser


def parse():
    moscow_parser = cianparser.CianParser(location="Ростов-на-Дону")
    data = moscow_parser.get_flats(deal_type="sale", rooms="all", additional_settings={"start_page":1, "end_page":5})
    flats = []
    for index, flat in enumerate(data):
        per = int(index/len(data)*10)
        print(f"\r{index/len(data)*100:2f}% [{ int(per-1) * '=' }>{ int(10-per) * ' ' }]")
        flats.append({
            "name": flat["author"] + " " + flat["residential_complex"],
            "price": flat["price"],
            "location": flat["location"],
            "metrs": flat["total_meters"],
            "image": take_photo(flat["url"]),
            "url": flat["url"],
            "source": "cian"
        })
    return flats


def take_photo(url, flag=False):
    time.sleep(0.1)
    req = requests.get(url)
    if not req.ok:
        if flag:
            ["https://www.qctonline.com/wp-content/uploads/qctonline_archives/not_found.png"] * 3
        else:
            time.sleep(1)
            return take_photo(url, flag=True)
    html = req.text
    start = 0
    imgs = []
    b_imgs = []

    for i in range(html.count('<img ')):
        url, end = cut_img(html, start)
        if url.startswith('https://images.cdn-cian.ru/') and url.split(".")[-1] in ['jpg', 'jpeg', 'png']:
            imgs.append(url)
        else:
            b_imgs.append(url)
        start = end
    if imgs:
        return imgs[0], random.choice(imgs), random.choice(imgs)
    elif b_imgs:
        return b_imgs[0], random.choice(b_imgs), random.choice(b_imgs)
    else:
        return ["https://www.qctonline.com/wp-content/uploads/qctonline_archives/not_found.png"] * 3


def cut_img(html, start):
    first_img_index = html.find("<img", start)
    cut_data = html[first_img_index:]
    first_src_index = cut_data.find("src")
    cut_data = cut_data[first_src_index:]

    h_start = cut_data.find("\"") + 1
    h_end = cut_data.find("\"", h_start+1)
    return cut_data[h_start:h_end], h_end+first_img_index
