import tkinter as tk
from tkinter import ttk, messagebox

import database_connector as db
from database_config import db_farm_id


class FarmApp:
    def __init__(self, root):
        self.root = root
        self.root.title(f"Управление Фермой)")
        self.root.geometry("1100x750")

        # ID фермы
        self.current_farm_id = db_farm_id

        # Словари для хранения StringVar для продукта
        # Продукты
        self.product_vars = {}
        self.selected_product_id = None
        # Рекламодатели
        self.advertiser_vars = {}
        self.selected_advertiser_id = None
        # Амбары
        self.barn_vars = {}
        self.selected_barn_id = None
        # Фермеры
        self.farmer_vars = {}
        self.selected_farmer_id = None
        # Поля
        self.field_vars = {}
        self.selected_field_id = None
        # Данные фермы
        self.farm_edit_vars = {}

        self.create_widgets()
        self.load_initial_data()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root)

        # --- Вкладка "Данные Фермы" (для редактирования текущей фермы) ---
        self.manage_farm_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.manage_farm_tab, text=f'Данные Фермы (ID:{self.current_farm_id})')
        self.create_manage_farm_widgets(self.manage_farm_tab)

        # --- Вкладка "Продукты" ---
        self.product_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.product_tab, text='Продукты')
        self.create_product_widgets(self.product_tab)

        # --- Вкладка "Рекламодатели" ---
        self.advertiser_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.advertiser_tab, text='Рекламодатели')
        self.create_advertiser_widgets(self.advertiser_tab)

        # --- Вкладка "Амбары" ---
        self.barn_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.barn_tab, text='Амбары')
        self.create_barn_widgets(self.barn_tab)

        # --- Вкладка "Фермеры" ---
        self.farmer_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.farmer_tab, text='Фермеры')
        self.create_farmer_widgets(self.farmer_tab)

        # --- Вкладка "Поля (земли)" ---
        self.field_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.field_tab, text='Поля')
        self.create_field_widgets(self.field_tab)

        self.notebook.pack(expand=True, fill='both', padx=5, pady=5)

    def load_initial_data(self):
        self.load_current_farm_data_to_form()
        self.load_products_data()
        self.load_advertisers_data()
        self.load_barns_data()
        self.load_farmers_data()
        self.load_fields_data()

    # ----------------------------------
    # CRUD для вкладки "Данные Фермы"
    # ----------------------------------
    def create_manage_farm_widgets(self, parent_tab):
        self.farm_edit_vars['name'] = tk.StringVar()
        self.farm_edit_vars['address'] = tk.StringVar()
        self.farm_edit_vars['asset_cost'] = tk.StringVar()

        frame = ttk.LabelFrame(parent_tab, text=f"Редактирование данных Фермы ID: {self.current_farm_id}")
        frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(frame, text="Название:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        ttk.Entry(frame, textvariable=self.farm_edit_vars['name'], width=50).grid(row=0, column=1, sticky="ew", padx=5,
                                                                                  pady=2)
        ttk.Label(frame, text="Адрес:").grid(row=1, column=0, sticky="w", padx=5, pady=2)
        ttk.Entry(frame, textvariable=self.farm_edit_vars['address'], width=50).grid(row=1, column=1, sticky="ew",
                                                                                     padx=5, pady=2)
        ttk.Label(frame, text="Стоимость активов:").grid(row=2, column=0, sticky="w", padx=5, pady=2)
        ttk.Entry(frame, textvariable=self.farm_edit_vars['asset_cost'], width=50).grid(row=2, column=1, sticky="ew",
                                                                                        padx=5, pady=2)

        ttk.Button(frame, text="Сохранить изменения", command=self.save_current_farm_details).grid(row=3, column=0,
                                                                                                   columnspan=2,
                                                                                                   pady=10)
        ttk.Button(frame, text="Обновить форму", command=self.load_current_farm_data_to_form).grid(row=4, column=0,
                                                                                                   columnspan=2, pady=5)

    def load_current_farm_data_to_form(self):
        farm_data = db.get_farm_by_id(
            self.current_farm_id)
        if farm_data:
            self.farm_edit_vars['name'].set(farm_data.get('name', ''))
            self.farm_edit_vars['address'].set(farm_data.get('address', ''))
            ac = farm_data.get('asset_cost')
            self.farm_edit_vars['asset_cost'].set(str(ac) if ac is not None else '')
        else:
            messagebox.showerror("Ошибка", f"Не удалось загрузить данные для фермы ID: {self.current_farm_id}")

    def save_current_farm_details(self):
        name = self.farm_edit_vars['name'].get().strip()
        address = self.farm_edit_vars['address'].get().strip()
        asset_cost_str = self.farm_edit_vars['asset_cost'].get().strip()
        try:
            asset_cost = float(asset_cost_str) if asset_cost_str else None
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Стоимость активов должна быть числом.")
            return
        if not name:  # Имя не должно быть пустым
            messagebox.showerror("Ошибка ввода", "Название фермы не может быть пустым.")
            return

        if db.update_farm_details(self.current_farm_id, name, address, asset_cost):
            messagebox.showinfo("Успех", "Данные фермы обновлены.")
        else:
            messagebox.showerror("Ошибка БД", f"Не удалось обновить данные фермы ID {self.current_farm_id}.")

    # ----------------------------
    # CRUD для вкладки "Продукты"
    # ----------------------------
    def create_product_widgets(self, parent_tab):
        self.product_vars = {
            'category': tk.StringVar(), 'price': tk.StringVar(), 'volume': tk.StringVar(),
            'supplier_id': tk.StringVar(), 'advertiser_id': tk.StringVar(), 'market_id': tk.StringVar(),
            'distributor_id': tk.StringVar(), 'barn_id': tk.StringVar(), 'livestock_id': tk.StringVar(),
            'field_id': tk.StringVar()
        }

        input_frame = ttk.LabelFrame(parent_tab, text="Данные Продукта")
        input_frame.pack(padx=10, pady=5, fill="x")

        product_fields_labels = {
            'category': "Категория:", 'price': "Цена:", 'volume': "Объем:",
            'supplier_id': "ID Поставщика:", 'advertiser_id': "ID Рекламодателя:",
            'market_id': "ID Рынка:", 'distributor_id': "ID Дистрибьютора:",
            'barn_id': "ID Амбара:", 'livestock_id': "ID Скота:", 'field_id': "ID Поля:"
        }
        row_idx = 0
        col_idx = 0
        for key, label_text in product_fields_labels.items():
            ttk.Label(input_frame, text=label_text).grid(row=row_idx, column=col_idx, sticky="w", padx=5, pady=2)
            ttk.Entry(input_frame, textvariable=self.product_vars[key], width=25).grid(row=row_idx, column=col_idx + 1,
                                                                                       sticky="ew", padx=5, pady=2)
            col_idx += 2
            if col_idx >= 4:  # Переход на новую строку после 2х пар Label-Entry
                col_idx = 0
                row_idx += 1

        # Кнопки
        button_frame = ttk.Frame(input_frame)
        button_frame.grid(row=row_idx + 1, column=0, columnspan=4, pady=10)
        self.add_product_btn = ttk.Button(button_frame, text="Добавить", command=self.add_product_gui)
        self.add_product_btn.pack(side=tk.LEFT, padx=5)
        self.update_product_btn = ttk.Button(button_frame, text="Обновить", command=self.update_product_gui,
                                             state=tk.DISABLED)
        self.update_product_btn.pack(side=tk.LEFT, padx=5)
        self.delete_product_btn = ttk.Button(button_frame, text="Удалить", command=self.delete_product_gui,
                                             state=tk.DISABLED)
        self.delete_product_btn.pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Очистить", command=self.clear_product_fields).pack(side=tk.LEFT, padx=5)

        # Treeview для списка продуктов
        tree_frame = ttk.LabelFrame(parent_tab, text="Список Продуктов")
        tree_frame.pack(padx=10, pady=5, fill="both", expand=True)

        # Колонки в том порядке, в котором они будут в values кортеже
        self.product_tree_columns = ("id", "category", "price", "volume", "supplier_id", "advertiser_id",
                                     "market_id", "distributor_id", "barn_id", "livestock_id", "field_id")
        self.product_tree = ttk.Treeview(tree_frame, columns=self.product_tree_columns, show="headings")

        for col in self.product_tree_columns:
            self.product_tree.heading(col, text=col.replace("_id", " ID").replace("_", " ").title())
            self.product_tree.column(col, width=70 if "_id" in col or col == "id" else 120,
                                     anchor=tk.W if col == "category" else tk.CENTER)

        prod_scroll_y = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.product_tree.yview)
        self.product_tree.configure(yscroll=prod_scroll_y.set)
        prod_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        prod_scroll_x = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL, command=self.product_tree.xview)
        self.product_tree.configure(xscroll=prod_scroll_x.set)
        prod_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.product_tree.pack(fill="both", expand=True)
        self.product_tree.bind("<<TreeviewSelect>>", self.on_product_tree_select)

    def load_products_data(self):
        for item in self.product_tree.get_children():
            self.product_tree.delete(item)
        products = db.get_all_products_for_farm(self.current_farm_id)
        for p_dict in products:
            # Собираем значения в порядке колонок Treeview
            values = [p_dict.get(col_name, '') for col_name in self.product_tree_columns]
            self.product_tree.insert("", tk.END, values=tuple(values))

    def clear_product_fields(self):
        for key in self.product_vars:
            self.product_vars[key].set("")
        self.selected_product_id = None
        self.add_product_btn.config(state=tk.NORMAL)
        self.update_product_btn.config(state=tk.DISABLED)
        self.delete_product_btn.config(state=tk.DISABLED)
        if self.product_tree.selection():
            self.product_tree.selection_remove(self.product_tree.selection()[0])

    def on_product_tree_select(self, event):
        selected_items = self.product_tree.selection()
        if not selected_items: return

        values_tuple = self.product_tree.item(selected_items[0], "values")
        if values_tuple:
            self.selected_product_id = values_tuple[0]  # id
            # Заполняем StringVar из product_vars, сопоставляя с product_tree_columns
            for i, col_name in enumerate(self.product_tree_columns):
                if col_name != 'id' and col_name in self.product_vars:  # id не в форме
                    self.product_vars[col_name].set(str(values_tuple[i]) if values_tuple[i] is not None else "")

            self.add_product_btn.config(state=tk.DISABLED)
            self.update_product_btn.config(state=tk.NORMAL)
            self.delete_product_btn.config(state=tk.NORMAL)

    def _collect_product_data_from_form(self):
        data = {}
        try:
            for key, var in self.product_vars.items():
                value_str = var.get().strip()
                if "_id" in key:  # Поля внешних ключей
                    data[key] = int(value_str) if value_str else None
                elif key in ['price', 'volume']:  # Числовые поля
                    data[key] = float(value_str) if value_str else None
                else:  # Текстовые поля
                    data[key] = value_str if value_str else None

            if not data.get('category'):  # Обязательное поле
                messagebox.showerror("Ошибка ввода", "Категория продукта не может быть пустой.")
                return None
            return data
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Проверьте числовые поля (Цена, Объем, ID).")
            return None

    def add_product_gui(self):
        product_data = self._collect_product_data_from_form()
        if product_data is None: return

        # farm_id будет добавлен функцией create_product по умолчанию
        new_id = db.create_product(**product_data, farm_id=self.current_farm_id)
        if new_id:
            messagebox.showinfo("Успех", f"Продукт '{product_data.get('category')}' добавлен с ID: {new_id}.")
            self.load_products_data()
            self.clear_product_fields()
        else:
            messagebox.showerror("Ошибка БД", "Не удалось добавить продукт.")

    def update_product_gui(self):
        if self.selected_product_id is None:
            messagebox.showwarning("Внимание", "Выберите продукт для обновления.")
            return
        product_data = self._collect_product_data_from_form()
        if product_data is None: return

        if db.update_product(self.selected_product_id, **product_data, farm_id=self.current_farm_id):
            messagebox.showinfo("Успех", f"Продукт ID {self.selected_product_id} обновлен.")
            self.load_products_data()
            self.clear_product_fields()
        else:
            messagebox.showerror("Ошибка БД", f"Не удалось обновить продукт ID {self.selected_product_id}.")

    def delete_product_gui(self):
        if self.selected_product_id is None:
            messagebox.showwarning("Внимание", "Выберите продукт для удаления.")
            return

        category_to_delete = self.product_vars['category'].get()
        if messagebox.askyesno("Подтверждение",
                               f"Удалить продукт '{category_to_delete}' (ID: {self.selected_product_id})?"):
            if db.delete_product(self.selected_product_id):
                messagebox.showinfo("Успех", "Продукт удален.")
                self.load_products_data()
                self.clear_product_fields()
            else:
                messagebox.showerror("Ошибка БД", "Не удалось удалить продукт.")

    # -------------------------------------------------------------------
    # ЗАГОТОВКИ для других вкладок (Advertiser, Barn, Farmer, Field)
    # Вам нужно будет реализовать их по аналогии с Product
    # -------------------------------------------------------------------

    def create_advertiser_widgets(self, parent_tab):
        # TODO: Создать поля ввода (self.advertiser_vars), кнопки и Treeview (self.advertiser_tree)
        ttk.Label(parent_tab, text="CRUD для Рекламодателей будет здесь").pack(padx=20, pady=20)
        pass

    def load_advertisers_data(self):
        # TODO: Вызвать db.get_all_advertisers() и заполнить self.advertiser_tree
        pass

    def clear_advertiser_fields(self):
        pass

    def on_advertiser_tree_select(self, event):
        pass

    def _collect_advertiser_data_from_form(self):
        pass  # return data_dict or None

    def add_advertiser_gui(self):
        pass

    def update_advertiser_gui(self):
        pass

    def delete_advertiser_gui(self):
        pass

    def create_barn_widgets(self, parent_tab):
        ttk.Label(parent_tab, text="CRUD для Амбаров будет здесь").pack(padx=20, pady=20)
        pass

    def load_barns_data(self):
        pass

    def clear_barn_fields(self):
        pass

    def on_barn_tree_select(self, event):
        pass

    def _collect_barn_data_from_form(self):
        pass

    def add_barn_gui(self):
        pass

    def update_barn_gui(self):
        pass

    def delete_barn_gui(self):
        pass

    def create_farmer_widgets(self, parent_tab):
        ttk.Label(parent_tab, text="CRUD для Фермеров будет здесь").pack(padx=20, pady=20)
        pass

    def load_farmers_data(self):
        pass

    def clear_farmer_fields(self):
        pass

    def on_farmer_tree_select(self, event):
        pass

    def _collect_farmer_data_from_form(self):
        pass

    def add_farmer_gui(self):
        pass

    def update_farmer_gui(self):
        pass

    def delete_farmer_gui(self):
        pass

    def create_field_widgets(self, parent_tab):
        ttk.Label(parent_tab, text="CRUD для Полей (земли) будет здесь").pack(padx=20, pady=20)
        pass

    def load_fields_data(self):
        pass

    def clear_field_fields(self):
        pass

    def on_field_tree_select(self, event):
        pass

    def _collect_field_data_from_form(self):
        pass

    def add_field_gui(self):
        pass

    def update_field_gui(self):
        pass

    def delete_field_gui(self):
        pass


if __name__ == "__main__":
    main_window = tk.Tk()
    app = FarmApp(main_window)
    main_window.mainloop()