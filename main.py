import random


yes = ["да", "yes", "y", "д", "принял","accept", "ага", "yeah","угу"]


# Продукты
products = ["помои", "один банан"]
# Шансы продуктов
products_weights = [70, 30]
# Является ли продукт хорошим? (True - хороший, False - Плохой)
products_value = [False, True]

lives = 3
live_symbol = "❤"
coins = 0

def load_mod(mod_name):
    with open(f"{mod_name}{'' if mod_name.endswith('.mod') else '.mod'}") as mod:
        exec(mod.read())

        
     
def random_product(product = products, chances= products_weights):
    return random.choices(product, weights=chances)[0]

def menu():
    global lives
    global live_symbol
    global coins
    while True:
        print("""
    1. Магазин
    2. Выгрузить моды
    3. Загрузить мод
    4. Выйти из меню""")
        menu_choice = int(input())
        if menu_choice == 1:
            print("В разработке")

        if menu_choice == 2:
            products = ["помои", "один банан"]
            products_weights = [70, 30]
            products_value = [False, True]
            live_symbol = "❤"
        if menu_choice == 3:
            inp_name = input("Введите название мода")
            load_mod(inp_name)
        if menu_choice == 4:
            main()
    

def main():
    global lives
    global live_symbol
    global coins
    while True:
        print(f"""
        Съешь ли ты случайную еду, она может быть как хорошой так и плохой?
        Жизни: {live_symbol*lives}    Монеты: {coins}
        Напишите m для выхода в меню
        """)

        choice = input("").strip().lower()
        product = random_product()
        if choice == "m":
            menu()
        elif choice in yes:

            if products_value[products.index(product)] == False:
                    lives -= 1
            else:
                    coins += 1
            print("-"*30)
            
            print(f"""
            Ты съел блюдо, и это {'хорошо' if products_value[products.index(product)] else "плохо"}!
            Блюдо, которое ты съел '{product}'
            Жизни: {live_symbol*lives} Монеты: {coins}
            """)
            
        else:
            print(f"""
                    Ты не съел блюдо, и это {'хорошо' if not products_value[products.index(product)] else "плохо"}!
                    Блюдо, которое ты не съел '{product}'
                    Жизни: {live_symbol*lives} Монеты: {coins}
                    """)
                
            




    
if __name__ == "__main__":
    main()