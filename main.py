def main():
    to_do_list = list_maker()
    print_list(to_do_list)
    while len(to_do_list) > 0:
        mark_complete(to_do_list)
        print_list(to_do_list)
    

# takes user inputs in order to create the to do list
def list_maker():
    to_do = []
    print('Type h for help or enter q to quit:')
    user_input = input("Type a task: ")
    while user_input != 'q':
        if user_input == 'h':
            print('type q to quit, or enter a task')
        elif user_input == 'q':
            break
        else:
            to_do.append(user_input)
        user_input = input("Type a task: ")
    return to_do

# function for marking tasks off the list
def mark_complete(list):
    user_input = input("Type finished task/task number: ")
    if user_input == 'q':
        return
    try:
        user_input = int(user_input) - 1
        if user_input < len(list):
            index = user_input - 1
            del list[index]
    except:
        user_input = user_input.lower()
        if user_input in list:
            index = list.index(user_input)
            del list[index]
        else:
            print("Task not found")
             

# self explanatory
def print_list(list):
    i = 1
    print()
    print("To do today:")
    for item in list:
        print(f"{i}) {item}")
        i += 1

main()