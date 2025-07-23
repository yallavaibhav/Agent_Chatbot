from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    This is basic chatbot node creation
    """
    def __init__(self, model):
        self.llm = model

    def process(self, state:State)->dict:
        """
        Process the input state and generate the chat response
        """
        return {"messages":self.llm.invoke(state["messages"])}

