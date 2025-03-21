def simple_chatbot(user_query):
    # Predefined responses
    if user_query == "What is the total revenue?":
        return "The total revenue is $5,000,000."
    elif user_query == "What are the main expenses?":
        return "The main expenses include salaries, rent, and marketing costs totaling $3,000,000."
    elif user_query == "How has net income changed over the last year?":
        return "The net income has increased by $500,000 over the last year."
    elif user_query == "What is the profit margin?":
        return "The profit margin is 20%."
    elif user_query == "Which quarter was the most profitable?":
        return "The most profitable quarter was Q2 with a profit of $1,200,000."
    else:
        return "Sorry, I can only provide information on predefined queries."

# Main script
if __name__ == "__main__":
    print("Welcome to the Financial Chatbot! Ask a question:")
    while True:
        user_query = input("You: ")
        if user_query.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = simple_chatbot(user_query)
        print(f"Chatbot: {response}")
