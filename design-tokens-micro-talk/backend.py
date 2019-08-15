print("Hi, how are you?")
hi_response = input()

# Make the response lowercase
hi_response_lower = hi_response.lower()

if (hi_response == "well"):
    print("Great!")
else:
    print("Ok.")

############################# Second Question ###############################
print("What are you doing today?")
doing_today_response = input()

# Make the response lowercase
doing_today_response_lower = doing_today_response.lower()

if (doing_today_response == "fishing"):
    print("Great!")
else:
    print("Ok.")

############################# Third Question ###############################
print("What are you doing tomorrow?")
doing_tomorrow_response = input()

if (len(doing_today_response) > 0):
    print("I'm going to be honest. I can't understand a word you said.")
