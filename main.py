from chatbot.standard_chatbot import chatbot_response
from agent.agent import AIAgent


print("=== STANDARD CHATBOT ===")
print(chatbot_response("Analyze inventory"))

print("\n=== AI AGENT ===")
agent = AIAgent("Find risky SKUs and create warning report")
final_result = agent.run()

print("\nReport generated successfully.")
