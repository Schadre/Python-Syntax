# Task 2: Your Mood Today Ask the user how they feel today. 
# If they say "happy", print "That's great to hear!", 
# and if they say "sad", print "I hope your day gets better!". 
# Ensure your if statement is properly indented. 
# HINT: Use the input() function to ask the user how they feel! 
# If you need a refresher, check this out here: https://www.w3schools.com/python/python_user_input.asp

emotions = input("How do you feel today? ").lower()

if emotions == "happy":
    print("That's great to hear!")
elif emotions == "sad":
    print("I hope your day gets better!")