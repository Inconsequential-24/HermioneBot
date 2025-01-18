
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Use the publicly available LLAMA model
model_name = "meta-llama/Llama-2-7b-chat-hf"  # Publicly available model

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Create a text-generation pipeline
chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

class Memory:
    def __init__(self, memory_limit=5):
        self.memory = []
        self.memory_limit = memory_limit

    def remember(self, user_input, bot_response):
        # Add the current conversation to memory
        self.memory.append((user_input, bot_response))
        # Keep only the last 'memory_limit' exchanges
        if len(self.memory) > self.memory_limit:
            self.memory.pop(0)

    def get_memory(self):
        # Return the memory in a format that the chatbot can use
        return "\n".join([f"User: {user_input}\nHermione: {bot_response}"
                          for user_input, bot_response in self.memory])

class HermioneChatbot:
    def __init__(self):
        self.memory = Memory()  # Initialize memory system

    def get_response(self, user_input):
        # Get recent memory context (conversation history)
        memory_context = self.memory.get_memory()

        # Add the new user input to the conversation context
        prompt = f"{memory_context}\nUser: {user_input}\nHermione:"

        # Generate a response using the LLAMA model
        response = chatbot(prompt, max_length=150)

        # Extract the bot's response (after "Hermione:")
        bot_response = response[0]['generated_text'].split("Hermione:")[-1].strip()

        # Store the conversation in memory
        self.memory.remember(user_input, bot_response)

        return bot_response
