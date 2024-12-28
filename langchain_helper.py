from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate

##
ollama = Ollama(base_url="http://localhost:11434", model="llama3.2:1b")


def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="Suggest a fancy name for a {cuisine} restaurant."
    )

    name_chain = LLMChain(llm=ollama, prompt=prompt_template_name, output_key='restaurant_name')

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest 3 popular dishes for {restaurant_name}."
    )

    food_items_chain = LLMChain(llm=ollama, prompt=prompt_template_items, output_key='menu_items')

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    # Fixing the indentation here
    response = chain({'cuisine': cuisine})

    return response
