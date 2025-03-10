"""
input:
8
1 0 menu_1
2 0 menu_2
3 1 menu_3
4 1 menu_4
5 2 menu_5
6 3 menu_6
7 0 menu_7
8 2 menu_8
"""

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
