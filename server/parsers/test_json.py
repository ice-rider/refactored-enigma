import json


def test_has_item_required_fields(item):
    assert item.get('name') is not None
    assert item.get('price') is not None
    assert item.get('location') is not None
    assert item.get('metrs') is not None
    assert item.get('image') is not None
    assert item.get('url') is not None
    assert item.get('source') is not None


def test_images_count(item):
    assert len(item.get('image')) == 3


def main():
    with open('out_all.json', 'r') as f:
        data = json.load(f)
        for item in data:
            try:
                test_has_item_required_fields(item)
                test_images_count(item)
            except AssertionError as e:
                print(item)
                raise e


if __name__ == '__main__':  
    main()