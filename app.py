
# Jerrod Bolton

# Date: Nov 5, 2025
# Python class 235 Programming I - Assignment 2

"""
This program is part of Assignment 2 for Python class 235 Programming I. 
The goal of this assignment is to demonstrate mastery over variables, data types, user input/output, 
and file operations in Python. The program will include functionality to persist data between uses 
by reading from and writing to files. 

Key Features:
- User input and output to interact with the program.
- Use of at least two variables holding different data types.
- Writing data to a text file for persistence.
- Reading data from a text file to retrieve and display information.
- A focus on creating a great user experience.

Possible Themes:
- Time Machine Journal: Users can write journal entries, save them to a file, and read previous entries.
- Movie Review Database: Users can add and retrieve movie reviews.
- RPG Character Keeper: Users can save and load RPG character information.

Requirements:
1. Demonstrate input and output functionality.
2. Use variables with different data types.
3. Implement file read and write operations.
4. Ensure the file operations add meaningful functionality to the application.
5. Include detailed comments throughout the code for clarity.

Optional:
- Use functions to organize the program into reusable components.
"""


print("======================================================================")
# this is ust something to add some space before the title of the program.
print("           Welcome to the Movie Review Journal!                ")
print("======================================================================")

name = input("Please enter your name: ")

print(f"Hello, {name}! Let's add a movie review to your journal.")

movie_title = input("Enter the movie title: ") # This is the title of the movie being reviewed.

review = input("Enter your review: ") # This is the user's review of the movie. 

rating = input("Enter your rating (1-10); 1 being low and 10 being high: ") # This is the user's rating of the movie.

# print a summary of the review give the user a chance to confirm what they texted.

print("\nHere is a summary of your review:")
print(f"Movie Title: {movie_title}")
print(f"Review: {review}")
print(f"Rating: {rating}/10")

confirm = input("Is this information correct? (yes/no): ")
 
if confirm.lower() == 'yes':
    with open("movie_reviews.txt", "a") as file:
        file.write("--------------------------------------------------\n")
        file.write(f"Reviewer: {name}\n")
        file.write(f"Movie Title: {movie_title}\n")
        file.write(f"Review: {review}\n")
        file.write(f"Rating: {rating}/10\n")
        file.write("--------------------------------------------------\n")
    print("Your review has been saved to movie_reviews.txt.")
else:
    print("Review not saved. Please restart the program to enter your review again.")
# Option to read previous reviews
print("\nThank you for using the Movie Review Journal. Goodbye!")
