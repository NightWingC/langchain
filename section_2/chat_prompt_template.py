from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un traductor del español al inglés muy preciso."),
    ("human", "{text}")
])

message = chat_prompt.format_messages(text = "Hola mundo ¿cómo estás?")
for msg in message:
    print(f"{type(msg)}: {msg.content}")