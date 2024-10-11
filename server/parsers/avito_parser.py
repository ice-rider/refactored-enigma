import time
import json
import random
import subprocess


request_template = r"""
curl "https://www.avito.ru/web/1/main/items?forceLocation=false&locationId=652000&lastStamp={last_stamp}&limit={limit}&offset={offset}&categoryId=4"
"""


def parse():
    try:
        offset = 0
        limit = 1000
        request = request_template.format(
            last_stamp = time.time(),
            offset = offset,
            limit = limit
        )
        process = subprocess.Popen(request, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        flats = []
        if process.returncode == 0:
            data = json.loads(stdout.decode())
            for flat in data["items"]:
                flats.append({
                    "name": flat["title"],
                    "price": flat["priceDetailed"]["value"],
                    "location": flat["location"]["name"],
                    "metrs": (lambda x: x[0] if x else None)([x for x in flat["title"].split(" ") if x and x[0].isdigit() and x[1].isdigit()]) or "...м",
                    "image": [flat["images"][index]["864x864"] for index in random.choices(list(range(flat.get("imagesCount"))), k=3) if flat.get("imagesCount")] or ["https://www.qctonline.com/wp-content/uploads/qctonline_archives/not_found.png"] * 3,
                    "url": "https://www.avito.ru" + flat["urlPath"],
                    "source": "avito"
                })
            return flats
        else:
            print(f"Error: {stderr.decode()}")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")