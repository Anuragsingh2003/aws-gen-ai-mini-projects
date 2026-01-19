from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain_aws import ChatBedrockConverse

#alway refer model list https://aws.amazon.com/bedrock/models/
#https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html
#refer to docs of models aws 
def demo_chatbot(messages):
    demo_llm=ChatBedrockConverse(
    credentials_profile_name="default",
    region_name="us-east-1",  # Change as per your setup
        model="us.deepseek.r1-v1:0",
        temperature=0.1,
        max_tokens=1024,
    )
    return demo_llm.invoke(messages)

messages = [
    {"role": "user", 
     "content": [{"text":"Who won the world series in 2020?"}]
     }
]

response = demo_chatbot(messages)
print(response)