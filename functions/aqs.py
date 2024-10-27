from groq import Groq

# function to get AI answer 
def ai_query(transcript):

    # defining the Groq API key for the client 
    client = Groq(
        api_key="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"
    )

    # setting up the role of the client and passing the question
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": transcript,
            }
        ],
        # What LLM is used should be defined here, I am using mixtral
        model="mixtral-8x7b-32768",
    )
    
    return chat_completion.choices[0].message.content