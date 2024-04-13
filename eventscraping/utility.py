from constant import web3_category_keywords

def is_contain_keyword(title):
    for keyword in web3_category_keywords:
        if keyword.lower() in title.lower():
            return True
    return False