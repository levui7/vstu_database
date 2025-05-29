# import tkinter as tk
# from tkinter import ttk, messagebox
#
# import database_connector as db
# from database_config import db_farm_id
#
#
# class FarmApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title(f"Управление Фермой)")
#         self.root.geometry("1100x750")
#
#         # ID фермы
#         self.current_farm_id = db_farm_id
#
#         # Словари для хранения StringVar для продукта
#         # Продукты
#         self.product_vars = {}
#         self.selected_product_id = None
#         # Рекламодатели
#         self.advertiser_vars = {}
#         self.selected_advertiser_id = None
#         # Амбары
#         self.barn_vars = {}
#         self.selected_barn_id = None
#         # Фермеры
#         self.farmer_vars = {}
#         self.selected_farmer_id = None
#         # Поля
#         self.field_vars = {}
#         self.selected_field_id = None
#         # Данные фермы
#         self.farm_edit_vars = {}
#
#         self.create_widgets()
#         self.load_initial_data()
#
#     def create_widgets(self):
#         self.notebook = ttk.Notebook(self.root)
#
#         # --- Вкладка "Данные Фермы" (для редактирования текущей фермы) ---
#         self.manage_farm_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.manage_farm_tab, text=f'Данные Фермы (ID:{self.current_farm_id})')
#         self.create_manage_farm_widgets(self.manage_farm_tab)
#
#         # --- Вкладка "Продукты" ---
#         self.product_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.product_tab, text='Продукты')
#         self.create_product_widgets(self.product_tab)
#
#         # --- Вкладка "Рекламодатели" ---
#         self.advertiser_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.advertiser_tab, text='Рекламодатели')
#         self.create_advertiser_widgets(self.advertiser_tab)
#
#         # --- Вкладка "Амбары" ---
#         self.barn_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.barn_tab, text='Амбары')
#         self.create_barn_widgets(self.barn_tab)
#
#         # --- Вкладка "Фермеры" ---
#         self.farmer_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.farmer_tab, text='Фермеры')
#         self.create_farmer_widgets(self.farmer_tab)
#
#         # --- Вкладка "Поля (земли)" ---
#         self.field_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.field_tab, text='Поля')
#         self.create_field_widgets(self.field_tab)
#
#         self.notebook.pack(expand=True, fill='both', padx=5, pady=5)
#
#     def load_initial_data(self):
#         self.load_current_farm_data_to_form()
#         self.load_products_data()
#         self.load_advertisers_data()
#         self.load_barns_data()
#         self.load_farmers_data()
#         self.load_fields_data()
#
#     # ----------------------------------
#     # CRUD для вкладки "Данные Фермы"
#     # ----------------------------------
#     def create_manage_farm_widgets(self, parent_tab):
#         self.farm_edit_vars['name'] = tk.StringVar()
#         self.farm_edit_vars['address'] = tk.StringVar()
#         self.farm_edit_vars['asset_cost'] = tk.StringVar()
#
#         frame = ttk.LabelFrame(parent_tab, text=f"Редактирование данных Фермы ID: {self.current_farm_id}")
#         frame.pack(padx=10, pady=10, fill="x")
#
#         ttk.Label(frame, text="Название:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
#         ttk.Entry(frame, textvariable=self.farm_edit_vars['name'], width=50).grid(row=0, column=1, sticky="ew", padx=5,
#                                                                                   pady=2)
#         ttk.Label(frame, text="Адрес:").grid(row=1, column=0, sticky="w", padx=5, pady=2)
#         ttk.Entry(frame, textvariable=self.farm_edit_vars['address'], width=50).grid(row=1, column=1, sticky="ew",
#                                                                                      padx=5, pady=2)
#         ttk.Label(frame, text="Стоимость активов:").grid(row=2, column=0, sticky="w", padx=5, pady=2)
#         ttk.Entry(frame, textvariable=self.farm_edit_vars['asset_cost'], width=50).grid(row=2, column=1, sticky="ew",
#                                                                                         padx=5, pady=2)
#
#         ttk.Button(frame, text="Сохранить изменения", command=self.save_current_farm_details).grid(row=3, column=0,
#                                                                                                    columnspan=2,
#                                                                                                    pady=10)
#         ttk.Button(frame, text="Обновить форму", command=self.load_current_farm_data_to_form).grid(row=4, column=0,
#                                                                                                    columnspan=2, pady=5)
#
#     def load_current_farm_data_to_form(self):
#         farm_data = db.get_farm_by_id(
#             self.current_farm_id)
#         if farm_data:
#             self.farm_edit_vars['name'].set(farm_data.get('name', ''))
#             self.farm_edit_vars['address'].set(farm_data.get('address', ''))
#             ac = farm_data.get('asset_cost')
#             self.farm_edit_vars['asset_cost'].set(str(ac) if ac is not None else '')
#         else:
#             messagebox.showerror("Ошибка", f"Не удалось загрузить данные для фермы ID: {self.current_farm_id}")
#
#     def save_current_farm_details(self):
#         name = self.farm_edit_vars['name'].get().strip()
#         address = self.farm_edit_vars['address'].get().strip()
#         asset_cost_str = self.farm_edit_vars['asset_cost'].get().strip()
#         try:
#             asset_cost = float(asset_cost_str) if asset_cost_str else None
#         except ValueError:
#             messagebox.showerror("Ошибка ввода", "Стоимость активов должна быть числом.")
#             return
#         if not name:  # Имя не должно быть пустым
#             messagebox.showerror("Ошибка ввода", "Название фермы не может быть пустым.")
#             return
#
#         if db.update_farm_details(self.current_farm_id, name, address, asset_cost):
#             messagebox.showinfo("Успех", "Данные фермы обновлены.")
#         else:
#             messagebox.showerror("Ошибка БД", f"Не удалось обновить данные фермы ID {self.current_farm_id}.")
#
#     # ----------------------------
#     # CRUD для вкладки "Продукты"
#     # ----------------------------
#     def create_product_widgets(self, parent_tab):
#         self.product_vars = {
#             'category': tk.StringVar(), 'price': tk.StringVar(), 'volume': tk.StringVar(),
#             'supplier_id': tk.StringVar(), 'advertiser_id': tk.StringVar(), 'market_id': tk.StringVar(),
#             'distributor_id': tk.StringVar(), 'barn_id': tk.StringVar(), 'livestock_id': tk.StringVar(),
#             'field_id': tk.StringVar()
#         }
#
#         input_frame = ttk.LabelFrame(parent_tab, text="Данные Продукта")
#         input_frame.pack(padx=10, pady=5, fill="x")
#
#         product_fields_labels = {
#             'category': "Категория:", 'price': "Цена:", 'volume': "Объем:",
#             'supplier_id': "ID Поставщика:", 'advertiser_id': "ID Рекламодателя:",
#             'market_id': "ID Рынка:", 'distributor_id': "ID Дистрибьютора:",
#             'barn_id': "ID Амбара:", 'livestock_id': "ID Скота:", 'field_id': "ID Поля:"
#         }
#         row_idx = 0
#         col_idx = 0
#         for key, label_text in product_fields_labels.items():
#             ttk.Label(input_frame, text=label_text).grid(row=row_idx, column=col_idx, sticky="w", padx=5, pady=2)
#             ttk.Entry(input_frame, textvariable=self.product_vars[key], width=25).grid(row=row_idx, column=col_idx + 1,
#                                                                                        sticky="ew", padx=5, pady=2)
#             col_idx += 2
#             if col_idx >= 4:  # Переход на новую строку после 2х пар Label-Entry
#                 col_idx = 0
#                 row_idx += 1
#
#         # Кнопки
#         button_frame = ttk.Frame(input_frame)
#         button_frame.grid(row=row_idx + 1, column=0, columnspan=4, pady=10)
#         self.add_product_btn = ttk.Button(button_frame, text="Добавить", command=self.add_product_gui)
#         self.add_product_btn.pack(side=tk.LEFT, padx=5)
#         self.update_product_btn = ttk.Button(button_frame, text="Обновить", command=self.update_product_gui,
#                                              state=tk.DISABLED)
#         self.update_product_btn.pack(side=tk.LEFT, padx=5)
#         self.delete_product_btn = ttk.Button(button_frame, text="Удалить", command=self.delete_product_gui,
#                                              state=tk.DISABLED)
#         self.delete_product_btn.pack(side=tk.LEFT, padx=5)
#         ttk.Button(button_frame, text="Очистить", command=self.clear_product_fields).pack(side=tk.LEFT, padx=5)
#
#         # Treeview для списка продуктов
#         tree_frame = ttk.LabelFrame(parent_tab, text="Список Продуктов")
#         tree_frame.pack(padx=10, pady=5, fill="both", expand=True)
#
#         # Колонки в том порядке, в котором они будут в values кортеже
#         self.product_tree_columns = ("id", "category", "price", "volume", "supplier_id", "advertiser_id",
#                                      "market_id", "distributor_id", "barn_id", "livestock_id", "field_id")
#         self.product_tree = ttk.Treeview(tree_frame, columns=self.product_tree_columns, show="headings")
#
#         for col in self.product_tree_columns:
#             self.product_tree.heading(col, text=col.replace("_id", " ID").replace("_", " ").title())
#             self.product_tree.column(col, width=70 if "_id" in col or col == "id" else 120,
#                                      anchor=tk.W if col == "category" else tk.CENTER)
#
#         prod_scroll_y = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.product_tree.yview)
#         self.product_tree.configure(yscroll=prod_scroll_y.set)
#         prod_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
#         prod_scroll_x = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL, command=self.product_tree.xview)
#         self.product_tree.configure(xscroll=prod_scroll_x.set)
#         prod_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
#         self.product_tree.pack(fill="both", expand=True)
#         self.product_tree.bind("<<TreeviewSelect>>", self.on_product_tree_select)
#
#     def load_products_data(self):
#         for item in self.product_tree.get_children():
#             self.product_tree.delete(item)
#         products = db.get_all_products_for_farm(self.current_farm_id)
#         for p_dict in products:
#             # Собираем значения в порядке колонок Treeview
#             values = [p_dict.get(col_name, '') for col_name in self.product_tree_columns]
#             self.product_tree.insert("", tk.END, values=tuple(values))
#
#     def clear_product_fields(self):
#         for key in self.product_vars:
#             self.product_vars[key].set("")
#         self.selected_product_id = None
#         self.add_product_btn.config(state=tk.NORMAL)
#         self.update_product_btn.config(state=tk.DISABLED)
#         self.delete_product_btn.config(state=tk.DISABLED)
#         if self.product_tree.selection():
#             self.product_tree.selection_remove(self.product_tree.selection()[0])
#
#     def on_product_tree_select(self, event):
#         selected_items = self.product_tree.selection()
#         if not selected_items: return
#
#         values_tuple = self.product_tree.item(selected_items[0], "values")
#         if values_tuple:
#             self.selected_product_id = values_tuple[0]  # id
#             # Заполняем StringVar из product_vars, сопоставляя с product_tree_columns
#             for i, col_name in enumerate(self.product_tree_columns):
#                 if col_name != 'id' and col_name in self.product_vars:  # id не в форме
#                     self.product_vars[col_name].set(str(values_tuple[i]) if values_tuple[i] is not None else "")
#
#             self.add_product_btn.config(state=tk.DISABLED)
#             self.update_product_btn.config(state=tk.NORMAL)
#             self.delete_product_btn.config(state=tk.NORMAL)
#
#     def _collect_product_data_from_form(self):
#         data = {}
#         try:
#             for key, var in self.product_vars.items():
#                 value_str = var.get().strip()
#                 if "_id" in key:  # Поля внешних ключей
#                     data[key] = int(value_str) if value_str else None
#                 elif key in ['price', 'volume']:  # Числовые поля
#                     data[key] = float(value_str) if value_str else None
#                 else:  # Текстовые поля
#                     data[key] = value_str if value_str else None
#
#             if not data.get('category'):  # Обязательное поле
#                 messagebox.showerror("Ошибка ввода", "Категория продукта не может быть пустой.")
#                 return None
#             return data
#         except ValueError:
#             messagebox.showerror("Ошибка ввода", "Проверьте числовые поля (Цена, Объем, ID).")
#             return None
#
#     def add_product_gui(self):
#         product_data = self._collect_product_data_from_form()
#         if product_data is None: return
#
#         # farm_id будет добавлен функцией create_product по умолчанию
#         new_id = db.create_product(**product_data, farm_id=self.current_farm_id)
#         if new_id:
#             messagebox.showinfo("Успех", f"Продукт '{product_data.get('category')}' добавлен с ID: {new_id}.")
#             self.load_products_data()
#             self.clear_product_fields()
#         else:
#             messagebox.showerror("Ошибка БД", "Не удалось добавить продукт.")
#
#     def update_product_gui(self):
#         if self.selected_product_id is None:
#             messagebox.showwarning("Внимание", "Выберите продукт для обновления.")
#             return
#         product_data = self._collect_product_data_from_form()
#         if product_data is None: return
#
#         if db.update_product(self.selected_product_id, **product_data, farm_id=self.current_farm_id):
#             messagebox.showinfo("Успех", f"Продукт ID {self.selected_product_id} обновлен.")
#             self.load_products_data()
#             self.clear_product_fields()
#         else:
#             messagebox.showerror("Ошибка БД", f"Не удалось обновить продукт ID {self.selected_product_id}.")
#
#     def delete_product_gui(self):
#         if self.selected_product_id is None:
#             messagebox.showwarning("Внимание", "Выберите продукт для удаления.")
#             return
#
#         category_to_delete = self.product_vars['category'].get()
#         if messagebox.askyesno("Подтверждение",
#                                f"Удалить продукт '{category_to_delete}' (ID: {self.selected_product_id})?"):
#             if db.delete_product(self.selected_product_id):
#                 messagebox.showinfo("Успех", "Продукт удален.")
#                 self.load_products_data()
#                 self.clear_product_fields()
#             else:
#                 messagebox.showerror("Ошибка БД", "Не удалось удалить продукт.")
#
#     # -------------------------------------------------------------------
#     # ЗАГОТОВКИ для других вкладок (Advertiser, Barn, Farmer, Field)
#     # Вам нужно будет реализовать их по аналогии с Product
#     # -------------------------------------------------------------------
#
#     def create_advertiser_widgets(self, parent_tab):
#         # TODO: Создать поля ввода (self.advertiser_vars), кнопки и Treeview (self.advertiser_tree)
#         ttk.Label(parent_tab, text="CRUD для Рекламодателей будет здесь").pack(padx=20, pady=20)
#         pass
#
#     def load_advertisers_data(self):
#         # TODO: Вызвать db.get_all_advertisers() и заполнить self.advertiser_tree
#         pass
#
#     def clear_advertiser_fields(self):
#         pass
#
#     def on_advertiser_tree_select(self, event):
#         pass
#
#     def _collect_advertiser_data_from_form(self):
#         pass  # return data_dict or None
#
#     def add_advertiser_gui(self):
#         pass
#
#     def update_advertiser_gui(self):
#         pass
#
#     def delete_advertiser_gui(self):
#         pass
#
#     def create_barn_widgets(self, parent_tab):
#         ttk.Label(parent_tab, text="CRUD для Амбаров будет здесь").pack(padx=20, pady=20)
#         pass
#
#     def load_barns_data(self):
#         pass
#
#     def clear_barn_fields(self):
#         pass
#
#     def on_barn_tree_select(self, event):
#         pass
#
#     def _collect_barn_data_from_form(self):
#         pass
#
#     def add_barn_gui(self):
#         pass
#
#     def update_barn_gui(self):
#         pass
#
#     def delete_barn_gui(self):
#         pass
#
#     def create_farmer_widgets(self, parent_tab):
#         ttk.Label(parent_tab, text="CRUD для Фермеров будет здесь").pack(padx=20, pady=20)
#         pass
#
#     def load_farmers_data(self):
#         pass
#
#     def clear_farmer_fields(self):
#         pass
#
#     def on_farmer_tree_select(self, event):
#         pass
#
#     def _collect_farmer_data_from_form(self):
#         pass
#
#     def add_farmer_gui(self):
#         pass
#
#     def update_farmer_gui(self):
#         pass
#
#     def delete_farmer_gui(self):
#         pass
#
#     def create_field_widgets(self, parent_tab):
#         ttk.Label(parent_tab, text="CRUD для Полей (земли) будет здесь").pack(padx=20, pady=20)
#         pass
#
#     def load_fields_data(self):
#         pass
#
#     def clear_field_fields(self):
#         pass
#
#     def on_field_tree_select(self, event):
#         pass
#
#     def _collect_field_data_from_form(self):
#         pass
#
#     def add_field_gui(self):
#         pass
#
#     def update_field_gui(self):
#         pass
#
#     def delete_field_gui(self):
#         pass
#
#
# if __name__ == "__main__":
#     main_window = tk.Tk()
#     app = FarmApp(main_window)
#     main_window.mainloop()

