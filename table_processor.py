import pandas as pd

def process_items(data):

    items = data.get("items", [])

    table = []

    for item in items:

        name = item.get("item","Unknown")
        qty = item.get("qty",0)
        price = item.get("price",0)

        total = qty * price

        table.append({
            "item":name,
            "qty":qty,
            "price":price,
            "line_total":total
        })

    df = pd.DataFrame(table)

    return df