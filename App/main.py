import app_gui


def main_menu():
    """Отображает главное меню и обрабатывает выбор пользователя."""
    while True:
        print("\n===== Система управления фермой =====")
        print("Язык: Python, Библиотека БД: mysql-connector-python")
        print("GitHub Repo: https://github.com/levui7/vstu_database")

        print("\n--- Операции с Фермами (Farm) ---")
        print("1. Добавить ферму")
        print("2. Показать все фермы")
        print("3. Редактировать ферму")
        print("4. Удалить ферму")

        print("\n--- Операции с Продуктами (Product) ---")
        print("5. Добавить продукт")
        print("6. Показать все продукты")
        print("7. Редактировать продукт")
        print("8. Удалить продукт")

        print("\n--- Операции с Рекламодателями (Advertiser) ---")
        print("9. Добавить рекламодателя")
        print("10. Показать всех рекламодателей")
        print("11. Редактировать рекламодателя")
        print("12. Удалить рекламодателя")

        # Добавьте здесь пункты меню для Barn, Farmer, Field, когда они будут готовы
        # print("\n--- Операции с Амбарами (Barn) ---")
        # print("13. ...")

        print("\n--- Аналитические запросы ---")
        print("20. Дорогие продукты на определенной ферме")
        print("21. Фермы по стоимости активов и сегменту рынка")

        print("\n0. Выход")

        choice = input("Введите ваш выбор: ")

        if choice == '1':
            app_gui.ui_add_farm()
        elif choice == '2':
            app_gui.ui_view_farms()
        elif choice == '3':
            app_gui.ui_edit_farm()
        elif choice == '4':
            app_gui.ui_delete_farm()
        elif choice == '5':
            app_gui.ui_add_product()
        elif choice == '6':
            app_gui.ui_view_products()
        elif choice == '7':
            app_gui.ui_edit_product()
        elif choice == '8':
            app_gui.ui_delete_product()
        elif choice == '9':
            app_gui.ui_add_advertiser()
        elif choice == '10':
            app_gui.ui_view_advertisers()
        elif choice == '11':
            app_gui.ui_edit_advertiser()
        elif choice == '12':
            app_gui.ui_delete_advertiser()
        elif choice == '0':
            print("Выход из приложения.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main_menu()