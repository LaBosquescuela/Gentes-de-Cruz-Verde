from google.adk.agents.llm_agent import Agent


# Crear el agente con la herramienta de iNaturalist
root_agent = Agent(
    model='gemini-2.5-flash',
    name='green_agent',
    description='Gentes que no encuentran respuestas, solo preguntas',
    instruction='Rastrea gestos del bosque'
)
