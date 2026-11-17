class LybraryError(Exception):
    pass

def get_non_empty_string(prompt):
    while True:
        try:
            value = str(input(prompt)).strip().lower()

            if value:
                return value

            print("input can't be empty")
        except Exception:
            print("Enter valid answer and try again!")

def get_int_input(prompt,minimum:int | None = None,maximum:int | None = None):

    while True:
        try:
            value = int(input(prompt))

            if maximum is not None and value > maximum:
                print(f"input must be less than {maximum}")
                continue

            elif minimum is not None and value < minimum:
                print(f"input must be greater than {minimum}")
                continue

            return value

        except ValueError:
            print("Enter valid integer answer and try again!")

        except Exception as e:
            print(f"Error : {e}")

def get_flot_input(prompt,minimum:int | None = None,maximum:int | None = None):

    while True:
        try:
            value = float(input(prompt))

            if minimum is not None and value < minimum:
                print(f"input must be greater than {minimum}")
                continue

            if maximum is not None and value > maximum:
                print(f"input must be less than {maximum}")
                continue

            return value
        except ValueError:
            print("Enter valid floating answer and try again!")

        except Exception as e:
            print(f"Error : {str(e)}")

def choose_two_options(option_one,option_two):
    while True:
        user_option = input("Enter your option here : ")
        if user_option == option_one:
            return option_one
        elif user_option == option_two:
            return option_two
        else:
            print("invalid user option")








