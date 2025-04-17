from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2-medium')
set_seed(42)

generator("Hello, I'm a language model,", max_length=30, num_return_sequences=5)
[{'generated_text': "Hello, I'm a language model, I'm a language. I'm a compiler, I'm a parser, I'm a server process. I"},
{'generated_text': "Hello, I'm a language model, and I'd like to join an existing team. What can I do to get started?\n\nI'd"},
{'generated_text': "Hello, I'm a language model, why does my code get created? Can't I just copy it? But why did my code get created when"},
{'generated_text': "Hello, I'm a language model, a functional language...\n\nI'm a functional language. Is it hard? A little, yes. But"},
{'ggenerated_text': "Hello, I'm a language model, not an object model.\n\nIn a nutshell, I need to give me objects from which I can get"}]
   
recent_chats = []
   
print("Please type something to start chatting. Type'exit' to quit chatting")

print("please enter desired max length for chat: ")
  
max_length = int(input(""))
  
print("please enter desired tempeture for chat (0.1 - 1.0): ")
  
temperature = float(input(""))
  
  
while True:
  user_input = input("")
  
  if (user_input.lower() == "exit"):
    print("ending chat now bye bye")
    break

  
  recent_chats.append(user_input)
  recent_chats = recent_chats[-5:]
  chat_prompt = "\n".join(recent_chats) + "\nChatbot:"
  #recent_chats = generator("Hello, I'm a language model,", max_length, num_return_sequences=5)
  # Generate text
  results = generator(
    chat_prompt,
    max_new_tokens=max_length,
    num_return_sequences=5,
    temperature=temperature,
    pad_token_id=50256,
    truncation=True)[0]['generated_text']
    
  answer = results[len(chat_prompt):].strip().split("\n")[0] 
  #generator("Hello, I'm a language model,", max_length, num_return_sequences=5)
  #[{'generated_text': "Hello, I'm a language model, I'm a language. I'm a compiler, I'm a parser, I'm a server process. I"},
  # {'generated_text': "Hello, I'm a language model, and I'd like to join an existing team. What can I do to get started?\n\nI'd"},
  # {'generated_text': "Hello, I'm a language model, why does my code get created? Can't I just copy it? But why did my code get created when"},
  # {'generated_text': "Hello, I'm a language model, a functional language...\n\nI'm a functional language. Is it hard? A little, yes. But"},
   #{'generated_text': "Hello, I'm a language model, not an object model.\n\nIn a nutshell, I need to give me objects from which I can get"}]

  #response = generator("Hello, I'm a language model,", max_length, num_return_sequences=5)
  #for result in results:
  #    print(result['generated_text'])
  
  print("\nChatbot responses:")
  recent_chats.append(f"Chatbot: {answer}")
  #for idx, result in enumerate(results, 1):
    #print(f"{idx}. {result['generated_text'].strip()}\n")