from crud_files import (
    get_farm_by_id, update_farm_details,
    create_product, get_all_products, get_product_by_id, update_product, delete_product,
    create_advertiser, get_all_advertisers, get_advertiser_by_id, update_advertiser, delete_advertiser,
    create_barn, get_all_barns, get_barn_by_id, update_barn, delete_barn,
    create_farmer, get_all_farmers, get_farmer_by_id, update_farmer, delete_farmer,
    create_field, get_all_fields, get_field_by_id, update_field, delete_field
)


def get_int_input(prompt, allow_empty=False):
    """Получает целочисленный ввод от пользователя."""
    while True:
        try:
            value_str = input(prompt).strip()
            if allow_empty and not value_str:
                return None
            return int(value_str)
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")


def get_float_input(prompt, allow_empty=False):
    """Получает ввод числа с плавающей точкой от пользователя."""
    while True:
        try:
            value_str = input(prompt).strip()
            if allow_empty and not value_str:
                return None
            return float(value_str)
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите десятичное число.")


def get_string_input(prompt, allow_empty=False):
    """Получает строковый ввод от пользователя."""
    while True:
        value = input(prompt).strip()
        if not allow_empty and not value:
            print("Ввод не может быть пустым.")
            continue
        return value


# --- UI для Ферм ---

