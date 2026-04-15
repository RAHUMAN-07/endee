import aiml

# Create kernel
kernel = aiml.Kernel()

# Load startup file
kernel.learn("std-startup.xml")
kernel.respond("LOAD AIML B")

print("Weather Bot is running! (type 'bye' to exit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break
    
    response = kernel.respond(user_input)
    print("Bot:", response)
