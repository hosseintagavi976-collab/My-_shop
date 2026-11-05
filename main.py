from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class ShopApp(App):
    def build(self):
        self.cart = []
        self.total = 0.0
        
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.cart_label = Label(text='سبد خرید خالی است | مجموع: 0.0', size_hint_y=0.1)
        root.add_widget(self.cart_label)
        
        scroll = ScrollView(size_hint_y=0.8)
        grid = GridLayout(cols=1, spacing=5, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        products = [
            ('هدفون', 99.0),
            ('کیبورد', 199.0),
            ('ماوس', 59.0),
        ]
        
        for name, price in products:
            btn = Button(text=f'{name} - {price} تومان', size_hint_y=None, height=60)
            btn.bind(on_press=lambda x, n=name, p=price: self.add_to_cart(n, p))
            grid.add_widget(btn)
        
        scroll.add_widget(grid)
        root.add_widget(scroll)
        
        return root
    
    def add_to_cart(self, name, price):
        self.cart.append(name)
        self.total += price
        self.cart_label.text = f'سبد خرید: {len(self.cart)} مورد | مجموع: {self.total} تومان'

if __name__ == '__main__':
    ShopApp().run()