def ui_view_farms():
    print("\n--- Ферма ---")
    farms = get_farm_by_id()
    if not farms:
        print("Фермы не найдены.")
        return
    for farm in farms:
        # Используем имена полей, как они возвращаются из get_all_farms (с JOIN)
        market_display = farm.get('market_name', farm.get('market_id', 'N/A'))
        product_display = farm.get('product_category', farm.get('product_id', 'N/A'))
        print(f"ID: {farm['id']}, Название: {farm['name']}, Адрес: {farm['address']}, "
              f"Стоимость активов: {farm['asset_cost']:.2f}, Рынок: {market_display}, Продукт: {product_display}")


def ui_edit_farm():
    print("\n--- Редактировать ферму ---")
    farm_id = get_int_input("Введите ID фермы для редактирования: ")
    farm = get_farm_by_id(farm_id)  # Эта функция должна вернуть ферму с ID для FK
    if not farm:
        print("Ферма не найдена.")
        return

    print(f"Редактирование фермы: {farm['name']}")
    address = get_string_input(f"Новый адрес (текущий: {farm['address']}): ", allow_empty=True) or farm['address']
    asset_cost = get_float_input(f"Новая стоимость активов (текущая: {farm['asset_cost']}): ", allow_empty=True) or \
                 farm['asset_cost']
    name = get_string_input(f"Новое название (текущее: {farm['name']}): ", allow_empty=True) or farm['name']
    market_id = get_int_input(f"Новый ID рынка (текущий: {farm['market_id']}): ", allow_empty=True) or farm['market_id']
    product_id = get_int_input(f"Новый ID продукта (текущий: {farm.get('product_id', '')}): ", allow_empty=True)
    if product_id is None and 'product_id' in farm:  # если оставили пустым, но было значение
        product_id = farm['product_id']

    update_farm_details(farm_id, address, asset_cost, name, market_id, product_id)



