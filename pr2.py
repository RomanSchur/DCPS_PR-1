import copy
standard_tariff_day = 26.4
standard_tariff_night = 21.6
nakrytka_day = 100
nakrytka_night = 80

Information_storage = [
    {"ID": 1, "Дата": "01.03.2025", "Денне_споживання(кВт)": 40.5, "Нічне_споживання(кВт)": 10.5,"Загальна сума оплати на теперішню дату":1296},
    {"ID": 2, "Дата": "01.03.2025", "Денне_споживання(кВт)": 50.1, "Нічне_споживання(кВт)": 20,"Загальна сума оплати на теперішню дату":2000},
    {"ID": 3, "Дата": "01.03.2025", "Денне_споживання(кВт)": 40, "Нічне_споживання(кВт)": 20.5,"Загальна сума оплати на теперішню дату":3000},
]

def Calculate_price(new_data):
    old_data = next((i for i in Information_storage if i["ID"] == new_data["ID"]), None)
    old_index = next((index for index, i in enumerate(Information_storage) if i["ID"] == new_data["ID"]), None)
    new_data_copy = copy.deepcopy(new_data)

    if old_data is None:
        res_price=new_data_copy['Денне_споживання(кВт)']*standard_tariff_day+new_data_copy['Нічне_споживання(кВт)']*standard_tariff_night
        print(f"-------------------------------- Результат обрахунку для лічильника № {new_data_copy['ID']} --------------------------------")
        print(f"Станом на {new_data_copy['Дата']} лічильник №{new_data_copy['ID']} нарахував: {new_data_copy['Денне_споживання(кВт)']} кВт вночі.")
        print(f"Станом на {new_data_copy['Дата']} лічильник №{new_data_copy['ID']} нарахував: {new_data_copy['Нічне_споживання(кВт)']} кВт вночі.")
        print(f"--------------------------------------------------------------------------------------------------------------------")
        print(f"Плата за {new_data_copy['Дата']} для лічильника №{new_data_copy['ID']} становить: {res_price:.2f} грн")
        new_data_copy['Загальна сума оплати на теперішню дату'] = res_price
        Information_storage.append(new_data_copy)
        return

    if new_data_copy["Денне_споживання(кВт)"] < old_data["Денне_споживання(кВт)"]:
        new_data_copy["Денне_споживання(кВт)"] += nakrytka_day
        differens_day = new_data_copy["Денне_споживання(кВт)"] - old_data["Денне_споживання(кВт)"]
        price_day = differens_day * standard_tariff_day
    else:
        price_day = (new_data_copy["Денне_споживання(кВт)"] - old_data["Денне_споживання(кВт)"]) * standard_tariff_day

    if new_data_copy["Нічне_споживання(кВт)"] < old_data["Нічне_споживання(кВт)"]:
        new_data_copy["Нічне_споживання(кВт)"] += nakrytka_night
        differens_night=new_data_copy["Нічне_споживання(кВт)"]-old_data["Нічне_споживання(кВт)"]
        price_night = differens_night * standard_tariff_night
    else:
        price_night = (new_data_copy["Нічне_споживання(кВт)"] - old_data["Нічне_споживання(кВт)"]) * standard_tariff_night

    res_day_price = price_night + price_day
    res_price = old_data["Загальна сума оплати на теперішню дату"]+res_day_price

    new_data_copy['Загальна сума оплати на теперішню дату']=res_price


    print(f"-------------------------------- Результат обрахунку для лічильника № {new_data_copy['ID']} --------------------------------")
    print(f"Станом на {old_data['Дата']} лічильник №{old_data['ID']} нарахував: {old_data['Денне_споживання(кВт)']} кВт вдень.")
    print(f"Станом на {old_data['Дата']} лічильник №{old_data['ID']} нарахував: {old_data['Нічне_споживання(кВт)']} кВт вночі.")
    print(f"--------------------------------------------------------------------------------------------------------------------")
    print(f"Станом на {new_data_copy['Дата']} лічильник №{new_data_copy['ID']} нарахував: {new_data_copy['Денне_споживання(кВт)']} кВт вдень.")
    print(f"Станом на {new_data_copy['Дата']} лічильник №{new_data_copy['ID']} нарахував: {new_data_copy['Нічне_споживання(кВт)']} кВт вночі.")
    print(f"--------------------------------------------------------------------------------------------------------------------")
    print(f"Плата за {new_data_copy['Дата']} для лічильника №{new_data_copy['ID']} становить: {res_day_price:.2f} грн")

    Information_storage[old_index] = copy.deepcopy(new_data_copy)



test_data = [
    {"ID": 1, "Дата": "02.03.2025", "Денне_споживання(кВт)": 30.5, "Нічне_споживання(кВт)": 8.5 ,"Загальна сума оплати на теперішню дату":0},
    {"ID": 2, "Дата": "02.03.2025", "Денне_споживання(кВт)": 43.1, "Нічне_споживання(кВт)": 9.5 ,"Загальна сума оплати на теперішню дату":0},
    {"ID": 3, "Дата": "02.03.2025", "Денне_споживання(кВт)": 55.5, "Нічне_споживання(кВт)": 25.5, "Загальна сума оплати на теперішню дату":0},
    {"ID": 4, "Дата": "02.03.2025", "Денне_споживання(кВт)": 66, "Нічне_споживання(кВт)": 45.5, "Загальна сума оплати на теперішню дату":0},
]

for i in test_data:
    Calculate_price(i)
print("\n")
for Element in Information_storage:
    print(f"Лічильник №{Element['ID']}, Дата: {Element['Дата']}, "
          f"Денне споживання: {Element['Денне_споживання(кВт)']} кВт, "
          f"Нічне споживання: {Element['Нічне_споживання(кВт)']} кВт "
          f"Загальна сума оплати на теперішню дату: {Element['Загальна сума оплати на теперішню дату']} грн ")

with open('hist.txt', 'a') as file:
    for Element in Information_storage:
        file.write(f"Лічильник №{Element['ID']}, Дата: {Element['Дата']}, "
                   f"Денне споживання: {Element['Денне_споживання(кВт)']} кВт, "
                   f"Нічне споживання: {Element['Нічне_споживання(кВт)']} кВт "
                   f"Загальна сума оплати на теперішню дату: {Element['Загальна сума оплати на теперішню дату']} грн\n")
    file.write("\n")
