
# Jerrod Bolton

# Date: Nov 5, 2025
# Python class 235 Programming I - Assignment Input and Output

print("======================================================================")
# this is ust something to add some space before the title of the program.
print("           Welcome to the Movie Review Journal!              ")
print("======================================================================")

def makeNewEntry():
     # This function allows the user to create a new movie review entry.
            
    makeAJournal = input("Would you like to make a new movie review (y/n): ") #Asking the user would they like to make a new movie review. name = input("Please enter your name: ")

    if  makeAJournal.lower() == 'y' or makeAJournal.lower() == 'yes':

        movie_title = input("Enter the movie title: ") # This is the title of the movie being reviewed.
        review = input("Enter your review: ") # This is the user's review of the movie. 
        rating = input("Enter your rating (1-10); 1 being low and 10 being high: ") # This is the user's rating of the movie.
        reviewEntry = input("Would you like to save this review? (yes/no): ") 
        if reviewEntry.lower() == 'yes' or reviewEntry.lower() == 'y':
            print("\nHere is a summary of your review:")
            print(f"Movie Title: {movie_title}")
            print(f"Review: {review}")
            print(f"Rating: {rating}/10")
            confirm = input("Is this information correct? (y/n): ") #This is to confirm the user's review information. Before saving it to the file.
            if confirm.lower() == 'yes' or  confirm.lower() == 'y':
                with open("movie_reviews.txt", "a") as file:
                    file.write("--------------------------------------------------\n")
                    file.write(f"Reviewer: {name}\n")
                    file.write(f"Movie Title: {movie_title}\n")
                    file.write(f"Review: {review}\n")
                    file.write(f"Rating: {rating}/10\n")
                    file.write("--------------------------------------------------\n")
                    print("Your review has been saved to movie_reviews.txt.")
            else:
                print("==============================================================================")
                print("Review not saved. Please restart the program to enter your review again.")
        else:
            print("Okay I see you don't want to save the review. Come back anytime to add a review!")
    else:
        print("======================================================================")
        print("\n    Thank you for using the Movie Review Journal. Goodbye!")
        print("======================================================================")


name = input("Please enter your name: ")

print("======================================================================")
# this is ust something to add some space before the title of the program.
print(f"     Hello, {name}! Let's add a movie review to your journal.") #This greets the user by name. 
print("======================================================================")


      

reviewEntryMade = input("Have you made any review entry before? (y/n): ")
if reviewEntryMade.lower() == 'y' or reviewEntryMade.lower() == 'yes':
    print("======================================================================")
    print("Great! Would you like to view your previous reviews?")
    print("======================================================================")
    view_previous = input("(yes/no): ")
    print("======================================================================")
    if view_previous.lower() == 'y' or view_previous.lower() == 'yes':
        try:
            with open("./movie_reviews.txt", "r") as file:
                print("\nHere are your previous reviews:\n")
                print(file.read())
        except FileNotFoundError:
            print("No previous reviews found.") 
        makeNewEntry()
    else:
        print("No problem! Let's continue.")

elif reviewEntryMade.lower() == 'n' or reviewEntryMade.lower() == 'no':
    makeNewEntry()
            
else:
    changeToSee = input("Alright, See. you later! Wait...! would you like to add a new review? (y/n): ")
    if changeToSee.lower() == 'y' or changeToSee.lower() == 'yes':
            makeNewEntry()
    else:
        print("======================================================================")
        print("\n.        Thank you for using the Movie Review Journal. Goodbye!")
        print("======================================================================")

