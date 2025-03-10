def print_menu(menu, parent, tab=0):
    for data in menu:
        if data['parent'] == parent:
            print("..." * tab + data['label'])
            print_menu(menu, data['id'], tab + 1)

jumlah_menu = int(input("Jumlah menu: "))

menu = []
print("Masukkan id menu, parent menu dan label menu\ncontoh: 1 0 menu_1")
for i in range(jumlah_menu):
    data = input().strip().split()
    menu.append({
        'id': int(data[0]),
        'parent': int(data[1]),
        'label': data[2]
    })

print_menu(menu, 0)
