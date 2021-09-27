from models.item import Item

URL = 'https://www.linio.com.co/p/imac-con-pantalla-retina-4k-215-intel-core-i3-1tb-mrt32e-a-apple-jr3hnd?qid=5ed7ee35c9d4a4afb3fe1cf00c2f97f1&oid=AP039EL1L1ECHLCO&position=1&sku=AP039EL1L1ECHLCO'
TAG_NAME = 'span'
QUERY = {'class': 'price-main-md'}


imac = Item(URL, TAG_NAME, QUERY)
imac.save_to_database()

items_loaded = Item.all()
print(items_loaded[0].get_price())
