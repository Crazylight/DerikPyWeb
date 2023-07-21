import openai

class  charter:
    
    engine_name = 'DerikOpenAIModel'
    def __init__(self):                
        openai.api_key = '635ab39507ab4d3290e11157ec2e9f01'
        openai.api_base =  'https://derikopenai.openai.azure.com' 
        openai.api_type = 'azure' # Necessary for using the OpenAI library with Azure OpenAI
        openai.api_version = '2023-05-15' # Latest / target version of the API
        
    def chat(self, question):
                       
        response = openai.ChatCompletion.create(
            engine = self.engine_name,        
            messages=[
                {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
                {"role": "user", "content": question}
            ])

        return response['choices'][0]['message']['content']