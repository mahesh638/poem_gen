import os
os.environ['OPENAI_API_KEY'] = #Enter key

from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.chains import SequentialChain

def peom_gen(mood):
    
    llm = OpenAI(temperature = 0.69)
    prompting_1 = PromptTemplate( 
        input_variables = ['mood'],
        template = 'Give me a name of a title you might use to write poem which depicts {mood}'
        )
    mood_chain = LLMChain(llm = llm , prompt = prompting_1, output_key = 'name')

    prompting_2 = PromptTemplate( 
        input_variables = ['name'],
        template = 'Write a peom titled {name}. Give me only the poem without the title. DO NOT PRINT THE TITLE'
        )
    poem_chain = LLMChain(llm = llm, prompt = prompting_2, output_key = 'poem')
    
    chain = SequentialChain(chains = [mood_chain, poem_chain],
                            input_variables = ['mood'],
                            output_variables = ['name', 'poem'])
    out = chain({'mood': mood})
    
    return(out['name'], out['poem'])
