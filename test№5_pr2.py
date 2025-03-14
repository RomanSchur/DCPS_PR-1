#* тест отримання показників з заниженими нічними та денними показниками
import unittest
import copy

class test1_pr2(unittest.TestCase):
   def test(self):
        standard_tariff_day = 26.4
        standard_tariff_night = 21.6
        nakrytka_day = 100
        nakrytka_night = 80

        Information_storage = [{"ID": 1, "Дата": "01.03.2025", "Денне_споживання(кВт)": 40.5, "Нічне_споживання(кВт)": 10.5, "Загальна сума оплати на теперішню дату": 1296},]
        def Calculate_price(new_data):
            old_data = next((i for i in Information_storage if i["ID"] == new_data["ID"]), None)
            old_index = next((index for index, i in enumerate(Information_storage) if i["ID"] == new_data["ID"]), None)
            new_data_copy = copy.deepcopy(new_data)

            if old_data is None:
                res_price = new_data_copy['Денне_споживання(кВт)'] * standard_tariff_day + new_data_copy['Нічне_споживання(кВт)'] * standard_tariff_night
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
                differens_night = new_data_copy["Нічне_споживання(кВт)"] - old_data["Нічне_споживання(кВт)"]
                price_night = differens_night * standard_tariff_night
            else:
                price_night = (new_data_copy["Нічне_споживання(кВт)"] - old_data["Нічне_споживання(кВт)"]) * standard_tariff_night

            res_day_price = price_night + price_day
            res_price = old_data["Загальна сума оплати на теперішню дату"] + res_day_price

            new_data_copy['Загальна сума оплати на теперішню дату'] = res_price

            Information_storage[old_index] = copy.deepcopy(new_data_copy)

        #Створення тестових даних та перевірка
        new_data = {"ID": 1, "Дата": "02.03.2025", "Денне_споживання(кВт)": 35.5, "Нічне_споживання(кВт)": 5.5, "Загальна сума оплати на теперішню дату": 0}
        Calculate_price(new_data)
        updated_data = next(i for i in Information_storage if i["ID"] == 1)
        self.assertEqual(updated_data["Денне_споживання(кВт)"], 135.5)
        self.assertEqual(updated_data["Нічне_споживання(кВт)"], 85.5)
        self.assertEqual(updated_data["Загальна сума оплати на теперішню дату"], 5424)