# --- UI для Продуктов ---
def ui_add_product():
    print("\n--- Добавить новый продукт ---")
    # Показать доступные фермы для выбора farm_id
    print("Доступные фермы:")
    farms = get_farm_by_id()  # Получаем фермы с их именами
    if not farms:
        print("Нет доступных ферм. Пожалуйста, сначала добавьте ферму.")
        return
    for f_item in farms:
        print(f"  ID: {f_item['id']}, Название: {f_item['name']}")

    farm_id = get_int_input("Введите ID фермы для этого продукта: ")

    price = get_float_input("Введите цену продукта: ")
    category = get_string_input("Введите категорию продукта: ")
    volume = get_float_input("Введите объем/количество продукта: ")
    # Для других FK, как и требовалось, вводим ID
    print("Подсказка: Убедитесь, что ID для связанных таблиц существуют.")
    supplier_id = get_int_input("Введите ID поставщика: ", allow_empty=True)
    advertiser_id = get_int_input("Введите ID рекламодателя: ", allow_empty=True)
    market_id = get_int_input("Введите ID рынка: ", allow_empty=True)
    distributor_id = get_int_input("Введите ID дистрибьютора: ", allow_empty=True)
    barn_id = get_int_input("Введите ID амбара: ", allow_empty=True)
    livestock_id = get_int_input("Введите ID скота: ", allow_empty=True)
    field_id = get_int_input("Введите ID поля: ", allow_empty=True)

    create_product(price, category, volume, farm_id, supplier_id, advertiser_id,
                   market_id, distributor_id, barn_id, livestock_id, field_id)


