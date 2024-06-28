from requests import get
from datetime import datetime,timezone


API_KEY = "add api of etherescan"
address = "0x80af7f3db7c1d0eb1d9934773dee37c2f5d77dc3"
BASE_URL = "https://api.etherscan.io/api"
start_block = 100000  
end_block = 6699999 


def make_api_url(module, action, address , **kwargs):
    url = BASE_URL + f"?module={module}&action={action}&address={address}&apikey={API_KEY}"

    for key, value in kwargs.items():
        url+= f"&{key}={value}"

        return url
def filter_transactions_by_block(transactions, start_block, end_block):
    return [tx for tx in transactions if int(tx['blockNumber']) >= start_block and int(tx['blockNumber']) <= end_block]
    

def get_normal_transactions(address, start_block, end_block):
    get_normal_transactions_url = make_api_url("account", "txlist", address, startblock=start_block, endblock = end_block, page=1, offset = 10000, sort="asc")
    response = get(get_normal_transactions_url)
    normaltransactions = response.json()["result"]
    get_internal_transactions_url = make_api_url("account", "txlistinternal", address, startblock=start_block, endblock = end_block, page=1, offset = 10000, sort="asc")
    response2 = get(get_internal_transactions_url)
    internaltransactions = response2.json()["result"]
    get_erc20_transactions_url = make_api_url("account", "tokentx", address, startblock=start_block, endblock = end_block, page=1, offset = 10000, sort="asc")
    response3 = get(get_erc20_transactions_url)
    erc20transactions = response3.json()["result"]   
    normaltransactions = filter_transactions_by_block(normaltransactions, start_block, end_block)
    internaltransactions = filter_transactions_by_block(internaltransactions, start_block, end_block)
    erc20transactions = filter_transactions_by_block(erc20transactions, start_block, end_block)
     
     # from and to address and  timestamp for normal transactions

    for tx in normaltransactions:
        to = tx["to"]
        from_addr = tx["from"]
        time = datetime.fromtimestamp(int(tx['timeStamp']))
        print ("To:", to)
        print ("From:", from_addr)
        print ("Time:", time)

     # from and to address and  timestamp for internal transactions
    for tx in internaltransactions:
        to = tx["to"]
        from_addr = tx["from"]
        time = datetime.fromtimestamp(int(tx['timeStamp']))
        print ("To:", to)
        print ("From:", from_addr)
        print ("Time:", time)

    # from and to address and  timestamp for erc20 transactions
    for tx in erc20transactions:
        to = tx["to"]
        from_addr = tx["from"]
        time = datetime.fromtimestamp(int(tx['timeStamp']))
        print ("To:", to)
        print ("From:", from_addr)
        print ("Time:", time)
   




get_normal_transactions(address, start_block, end_block)

