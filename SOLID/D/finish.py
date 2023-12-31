import requests

class Connection:
    def get_json(self, url):
        raise NotImplementedError


class Request(Connection):
    def __init__(self, request: requests):
        self.request = request

    def get_json(self, url:str):
        response = self.request.get(url)
        return response.json()

class NewRequest(Connection):

    def get_json(self, url):
        pass


class ApiClient:
    def __init__(self, fetch: Connection):
        self.fetch = fetch
    def get_json(self, url):
        return self.fetch.get_json(url)



def pretty_view(data: list[dict]):
    pattern = '|{:^10}|{:^10}|{:^10}|'
    print(pattern.format('currency', 'sale', 'buy'))
    for el in data:
        currency, *_ = el.keys()
        buy = el.get(currency).get('buy')
        sale = el.get(currency).get('sale')
        print(pattern.format(currency, sale, buy))

def adapter_result_for_pretty_view(data):
    return [{f"{el.get('ccy')}": {'buy': float(el.get('buy')), "sale": float(el.get('sale'))}} for el in data]


if __name__ == '__main__':
    client = ApiClient(Request(requests))
    data = client.get_json(
        "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11"
    )
    pretty_view(adapter_result_for_pretty_view(data))