def ui_view_products():
    print("\n--- Список продуктов ---")
    products = get_all_products()
    if not products:
        print("Продукты не найдены.")
        return
    for p in products:
        print(f"ID: {p['id']}, Категория: {p['category']}, Цена: {p.get('price', 0):.2f}, Объем: {p.get('volume', 0)}")
        print(f"  Ферма: {p.get('farm_name', 'N/A')} (ID: {p.get('farm_id', 'N/A')})")
        print(f"  Поставщик: {p.get('supplier_name', 'N/A')} (ID: {p.get('supplier_id', 'N/A')})")
        print(f"  Рекламодатель: {p.get('advertiser_name', 'N/A')} (ID: {p.get('advertiser_id', 'N/A')})")
        print(f"  Рынок: {p.get('market_name', 'N/A')} (ID: {p.get('market_id', 'N/A')})")
        print(f"  Дистрибьютор: {p.get('distributor_name', 'N/A')} (ID: {p.get('distributor_id', 'N/A')})")
        print(f"  Амбар: {p.get('barn_identifier', 'N/A')} (ID: {p.get('barn_id', 'N/A')})")
        print(f"  Скот: {p.get('livestock_category', 'N/A')} (ID: {p.get('livestock_id', 'N/A')})")
        print(f"  Поле: {p.get('field_identifier', 'N/A')} (ID: {p.get('field_id', 'N/A')})")
        print("-" * 30)


