import uuid

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from question_answering_agent import question_answering_agent

load_dotenv()


# Create a new session service to store state
session_service_stateful = InMemorySessionService()

initial_state = {
    "user_name": "Hector DeJesus",
    "user_preferences": """
        I enjoy building AI-powered cloud-native applications.
        My favorite cuisine is Puerto Rican food.
        I like exploring trance, techno, and rave music events.
        I follow the latest trends in Google Cloud and AI/ML.
        I like producing and investing in exclusive clubs and discotheques.
        My favorite tool for coding is VSCode.
        I love working on Terraform and Infrastructure as Code projects.
        I enjoy teaching complex cloud and AI concepts in simple ways.
        I like playing with new SaaS ideas to generate online income.
        My favorite TV shows are sci-fi and fantasy, especially ones with deep storylines.
        I enjoy fitness through activities like intermittent fasting and exploring health hacks.
        I appreciate when people support my entrepreneurial projects like Develom.com.    
    """,
}

# Create a NEW session
APP_NAME = "Hector's Bot"
USER_ID = "hector_dejesus"
SESSION_ID = str(uuid.uuid4())
stateful_session = session_service_stateful.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
)
print("CREATED NEW SESSION:")
print(f"\tSession ID: {SESSION_ID}")

runner = Runner(
    agent=question_answering_agent,
    app_name=APP_NAME,
    session_service=session_service_stateful,
)

new_message = types.Content(
    role="user", parts=[types.Part(text="What is Hector's favorite food?")]
)

for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,
):
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"Final Response: {event.content.parts[0].text}")

print("==== Session Event Exploration ====")
session = session_service_stateful.get_session(
    app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
)

# Log final Session state
print("=== Final Session State ===")
for key, value in session.state.items():
    print(f"{key}: {value}")
