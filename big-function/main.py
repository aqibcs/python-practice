# Check if a person is considered an adult based on age and possession of an ID.
def is_an_adult(age: int, has_id: bool) -> bool:
    return age >= 21 and has_id


# Determine if the given name is "Bob" (case-insensitive).
def is_bob(name: str) -> bool:
    return name.lower() == 'bob'


# Decide if a person can enter the club based on their name, age, and ID status.
def enter_club(name: str, age: int, has_id: bool) -> None:
    if is_bob(name):
        print('Get out of here Bob, we don\'t want no trouble')
        return

    # Check if the person meets the age and ID requirements to enter the club.
    if is_an_adult(age, has_id):
        print('You may enter the club.')
    else:
        print('You may not enter the club.')


# Main function to test the club entry logic with different people.
def main() -> None:
    enter_club('Bob', 29, has_id=True)
    enter_club('James', 29, has_id=True)
    enter_club('Sandra', 27, has_id=False)
    enter_club('Mario', 20, has_id=True)


# Entry point of the script.
if __name__ == '__main__':
    main()