def ui_edit_product():
    print("\n--- Редактировать продукт ---")
    product_id_to_edit = get_int_input("Введите ID продукта для редактирования: ")
    product = get_product_by_id(product_id_to_edit)  # Эта функция должна возвращать все ID FK
    if not product:
        print("Продукт не найден.")
        return

    print(f"Редактирование продукта: {product.get('category', '')} с фермы {product.get('farm_name', '')}")

    print("Доступные фермы (для изменения farm_id):")
    farms = get_farm_by_id()
    for f_item in farms:
        print(f"  ID: {f_item['id']}, Название: {f_item['name']}")

    price = get_float_input(f"Новая цена (текущая: {product.get('price', 0):.2f}): ", allow_empty=True) or product.get(
        'price')
    category = get_string_input(f"Новая категория (текущая: {product.get('category', '')}): ",
                                allow_empty=True) or product.get('category')
    volume = get_float_input(f"Новый объем (текущий: {product.get('volume', 0)}): ", allow_empty=True) or product.get(
        'volume')
    farm_id = get_int_input(f"Новый ID фермы (текущий: {product.get('farm_id', '')}): ",
                            allow_empty=True) or product.get('farm_id')

    supplier_id = get_int_input(f"Новый ID поставщика (текущий: {product.get('supplier_id', '')}): ",
                                allow_empty=True) or product.get('supplier_id')
    advertiser_id = get_int_input(f"Новый ID рекламодателя (текущий: {product.get('advertiser_id', '')}): ",
                                  allow_empty=True) or product.get('advertiser_id')
    market_id = get_int_input(f"Новый ID рынка (текущий: {product.get('market_id', '')}): ",
                              allow_empty=True) or product.get('market_id')
    distributor_id = get_int_input(f"Новый ID дистрибьютора (текущий: {product.get('distributor_id', '')}): ",
                                   allow_empty=True) or product.get('distributor_id')
    barn_id = get_int_input(f"Новый ID амбара (текущий: {product.get('barn_id', '')}): ",
                            allow_empty=True) or product.get('barn_id')
    livestock_id = get_int_input(f"Новый ID скота (текущий: {product.get('livestock_id', '')}): ",
                                 allow_empty=True) or product.get('livestock_id')
    field_id = get_int_input(f"Новый ID поля (текущий: {product.get('field_id', '')}): ",
                             allow_empty=True) or product.get('field_id')

    update_product(product_id_to_edit, price, category, volume, farm_id, supplier_id, advertiser_id, market_id,
                   distributor_id, barn_id, livestock_id, field_id)


