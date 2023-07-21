# Add OpenAI library
import openai
from urllib import parse

openai.api_key = '635ab39507ab4d3290e11157ec2e9f01'
openai.api_base =  'https://derikopenai.openai.azure.com' 
openai.api_type = 'azure' # Necessary for using the OpenAI library with Azure OpenAI
openai.api_version = '2023-05-15' # Latest / target version of the API

engine_name = 'DerikOpenAI' # SDK calls this "engine", but naming
#                                            # it "deployment_name" for clarity
#engine_name="gpt-35-turbo", # The deployment name you chose when you deployed the GPT-35-Turbo or GPT-4 model.
engine_name ="DerikOpenAIModel"

question = "Who were the founders of Microsoft?"

response = openai.ChatCompletion.create(
    
    engine = engine_name,
    
    messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
        {"role": "user", "content": question}
    ]
)

print(response)

print(response['choices'][0]['message']['content'])


# import os
# import openai
# openai.api_type = "azure"
# openai.api_version = "2023-05-15" 
# openai.api_base = os.getenv("OPENAI_API_BASE")  # Your Azure OpenAI resource's endpoint value .
# openai.api_key = os.getenv("OPENAI_API_KEY")

# conversation=[{"role": "system", "content": "You are a helpful assistant."}]

# while True:
#     user_input = input()      
#     conversation.append({"role": "user", "content": user_input})

#     response = openai.ChatCompletion.create(
#         engine="gpt-3.5-turbo", # The deployment name you chose when you deployed the GPT-35-turbo or GPT-4 model.
#         messages=conversation
#     )

#     conversation.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
#     print("\n" + response['choices'][0]['message']['content'] + "\n")