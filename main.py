def main():
    to_do_list = list_maker()
    print_list(to_do_list)



def list_maker():
    to_do = []
    print('Type h for help, enter q to quit, or enter a task:')
    user_input = input()
    while user_input != 'q':
        if user_input == 'h':
            print('type q to quit, or enter a task')
        elif user_input == 'q':
            break
        else:
            to_do.append(user_input)
        user_input = input("Type a task:")
    return to_do

def print_list(list):
    print()
    print("To do today:")
    for item in list:
        print(item)

main()