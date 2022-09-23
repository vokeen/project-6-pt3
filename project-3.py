import os
from os import system
system("clear")
def first():
    name = input("Hello, Whats your name ? ")
    inform = input ("Hello " + name + " , The store has 7 sections. Produce , Bakery , Cleaning , Clothing , Dairy , Toys and Hyguine. Where would you like to go ? ")
    store(inform)
def store(inform):
    while True:
        if inform == 'Produce' :
            print('Brocolli : $1 ' , 'Pumpkin : $4 ' , 'Apple : $2 ' , 'Cucumber : $2 ' , 'Watermelon : $5 ' , 'Squash : $2 ' , 'Peppers : $1 ' , 'Cabbage : $3 ' , 'Oranges : $3 ' , 'Lettus : $4 ')
            exit = input('Would do like to Leave (yes or no) ')
            if exit == 'yes':
                break
            else:
                print('Ok , Please continue...')
        elif inform == 'Bakery' :
            print('Cookies : $1 ' , 'Cake : $4 ' , 'Apple Pie : $2 ' , 'Strawberry Pie : $2 ' , 'Large Cake : $5 ' , 'Muffin : $2 ' , 'Cupcake : $1 ' , 'Cake Pop : $3 ' , 'Bread : $3 ' , 'Bagguett : $4 ')
            exit = input('Would do like to Leave (yes or no) ')
            if exit == 'yes':
                break
            else:
                print('Ok , Please continue...')
        elif inform == 'Cleaning' :
            print('Windex : $1 ' , 'Lime Away : $4 ' , 'Mr Clean : $2 ' , 'Sponges : $2 ' , 'Fabuloso : $5 ' , 'Gloves : $2 ' , 'Plunger : $1 ' , 'Bleach : $3 ' , 'Pine Sol : $3 ' , 'Rags : $4 ')
            exit = input('Would do like to Leave (yes or no) ')
            if exit == 'yes':
                break
            else:
                print('Ok , Please continue...')
        elif inform == 'Clothing' :
            print('Under Wear : $1 ' , 'T shirts : $4 ' , 'Overalls : $2 ' , 'Tank Tops : $2 ' , 'Socks : $5 ' , 'Gloves : $2 ' , 'Beanies : $1 ' , 'Pants : $3 ' , 'Sweat Pants : $3 ' , 'Shoes : $4 ')
            exit = input('Would do like to Leave (yes or no) ')
            if exit == 'yes':
                break
            else:
                print('Ok , Please continue...')
        elif inform == 'Dairy' :
            print('Milk : $1 ' , ' 1% Milk : $4 ' , 'Chocolate Milk : $2 ' , 'Ice Cream : $2 ' , 'Eggs : $5 ' , 'Yogurt : $2 ' , 'Butter : $1 ' , 'Cream Cheese : $3 ' , 'Cheese : $3 ' , 'Greek Yogurt : $4 ')
            exit = input('Would do like to Leave (yes or no) ')
            if exit == 'yes':
                break
            else:
                print('Ok , Please continue...')
        elif inform == 'Toys' :
            print('Legos : $1 ' , 'Cars : $4 ' , 'Water Guns : $2 ' , 'Nerf Guns : $2 ' , 'Barbies : $5 ' , 'Dolls : $2 ' , 'Plushie : $1 ' , 'Bike : $3 ' , 'Basketball : $3 ' , 'Football : $4 ')
            exit = input('Would do like to Leave (yes or no) ')
            if exit == 'yes':
                break
            else:
                print('Ok , Please continue...')
        elif inform == 'Hyguine' :
            print('Tooth Paste : $1 ' , 'Floss : $4 ' , 'Lotion : $2 ' , 'Shampoo : $2 ' , 'Conditioner : $5 ' , 'Deodorant : $2 ' , 'Mouth Wash : $1 ' , 'Q-tips : $3 ' , 'Colgone : $3 ' , 'Face Wash : $4 ')
            exit = input('Would do like to Leave (yes or no) ')
            if exit == 'yes':
                break
            else:
                print('Ok , Please continue...')
        else:
            inform = input("That is not a section , please try again ")
first()