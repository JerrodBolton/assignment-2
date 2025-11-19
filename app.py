
# Name: Jerrod Bolton
# Date: Nov 5, 2025
# Python class 235 Programming I - Assignment Input and Output

# I would like to create a program that allows users to create a movie review journal. 
# In this program, users can input their movie reviews, ratings, and other relevant information. 
# The program will then save this information to a text file for future reference.

print("======================================================================")
# this is ust something to add some space before the title of the program.
print("           Welcome to the Movie Review Journal!                       ")
print("======================================================================")

# This function allows the user to create a new movie review entry.
def makeNewEntry(): # This starts the function to make a new movie review entry.
    #Anytime that I would like to make a new movie review entry I would just call this function. 

    makeAJournal = input("Would you like to make a new movie review (y/n): ") #Asking the user would they like to make a new movie review. name = input("Please enter your name: ")

    if  makeAJournal.lower() == 'y' or makeAJournal.lower() == 'yes':
        # This is asking the user for the movie title, review, and rating.
        movie_title = input("Enter the movie title: ") # This is the title of the movie being reviewed.
        review = input("Enter your review: ") # This is the user's review of the movie. 
        rating = input("Enter your rating (1-10); 1 being low and 10 being high: ") # This is the user's rating of the movie.
        reviewEntry = input("Would you like to save this review? (yes/no): ") 
        # This is asking the user if they would like to save their review to the file. It's a conditional statement
        if reviewEntry.lower() == 'yes' or reviewEntry.lower() == 'y':
            print("\nHere is a summary of your review:") # This prints a summary of the user's review before saving it to the file.
            print(f"Movie Title: {movie_title}") #This prints the movie title.
            print(f"Review: {review}") #This prints the user's review.
            print(f"Rating: {rating}/10") #This prints the user's rating.
            confirm = input("Is this information correct? (y/n): ") #This is to confirm the user's review information. Before saving it to the file.
            if confirm.lower() == 'yes' or  confirm.lower() == 'y': # If the user confirms the information is correct, it will save the review to the file.
                # This opens the file in append mode, so it doesn't overwrite previous reviews.
                # "a" stands for append mode, which allows you to add new content to the end of the file without deleting existing content.
                # if the file does not exist, it will be created.
                # "movie_reviews.txt" is the name of the file where the reviews will be saved. and also the file extension is 
                # .txt which indicates that it is a text file.and also the 
                # file is in the same directory as the Python script.

                with open("movie_reviews.txt", "a") as file: # This opens the file in append mode, so it doesn't overwrite previous reviews.
                    # This writes the review information to the file.write allows you to write a text file in in Python.
                    file.write("--------------------------------------------------\n")
                    file.write(f"Reviewer: {name}\n") #This writes the reviewer's name to the file.
                    file.write(f"Movie Title: {movie_title}\n") #This writes the movie title to the file.
                    file.write(f"Review: {review}\n") #This writes the user's review to the file.
                    file.write(f"Rating: {rating}/10\n") #This writes the user's rating to the file.
                    file.write("--------------------------------------------------\n")
                    print("Your review has been saved to movie_reviews.txt.")
            else:
                print("==============================================================================")
                print("Review not saved. Please restart the program to enter your review again.")
        else:
            print("Okay I see you don't want to save the review. Come back anytime to add a review!")
    # this is just setting up a nice goodbye message for the user. and if a user inputs no to making a new review.
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
    # this is just a fun little message if the user inputs something other than yes or no.
    if changeToSee.lower() == 'y' or changeToSee.lower() == 'yes':
            makeNewEntry()
    else:
        # this is just setting up a nice goodbye message for the user.
        print("======================================================================")
        print("\n.        Thank you for using the Movie Review Journal. Goodbye!")
        print("======================================================================")

