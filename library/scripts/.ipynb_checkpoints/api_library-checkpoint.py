from xmlrpc import client

url = 'https://krisleon99-odootest-bugs-2417243.dev.odoo.com'
db = 'krisleon99-odootest-bugs-2417243'
username = 'admin'
password = 'admin'


common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())


uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))
model_access_right = models.execute_kw(db, uid, password,
    'library.book', 'check_access_rights',
    ['read'], {'raise_exception': False})

print(model_access_right)

books = models.execute_kw(db, uid, password,
    'library.book', 'search',
    [[['total', '>', '0']]])

print(books)


book = models.execute_kw(db, uid, password,
    'library.book', 'search',
    [[['name', '=', 'Julieta']]])

print(book)


id = models.execute_kw(db, uid, password, 'library.book', 'create', [{
    'name': "New book",
}])