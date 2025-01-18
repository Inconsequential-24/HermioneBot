from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# LLAMA model
model_name = "meta-llama/Llama-2-7b-chat-hf"  

# HFtoken
token = "-----"  

# Load the model and tokenizer 
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=token)
model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=token)

#text-generation pipeline
chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)  # Set device=0 for GPU, if available

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
        memory_context = self.memory.get_memory()

        prompt = f"{memory_context}\nUser: {user_input}\nHermione:"

        response = chatbot(prompt, truncation=False, pad_token_id=tokenizer.eos_token_id, max_length=2048)  
        
        bot_response = response[0]['generated_text'].split("Hermione:")[-1].strip()

        self.memory.remember(user_input, bot_response)

        return bot_response
