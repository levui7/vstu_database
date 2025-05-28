import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import database_connector
from database_config import db_farm_id


class FarmApp:
    def __init__(self, root):
        self.root = root
        self.root.title(f"Управление Фермой")
        self.root.geometry("800x600")

        self.current_farm_data = None

        # --- Переменные для ПРОДУКТОВ (пример) ---
        self.product_category_var = tk.StringVar()
        self.product_price_var = tk.StringVar()
        self.product_volume_var = tk.StringVar()
        self.selected_product_id = None

        self.create_widgets()
        self.load_farm_info()  # Загружаем инфо о нашей ферме
        self.load_products_data()  # Загружаем продукты для нашей фермы

    def load_farm_info(self):
        """Загружает и отображает информацию о ЕДИНСТВЕННОЙ ферме."""
        self.current_farm_data = database_connector.get_farm_details()  # Использует SINGLE_FARM_ID по умолчанию
        if self.current_farm_data:
            # Отображаем информацию о ферме где-нибудь в GUI
            # Например, в заголовке вкладки или в специальном LabelFrame
            self.farm_info_label.config(
                text=f"Ферма: {self.current_farm_data.get('name', 'N/A')}\n"
                     f"Адрес: {self.current_farm_data.get('address', 'N/A')}\n"
                     f"Активы: {self.current_farm_data.get('asset_cost', 'N/A')}"
            )
        else:
            self.farm_info_label.config(text="Не удалось загрузить информацию о ферме.")
            messagebox.showerror("Ошибка", f"Не удалось загрузить данные для фермы ID: {db_farm_id}")

    def create_widgets(self):
        # --- Вкладки (Notebook) для разделения интерфейса ---
        self.notebook = ttk.Notebook(self.root)

        # Вкладка для информации о ферме и ее продуктах
        self.farm_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.farm_tab, text='Продукты Фермы')

        # (Опционально) Вкладка для редактирования данных самой фермы, если это нужно
        # self.edit_farm_tab = ttk.Frame(self.notebook)
        # self.notebook.add(self.edit_farm_tab, text='Данные Фермы')

        self.notebook.pack(expand=True, fill='both', padx=5, pady=5)

        # --- Содержимое вкладки "Продукты Фермы" ---
        farm_info_frame = ttk.LabelFrame(self.farm_tab, text="Информация о Ферме")
        farm_info_frame.pack(padx=10, pady=10, fill="x")
        self.farm_info_label = ttk.Label(farm_info_frame, text="Загрузка...", justify=tk.LEFT)
        self.farm_info_label.pack(padx=5, pady=5)

        # Фрейм для полей ввода продукта
        product_input_frame = ttk.LabelFrame(self.farm_tab, text="Данные Продукта")
        product_input_frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(product_input_frame, text="Категория:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.product_category_entry = ttk.Entry(product_input_frame, textvariable=self.product_category_var, width=30)
        self.product_category_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(product_input_frame, text="Цена:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.product_price_entry = ttk.Entry(product_input_frame, textvariable=self.product_price_var, width=30)
        self.product_price_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(product_input_frame, text="Объем:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.product_volume_entry = ttk.Entry(product_input_frame, textvariable=self.product_volume_var, width=30)
        self.product_volume_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Кнопки для продуктов
        product_button_frame = ttk.Frame(product_input_frame)
        product_button_frame.grid(row=3, column=0, columnspan=2, pady=10)

        self.add_product_button = ttk.Button(product_button_frame, text="Добавить продукт",
                                             command=self.add_product_gui)
        self.add_product_button.pack(side=tk.LEFT, padx=5)
        # ... кнопки Update, Delete, Clear для продуктов ...

        # Фрейм для отображения списка продуктов
        product_tree_frame = ttk.LabelFrame(self.farm_tab, text="Список Продуктов Фермы")
        product_tree_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.product_tree = ttk.Treeview(product_tree_frame, columns=("id", "category", "price", "volume"),
                                         show="headings")
        self.product_tree.heading("id", text="ID")
        self.product_tree.heading("category", text="Категория")
        self.product_tree.heading("price", text="Цена")
        self.product_tree.heading("volume", text="Объем")
        # ... настройка колонок ...
        self.product_tree.pack(fill="both", expand=True)  # Добавьте Scrollbar по аналогии с фермами
        self.product_tree.bind("<<TreeviewSelect>>", self.on_product_tree_select)

        # (Опционально) --- Содержимое вкладки "Данные Фермы" ---
        # Если вы хотите редактировать данные самой фермы (название, адрес и т.д.)
        # создайте здесь поля ввода и кнопки для Farm, как в предыдущем примере,
        # но они будут работать только с SINGLE_FARM_ID.
        # self.create_edit_farm_widgets(self.edit_farm_tab)

    def load_products_data(self):
        """Загружает продукты для текущей (единственной) фермы."""
        for item in self.product_tree.get_children():
            self.product_tree.delete(item)

        products = database_connector.get_products_for_farm()  # Использует SINGLE_FARM_ID по умолчанию
        for product in products:
            self.product_tree.insert("", tk.END, values=(
                product['id'],
                product['category'],
                product['price'],
                product.get('volume', '')
            ))

    def clear_product_fields(self):
        self.product_category_var.set("")
        self.product_price_var.set("")
        self.product_volume_var.set("")
        self.selected_product_id = None
        # ... управление состоянием кнопок для продуктов ...

    def on_product_tree_select(self, event):
        """Обработчик выбора продукта в таблице."""
        selected_items = self.product_tree.selection()
        if not selected_items:
            self.clear_product_fields()
            return

        selected_item = selected_items[0]
        product_values = self.product_tree.item(selected_item, "values")

        if product_values:
            self.selected_product_id = product_values[0]
            self.product_category_var.set(product_values[1])
            self.product_price_var.set(str(product_values[2]) if product_values[2] is not None else "")
            self.product_volume_var.set(str(product_values[3]) if product_values[3] is not None else "")
            # ... управление состоянием кнопок для продуктов ...

    def add_product_gui(self):
        category = self.product_category_var.get().strip()
        price_str = self.product_price_var.get().strip()
        volume_str = self.product_volume_var.get().strip()

        if not category:
            messagebox.showerror("Ошибка ввода", "Категория продукта не может быть пустой.")
            return

        try:
            price = float(price_str) if price_str else None
            volume = float(volume_str) if volume_str else None
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Цена и объем должны быть числами.")
            return

        # farm_id не нужен в аргументах, т.к. используется SINGLE_FARM_ID в db_connector
        if database_connector.add_product_to_farm(category, price, volume):
            messagebox.showinfo("Успех", "Продукт успешно добавлен.")
            self.load_products_data()
            self.clear_product_fields()
        else:
            messagebox.showerror("Ошибка БД", "Не удалось добавить продукт.")

    # --- Добавьте методы update_product_gui, delete_product_gui ---
    # --- и, если нужно, методы для редактирования данных самой фермы (create_edit_farm_widgets и ее обработчики) ---


if __name__ == "__main__":
    main_window = tk.Tk()
    app = FarmApp(main_window)
    main_window.mainloop()