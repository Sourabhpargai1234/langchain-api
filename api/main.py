from langcorn import create_service
import os
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY", "sk-********")

app = create_service(
    "api.llm_chain:chain",
    "api.conversation_chain:conversation"
)