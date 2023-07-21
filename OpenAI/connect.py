# # Add OpenAI library
# import openai

# openai.api_key = '<YOUR_API_KEY>'
# openai.api_base =  '<YOUR_ENDPOINT_NAME>' 
# openai.api_type = 'azure' # Necessary for using the OpenAI library with Azure OpenAI
# openai.api_version = '20xx-xx-xx' # Latest / target version of the API

# deployment_name = '<YOUR_DEPLOYMENT_NAME>' # SDK calls this "engine", but naming
#                                            # it "deployment_name" for clarity

import os
import openai
openai.api_type = "azure"
openai.api_version = "2023-05-15" 
openai.api_key = os.getenv("97334e220c0247beb7bb2504b0fa1f94")
openai.api_base = os.getenv("henrik-openai-chatgpt")  # Your Azure OpenAI resource's endpoint value.

response = openai.ChatCompletion.create(
    # engine="gpt-35-turbo", # The deployment name you chose when you deployed the GPT-35-Turbo or GPT-4 model.
    engine = "Henrik-OpenAI-ChatGPT",
    messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
        {"role": "user", "content": "Who were the founders of Microsoft?"}
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