def ui_delete_product():
    print("\n--- Удалить продукт ---")
    product_id_to_delete = get_int_input("Введите ID продукта для удаления: ")
    confirm = get_string_input(f"Вы уверены, что хотите удалить продукт ID {product_id_to_delete}? (да/нет): ").lower()
    if confirm == 'да':
        delete_product(product_id_to_delete)
    else:
        print("Удаление отменено.")


# --- UI для Рекламодателей (Advertiser) ---
def ui_add_advertiser():
    print("\n--- Добавить нового рекламодателя ---")
    company_name = get_string_input("Название компании: ")
    contact_person = get_string_input("Контактное лицо: ", allow_empty=True)
    email = get_string_input("Email: ", allow_empty=True)
    phone = get_string_input("Телефон: ", allow_empty=True)
    effectiveness = get_int_input("Эффективность (число): ", allow_empty=True)
    service_cost = get_float_input("Стоимость услуг: ", allow_empty=True)
    create_advertiser(company_name, contact_person, email, phone, effectiveness, service_cost)


def ui_view_advertisers():
    print("\n--- Список рекламодателей ---")
    advertisers = get_all_advertisers()
    if not advertisers:
        print("Рекламодатели не найдены.")
        return
    for ad in advertisers:
        print(f"ID: {ad['id']}, Компания: {ad['company_name']}, Контакт: {ad.get('contact_person', 'N/A')}, "
              f"Email: {ad.get('email', 'N/A')}, Телефон: {ad.get('phone', 'N/A')}, "
              f"Эффективность: {ad.get('effectiveness', 'N/A')}, Стоимость: {ad.get('service_cost', 0.0):.2f}")


def ui_edit_advertiser():
    print("\n--- Редактировать рекламодателя ---")
    ad_id = get_int_input("Введите ID рекламодателя для редактирования: ")
    advertiser = get_advertiser_by_id(ad_id)
    if not advertiser:
        print("Рекламодатель не найден.")
        return

    print(f"Редактирование: {advertiser['company_name']}")
    company_name = get_string_input(f"Новое название компании (тек: {advertiser['company_name']}): ", True) or \
                   advertiser['company_name']
    contact_person = get_string_input(f"Новое контактное лицо (тек: {advertiser.get('contact_person', '')}): ",
                                      True) or advertiser.get('contact_person')
    email = get_string_input(f"Новый email (тек: {advertiser.get('email', '')}: ", True) or advertiser.get('email')
    phone = get_string_input(f"Новый телефон (тек: {advertiser.get('phone', '')}: ", True) or advertiser.get('phone')
    effectiveness = get_int_input(f"Новая эффективность (тек: {advertiser.get('effectiveness', '')}: ",
                                  True) or advertiser.get('effectiveness')
    service_cost = get_float_input(f"Новая стоимость (тек: {advertiser.get('service_cost', 0.0)}: ",
                                   True) or advertiser.get('service_cost')

    update_advertiser(ad_id, company_name, contact_person, email, phone, effectiveness, service_cost)


def ui_delete_advertiser():
    print("\n--- Удалить рекламодателя ---")
    ad_id = get_int_input("Введите ID рекламодателя для удаления: ")
    confirm = get_string_input(f"Вы уверены, что хотите удалить рекламодателя ID {ad_id}? (да/нет): ").lower()
    if confirm == 'да':
        delete_advertiser(ad_id)
    else:
        print("Удаление отменено.")