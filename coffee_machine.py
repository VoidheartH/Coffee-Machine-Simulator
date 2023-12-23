from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QFileDialog
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtCore, QtGui


# Ingredient class (used to add new ingredients or remove old ones)
class Ingredient:
    def __init__(self, name):
        self.name = name

# Recipe class (used to give drinks their name ingredient list and description)
class Recipe:
    def __init__(self, name, ingredients, description):
        self.name = name
        self.ingredients = ingredients
        self.description = description

class CoffeeMachineApp(QWidget): # Inheriting QWidget class to use it in CoffeeMachineApp 
    def __init__(self):
        super().__init__()

        self.ingredients = [Ingredient("Coffee"), Ingredient("Green Tea"), Ingredient("Tea"), Ingredient("Chocolate"),
                            Ingredient("Milk"), Ingredient("Ginger"), Ingredient("Mint"), Ingredient("Lemon"), Ingredient("Honey"),
                            Ingredient("Cinnamon")]
        self.current_recipe = []

        # Displaying logo
        self.image = QPixmap("logo.png")
        self.logo = QLabel()
        self.logo.setPixmap(self.image)

        self.label = QLabel("Please choose 3 ingredients to brew a drink")
        self.label.setStyleSheet("font-size: 16px; font-style: italic;")

        self.result_label = QLabel("")

        # Display labels for selected ingredients
        self.base_label = QLabel("Base:")
        self.primary_label = QLabel("Primary:")
        self.secondary_label = QLabel("Secondary:")

        # Defining drink recipes based on the Recipe class
        self.recipes = [
                # Coffee Drinks
                Recipe("Black Magic", ["Coffee", "Mint", "Honey"], "Sweet, cool, and magically wakes you up"),
                Recipe("Caffe Latte", ["Coffee", "Milk", "Milk"], "A caffeine boost dominated by milk"),
                Recipe("Cappuccino", ["Coffee", "Coffee", "Milk"], "Italian delight"),
                Recipe("Espresso", ["Coffee", "Coffee", "Coffee"], "Blacker than a moonless night, hotter and more bitter than hell itself"),
                Recipe("Gingerbread Coffee", ["Coffee", "Ginger", "Cinnamon"], "Sweetened with brown sugar to satisfy the cookie monster"),
                Recipe("Ginger Latte", ["Coffee", "Ginger", "Milk"], "Warm energy boost, perfect for a cold evening"),
                Recipe("Jahe Tubruk", ["Coffee", "Coffee", "Ginger"], "Ginger presides over the ground coffee at the bottom of the cup"),
                Recipe("Sugar and Spice", ["Coffee", "Honey", "Cinnamon"], "Spicy, sweet, and natural bliss in a cup"),

                # Tea Drinks
                Recipe("Gala Had", ["Tea", "Milk", "Ginger"], "Ginger chai latte, good to calm yet warm your nerve"),
                Recipe("Masala Chai", ["Tea", "Ginger", "Cinnamon"], "Spiced tea from Southern Asia"),
                Recipe("Midsummer Night's Dream", ["Tea", "Lemon", "Honey"], "Sweet and memorable, like summertime blues"),
                Recipe("Russian Tea", ["Tea", "Lemon", "Cinnamon"], "Despite the name, it's a totally American drink"),
                Recipe("Shai Adeni", ["Tea", "Milk", "Cinnamon"], "Sweet spicy chai latte from the town of Aden, Yemen"),
                Recipe("Teh Tarik", ["Tea", "Tea", "Milk"], "Tea with milk, mixed by pouring the two repeatedly between cups"),
                Recipe("Cough Syrup", ["Green Tea", "Lemon", "Honey"], "A cure for a sore throat"),
                Recipe("Green Tea Latte", ["Green Tea", "Milk", "Milk"], "Both sweet and savory, with a hint of bitterness for the heart"),
                Recipe("Marrakech", ["Green Tea", "Mint", "Mint"], "Fresh and healthy drink from Morocco"),
                Recipe("Shin Genmaicha", ["Green Tea", "Green Tea", "Cinnamon"], "A variation of the Japanese brew, mixing the brown rice with ginger"),
                Recipe("The Grinch", ["Green Tea", "Ginger", "Cinnamon"], "Green, spicy, and not everyone's cup of tea"),

                # Chocolate Drinks
                Recipe("Bitter Heart", ["Chocolate", "Ginger", "Cinnamon"], "Shadows that will help you try to hide"),
                Recipe("Chocobee Miruku", ["Chocolate", "Honey", "Milk"], "Sweet, nourishing, healthy, chocolate"),
                Recipe("Dark Chocolate", ["Chocolate", "Chocolate", "Chocolate"], "A warm and calming darkness"),
                Recipe("Spanish Sahara", ["Chocolate", "Milk", "Ginger"], "Warm and cozy, just like a day in Barcelona"),
                Recipe("Spiced Lady", ["Chocolate", "Milk", "Cinnamon"], "A British chocolate drink, extremely popular in the 90s"),

                # Milk Drinks
                Recipe("Bedchamber", ["Milk", "Cinnamon", "Honey"], "A cup for those longing for a deep slumber"),
                Recipe("Honey Milk", ["Milk", "Honey", "Milk"], "A cup of milk and honey"),
                Recipe("Le Menthol", ["Milk", "Mint", "Lemon"], "Sour and cool, with a hint of home"),
                Recipe("Lemony Snippet", ["Milk", "Honey", "Lemon"], "A fortunate tale in a cup"),
                Recipe("Milky Way", ["Milk", "Honey", "Mint"], "Sweet and cool, like outer space"),
                Recipe("STMJ", ["Milk", "Ginger", "Honey"], "Warm booster made of susu -milk-, telur -egg-, madu -honey-, and jahe -ginger- from Indonesia"),

        ]

        self.buttons = []
        for ingredient in self.ingredients:
            button = QPushButton(ingredient.name, self)
            button.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # Making the cursor change upon hovering over the buttons
            button.setStyleSheet("*{border: 2px solid '#6a0d8f';"
                                  "border-radius: 15px;"
                                  "font-size: 14px;"
                                  "padding: 5px 0;}"
                                  "*:hover{background: '#6a0d8f';}") 
            button.clicked.connect(lambda state, i=ingredient: self.add_ingredient(i))
            self.buttons.append(button)

        self.brew_button = QPushButton("Brew", self)
        self.brew_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.brew_button.setStyleSheet("*{border: 2px solid '#0a020d';"
                                       "border-radius: 10px;"
                                       "font-size: 16px;"
                                       "margin: 40px 0px;"
                                       "font-weight: bold;"
                                       "color: white;"
                                       "padding: 15px 0px;}"
                                       "*:hover{background: '#0a020d';}") 
        self.brew_button.clicked.connect(self.make_drink) # Brew button uses the make_drink function to make drinks

        self.reset_button = QPushButton("Reset", self)
        self.reset_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.reset_button.setStyleSheet("*{border: 2px solid '#0a020d';"
                                        "border-radius: 15px;"
                                        "font-size: 14px;"
                                        "font-weight: bold;"
                                        "color: white;"
                                        "padding: 5px 0;}"
                                        "*:hover{background: '#0a020d';}") 
        self.reset_button.clicked.connect(self.reset_machine) # Reset button uses the reset_machine function to clear texts

        
        
        

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.logo)
        layout.addWidget(self.label)

        # Horizontal layout for labels and result
        labels_layout = QVBoxLayout()
        labels_layout.addWidget(self.base_label)
        self.base_label.setStyleSheet("font-size: 16px; font-family: Verdana; font-weight: bold;")
        labels_layout.addWidget(self.primary_label)
        self.primary_label.setStyleSheet("font-size: 15px; font-family: Verdana; font-weight: bold;")
        labels_layout.addWidget(self.secondary_label)
        self.secondary_label.setStyleSheet("font-size: 15px; font-family: Verdana; font-weight: bold;")

        layout.addLayout(labels_layout)

        # Grid layout for buttons with three columns
        buttons_layout = QGridLayout()
        row, col = 0, 0
        for button in self.buttons:
            buttons_layout.addWidget(button, row, col)
            col += 1
            if col == 3:
                col = 0
                row += 1

        # Add Brew button in the same row but different column
        buttons_layout.addWidget(self.brew_button, row + 1, 0, 1, 1) # Span the reset brew across two columns
        buttons_layout.addWidget(self.reset_button, row + 1, 1, 1, 1)  
        
        layout.addLayout(buttons_layout)

        layout.addWidget(self.result_label)

        self.setLayout(layout)

        # Flags to manage button states
        self.brew_clicked = False
        self.ingredients_chosen = False

    def add_ingredient(self, ingredient):
        if not self.brew_clicked:
            if len(self.current_recipe) == 0:
                self.base_label.setText(f"Base: {ingredient.name}")
            elif len(self.current_recipe) == 1:
                self.primary_label.setText(f"Primary: {ingredient.name}")
            elif len(self.current_recipe) == 2:
                self.secondary_label.setText(f"Secondary: {ingredient.name}")

            self.current_recipe.append(ingredient)
            if len(self.current_recipe) == 3:
                self.ingredients_chosen = True

    # Reseting the texts and buttons
    def reset_machine(self):
        # Reset labels and flags
        self.result_label.setText("")
        self.base_label.setText("Base:")
        self.primary_label.setText("Primary:")
        self.secondary_label.setText("Secondary:")
        self.current_recipe = []

        # Reset button flags
        self.brew_clicked = False
        self.ingredients_chosen = False

    def make_drink(self):
        for recipe in self.recipes:
            if recipe.ingredients == [ingredient.name for ingredient in self.current_recipe]:
                self.result_label.setText(f"Enjoy your {recipe.name}!\nDescription: {recipe.description}")
                self.result_label.setStyleSheet("font-size: 14px; font-family: Lucida Handwriting;")
                break
        else:
            self.result_label.setText("Invalid combination. Try again.")

        self.current_recipe = []

   

if __name__ == "__main__": # Check if this is the main app and not called from somewhere else
    app = QApplication([])
    window = CoffeeMachineApp()
    window.setWindowTitle("Coffee Machine")
    #window.setFixedSize(600, 400) # Breaks the description fullness
    window.setStyleSheet("background: #964338;") # Used to set a background color to the app
    
    window.show()
    app.exec_()
