
# target_list = ["socks", "soap", "detergent", "sponges"]

# bi_rite_list = ["butter", "cake", "cookies", "bread"]

# berkeley_bowl_list = ["apples", "oranges", "bananas", "milk"]

# safeway_list = ["oreos", "brownies", "soda"]

shopping_list = {
    "target": ["socks", "soap", "detergent", "sponges"],
    "bi_rite": ["butter", "cake", "cookies", "bread"],
    "berkeley": ["apples", "oranges", "bananas", "milk"],
    "safeway": ["oreos", "brownies", "soda"],
    }

# print shopping_list["target"
# user_input = raw_input("What selection?")


def menu_choice(user_input):
    print user_input
    if user_input == "1":
        print shopping_list
    elif user_input == "2":
        store_selection = raw_input("Which store?").lower()
        print shopping_list[store_selection]
    elif user_input == "3":
        store_input = raw_input("Would you like to add a new shopping list?").lower()
        if store_input == "yes":
            store_name = raw_input("What is the name of the store? ").lower()
            # new_list = %s % store_name
            shopping_list[store_name] = []
            print type(store_name)
        print shopping_list.keys()



menu_choice(raw_input("What selection?"))


#Option 1:

# print shopping_list
# print shopping_list[store_selection]
#would you like to add a new shopping_list
#user says yes
#what store?
#user types in store
#create new empty list
#add empty list into dictionary




#would you like to add to a shopping list?
#user says yes
#which store?
#user inputs store
#what items would you like to add?
#user enters items
#call dictionary
#call list
#add items to list
#print list

list_input = raw_input("Would you like to add an item to your list?").lower()
if list_input == "yes":
    store_input = raw_input("Which store").lower
    new_item = shopping_list[store_input]
