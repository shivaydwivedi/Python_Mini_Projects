# Mad Libs Generator

def mad_libs():
    print("Welcome to the Mad Libs Generator!")

    # Ask the user for inputs
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")
    place = input("Enter a place: ")

    # Pre-written story with placeholders
    story = f"""
    Once upon a time in a {adjective} {place}, there was a {noun} that loved to {verb} {adverb}.
    Everyone in the town admired the {noun} because of its unique way of {verb}ing.
    It truly was a sight to behold in the {place}!
    """

    # Display the generated Mad Libs story
    print("\nHere is your Mad Libs story:\n")
    print(story)

# Run the Mad Libs Generator
if __name__ == "__main__":
    mad_libs()
