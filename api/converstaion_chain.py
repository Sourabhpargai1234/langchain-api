from langchain.chains import ConverstaionChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import(
    chatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)

prompt = chatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(
            "It's a friendly conversation between AI Counsellor and human"
        ),
        MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template("{input}"),
    ]
)

llm=ChatOpenAI(temperature=0)
memory=ConversationBufferMemory(return_messages=True)
conversation=ConversationChain(memory=memory, prompt=prompt, llm=llm)

if __name__=="__main__":
    print(conversation.run(input="Hi there!"))