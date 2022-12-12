def pagination(products, page=1):
    per_page = 10
    start = (page - 1) * per_page
    end = per_page * page
    return products[start:end]
