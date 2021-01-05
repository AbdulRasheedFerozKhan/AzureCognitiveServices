#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Provide the Subscription ID of your existing Azure subscription
subscription_id = "565b5c7b-bfbc-4c19-9baa-0557713f1923"

#Provide a name for the Resource Group that will contain Azure ML related services 
resource_group = "codesizzlertext-rg" #"<your-subscription-group-name>"
# Provide the unique name and region for the Azure Machine Learning Workspace that will be created
workspace_name = "codesizzlertext"
workspace_region = "eastus" # eastus2, eastus, westcentralus, southeastasia, australiaeast, westeurope


# In[3]:


import azureml.core
print('azureml.core.VERSION: ', azureml.core.VERSION)

# import the Workspace class and check the azureml SDK version
from azureml.core import Workspace

ws = Workspace.create(
    name = workspace_name,
    subscription_id = subscription_id,
    resource_group = resource_group, 
    location = workspace_region, 
    exist_ok = True)

ws.write_config()
print('Workspace configuration succeeded')


# In[4]:


cat .azureml/config.json


# In[5]:


get_ipython().run_cell_magic('writefile', 'summarizer_service.py', '\nimport re\nimport nltk\nimport unicodedata\nfrom gensim.summarization import summarize, keywords\n\ndef clean_and_parse_document(document):\n    if isinstance(document, str):\n        document = document\n    elif isinstance(document, unicode):\n        return unicodedata.normalize(\'NFKD\', document).encode(\'ascii\', \'ignore\')\n    else:\n        raise ValueError("Document is not string or unicode.")\n    document = document.strip()\n    sentences = nltk.sent_tokenize(document)\n    sentences = [sentence.strip() for sentence in sentences]\n    return sentences\n\ndef summarize_text(text, summary_ratio=None, word_count=30):\n    sentences = clean_and_parse_document(text)\n    cleaned_text = \' \'.join(sentences)\n    summary = summarize(cleaned_text, split=True, ratio=summary_ratio, word_count=word_count)\n    return summary \n\ndef init():  \n    nltk.download(\'all\')\n    return\n\ndef run(input_str):\n    try:\n        return summarize_text(input_str)\n    except Exception as e:\n        return (str(e))')


# In[7]:


from azureml.core import Environment
from azureml.core.environment import CondaDependencies

myenv = Environment(name="myenv")
conda_dep = CondaDependencies()
conda_dep.add_pip_package("gensim")
conda_dep.add_pip_package("nltk")
myenv.python.conda_dependencies=conda_dep


# In[8]:


myenv.register(workspace=ws)


# In[9]:


from azureml.core.model import InferenceConfig
from azureml.core.webservice import AciWebservice

inference_config = InferenceConfig(entry_script='summarizer_service.py', environment=myenv)
aci_config = AciWebservice.deploy_configuration(
    cpu_cores = 1, 
    memory_gb = 1, 
    tags = {'name':'Summarization'}, 
    description = 'Summarizes text.')


# In[10]:


from azureml.core import Model
from azureml.core import Webservice
from azureml.exceptions import WebserviceException

service_name = "summarizer"

# Remove any existing service under the same name.
try:
    Webservice(ws, service_name).delete()
except WebserviceException:
    pass

webservice = Model.deploy(workspace=ws,
                       name=service_name,
                       models=[],
                       inference_config=inference_config,
                       deployment_config=aci_config)
webservice.wait_for_deployment(show_output=True)


# In[11]:


example_document = """
I was driving down El Camino and stopped at a red light.
It was about 3pm in the afternoon.  
The sun was bright and shining just behind the stoplight.
This made it hard to see the lights.
There was a car on my left in the left turn lane.
A few moments later another car, a black sedan pulled up behind me. 
When the left turn light changed green, the black sedan hit me thinking 
that the light had changed for us, but I had not moved because the light 
was still red.
After hitting my car, the black sedan backed up and then sped past me.
I did manage to catch its license plate. 
The license plate of the black sedan was ABC123. 
"""


# In[12]:


result = webservice.run(input_data = example_document)
print(result)


# In[13]:


webservice.scoring_uri


# In[ ]:




