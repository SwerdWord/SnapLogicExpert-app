import streamlit as st
import requests
import time
import os

# Set environment variables directly in the script
# Streamlit Properties
os.environ["PAGE_TITLE"] = "SnapLogic Agent Creator Demo Catalog"
os.environ["TITLE"] = "Welcome to the SnapLogic Agent Creator Demo Catalog"
# SL Properties
os.environ["SL_TASK_TIMEOUT"] = "90"
## HR Chatbot 
os.environ["HR_PAGE_TITLE"] = "HR Chatbot"
os.environ["HR_TITLE"] = "HR Chatbot"
os.environ["SL_HR_TASK_URL"] = "https://afd77e11a20c840bab10aabe6b8482ee-971464689.eu-west-3.elb.amazonaws.com/api/1/rest/feed-master/queue/ConnectFasterInc/Toni/Toni_GenAI_Chatbot/HR_Chatbot_2_RAG_UltraAPI"
os.environ["SL_HR_TASK_TOKEN"] = "jeSolCStYJxp6CGiDVOpnzdbhM47x9f5"
os.environ["SL_HR_TASK_NAMESPACE"] = "hr-chatbot"
## CRM Chatbot 
os.environ["CRM_PAGE_TITLE"] = "CRM AI Assistant"
os.environ["CRM_TITLE"] = "Query CRM using Natural Language"
os.environ["SL_CRM_TASK_URL"] = "https://a18c9f3a83b3e40a69da924330ab4acd-2111898486.eu-west-3.elb.amazonaws.com/api/1/rest/feed/run/task/ConnectFasterInc/Toni/Toni_GenAI_Chatbot/CRM_AI_Assistant_Task"
os.environ["SL_CRM_TASK_TOKEN"] = "wq5LWVvBWn1tzguHzQsqbsSZoyOYzrG0"
## Deloitte Chatbot 
os.environ["DL_PAGE_TITLE"] = "Deloitte GenAI Dossier Chatbot"
os.environ["DL_TITLE"] = "Deloitte GenAI Dossier Chatbot"
os.environ["SL_DL_TASK_URL"] = "https://afd77e11a20c840bab10aabe6b8482ee-971464689.eu-west-3.elb.amazonaws.com/api/1/rest/feed-master/queue/ConnectFasterInc/Toni/Toni_GenAI_Chatbot/HR_Chatbot_2_RAG_UltraAPI"
os.environ["SL_DL_TASK_TOKEN"] = "jeSolCStYJxp6CGiDVOpnzdbhM47x9f5"
os.environ["SL_DL_TASK_NAMESPACE"] = "deloitte-genai-dossier-chatbot"
## Billing Reconciliation Chatbot
os.environ["CREC_PAGE_TITLE"] = "Billing Reconciliation"
os.environ["CREC_TITLE"] = "Billing reconciliation between PDF Contracts and ERP"
os.environ["SL_CREC_TASK_URL"] = "https://a18c9f3a83b3e40a69da924330ab4acd-2111898486.eu-west-3.elb.amazonaws.com/api/1/rest/feed/run/task/ConnectFasterInc/Toni/Toni_GenAI_Contracts-Reconciliation/Content_Reconciliation_API"
os.environ["SL_CREC_TASK_TOKEN"] = "vktUhPn5qtMfLr4DqfpZW1mS9cNiT0gM"
## Health Insurance Chatbot 
os.environ["UW_PAGE_TITLE"] = "Underwriter assistant"
os.environ["UW_TITLE"] = "Healthcare Chatbot"
os.environ["SL_UW_TASK_URL"] = "https://afd77e11a20c840bab10aabe6b8482ee-971464689.eu-west-3.elb.amazonaws.com/api/1/rest/feed-master/queue/ConnectFasterInc/Toni/Toni_GenAI_InsuranceUnderwriter/T_AskMedicalQuestionsUltra"
os.environ["SL_UW_TASK_TOKEN"] = "2cSISiLe7mNaNTFlgsca5mQxCo8cwTWT"
## Manufacturing
os.environ["GM_PAGE_TITLE"] = "Manufacturing Assistant"
os.environ["GM_TITLE"] = "Manufacturing Spec Assistant"
os.environ["SL_GM_TASK_URL"] = "https://afd77e11a20c840bab10aabe6b8482ee-971464689.eu-west-3.elb.amazonaws.com/api/1/rest/feed-master/queue/ConnectFasterInc/RG/msg/MSG_Ultra%20Task"
os.environ["SL_GM_TASK_TOKEN"] = "s7R0GSJF7AfAayGFrSxHeFC3Tc1tjo3P"
## Dealer Invoices Chatbot 
os.environ["DI_PAGE_TITLE"] = "Dealer Invoices Assistant"
os.environ["DI_TITLE"] = "Dealer Chatbot"
os.environ["SL_DI_TASK_URL"] = "https://emea.snaplogic.com/api/1/rest/slsched/feed/ConnectFasterInc/Nilesh/GenAI/Invoice_Retriever_NP_Task"
os.environ["SL_DI_TASK_TOKEN"] = "JDrwOhJRJ9vtlAEiLli4tgBgUevH5xio"
## SF OAuth Endpoints
os.environ["SF_AUTHORIZE_URL"] = "https://snaplogic.my.salesforce.com/services/oauth2/authorize"
os.environ["SF_TOKEN_URL"] = "https://snaplogic.my.salesforce.com/services/oauth2/token" 
os.environ["SF_REVOKE_TOKEN_URL"] = "https://snaplogic.my.salesforce.com/services/oauth2/revoke"
os.environ["SF_REDIRECT_URI"] = "https://snaplogic-genai-builder.streamlit.app/Sales_Agent"
os.environ["SF_SCOPE"] = "id openid offline_access"
## Blog Post Generator
os.environ["BR_TASK_URL"] = "https://emea.snaplogic.com/api/1/rest/slsched/feed/ConnectFasterInc/snapLogic4snapLogic/BlogWriterAgent/AgentBlogWriterTask"
os.environ["BR_TASK_URL_TOKEN"] = "fY4hcH59Xy7FQbrjXiycPxch6PsmPADw"

# RFP Agent URL and Token
URL = "https://emea.snaplogic.com/api/1/rest/slsched/feed/ConnectFasterInc/snapLogic4snapLogic/AutoRFPAgent/ApiRfpAgent"
BEARER_TOKEN = "nNpLBJrd8FAtFh3TVC9xR97QAwWtJHgF"
timeout = 300

def typewriter(text: str, speed: int):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.markdown(curr_full_text)
        time.sleep(1 / speed)

st.set_page_config(page_title="SnapLogic Expert Assistant")
st.title("SnapLogic Expert Assistant")

st.markdown(""" 
### AI-powered RFP and technical expert assistant with Voice Interface

Get detailed answers to RFP questions and technical inquiries, with information sourced from official documentation,  
Slack discussions, and various other SnapLogic resources. 
""")

# Create columns with adjusted ratios for better widget display
col1, col2 = st.columns([1.2, 1.8])

with col1:
    # Embed ElevenLabs widget with adjusted container
    elevenlabs_html = """
    <div style="min-width: 300px; padding: 10px;">
        <elevenlabs-convai agent-id="nnoWPUe6P27G1OlPw25C" style="width: 100%;"></elevenlabs-convai>
        <script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>
    </div>
    """
    st.components.v1.html(elevenlabs_html, height=200, width=340)

st.markdown(""" 
💡 **Voice Interaction Available**
- Use the voice widget above to speak your questions
- Listen to AI-generated voice responses
- Perfect for hands-free operation

Sample queries:
- What security certifications does SnapLogic maintain?
- Describe SnapLogic's approach to API management
- What is the SnapLogic disaster recovery strategy?
- How does SnapLogic handle data encryption at rest and in transit?
- What monitoring capabilities are available in the platform?
- Explain SnapLogic's integration with identity providers
""")

# Initialize chat history
if "expert_assistant" not in st.session_state:
    st.session_state.expert_assistant = []

# Display chat messages from history
for message in st.session_state.expert_assistant:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
prompt = st.chat_input("Ask me anything about SnapLogic's technical capabilities")
if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.expert_assistant.append({"role": "user", "content": prompt})
    
    with st.spinner("Working..."):
        data = {"prompt": prompt}
        headers = {
            'Authorization': f'Bearer {BEARER_TOKEN}'
        }
        response = requests.post(
            url=URL,
            data=data,
            headers=headers,
            timeout=timeout,
            verify=False
        )
        
        if response.status_code == 200:
            try:
                result = response.json()
                if "response" in result:
                    assistant_response = result["response"]
                    with st.chat_message("assistant"):
                        typewriter(text=assistant_response, speed=30)
                    st.session_state.expert_assistant.append({"role": "assistant", "content": assistant_response})
                else:
                    with st.chat_message("assistant"):
                        st.error("❌ Invalid response format from API")
            except ValueError:
                with st.chat_message("assistant"):
                    st.error("❌ Invalid JSON response from API")
        else:
            st.error(f"❌ Error while calling the SnapLogic API")
        st.rerun()