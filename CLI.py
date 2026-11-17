from service.loan_service import LoanService
from utilitys.input_helps import get_non_empty_string, get_int_input, LybraryError
from service.menu_services import MenuService
from repositories.file_loan_repository import FileBaseLoanRepository
from repositories.file_book_repository import FileBaseBookRepository
from repositories.file_member_repository import FileBaseMemberRepository


book_repo = FileBaseBookRepository()
member_repo = FileBaseMemberRepository()
loan_repo = FileBaseLoanRepository()

menuservice = MenuService(book_repository=book_repo,member_repository=member_repo)
loanservice = LoanService(member_repository=member_repo,loan_repository=loan_repo,book_repository=book_repo)

def show_main_menu():
    print(f"""1. List all books
2. Add a book
3. Register a member
4. Borrow a book
5. Return a book
6. List active loans
7. List members
0. Exit""")

def add_a_book():

    book_id = get_non_empty_string("Enter book id : ")
    title = get_non_empty_string("Enter book title : ")
    author = get_non_empty_string("Enter book author's name : ")
    year = get_int_input("Year : ")

    try:
        menuservice.add_a_book(book_id=book_id,title=title,author=author,year=year)
        print("New book created successfully")

    except LybraryError as e:
        print(f"Error : {str(e)}")

def register_a_member():

    member_id = get_non_empty_string("Enter member id here : ")
    member_name = get_non_empty_string("Member name : ")

    try:
        menuservice.register_a_member(member_id=member_id,member_name=member_name)
        print("New member register successfully")
    except LybraryError as e:
        print(f"Error : {e}")

def borrow_a_book():
    menuservice.list_all_books()

    loan_id = get_non_empty_string("Loan ID : ")
    book_id = get_non_empty_string("Book ID : ")
    member_id = get_non_empty_string("Member ID : ")

    try:
        loanservice.borrow_a_book(loan_id=loan_id,book_id=book_id,member_id=member_id)
        print("Successfully borrowed")

    except LybraryError as e:
        print(f"Error : {e}")

def return_a_book():

    loan_id = get_non_empty_string("Loan id : ")

    try:
        loanservice.return_a_book(loan_id=loan_id)
        print("Book return successfully.")

    except LybraryError as e:
        print(f"Error : {e}")

while True:
    print("================================ MAIN MENU =====================================")
    show_main_menu()
    user_choice = get_int_input("Enter your choice here : ",minimum=0,maximum=7)

    match user_choice:
        case 1:
            print("================================ ALL BOOKS =====================================")
            menuservice.list_all_books()

        case 2:
            print("================================ ADD A NEW BOOK =====================================")
            add_a_book()

        case 3:
            print("================================ REGISTER A NEW MEMBER =====================================")
            register_a_member()

        case 4:
            print("================================ BORROW A BOOK =====================================")
            borrow_a_book()

        case 5:
            print("================================ RETURN A BOOK =====================================")
            return_a_book()

        case 6:
            print("================================ LIST ACTIVE LOANS =====================================")
            loanservice.get_active_loan()

        case 7:
            print("================================ LIST MEMBERS =====================================")
            menuservice.list_members()

        case 0:
            print("Thank you")
            break










