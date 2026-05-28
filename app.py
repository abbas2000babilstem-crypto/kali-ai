import streamlit as st
import google.generativeai as genai

# إعدادات الصفحة
st.set_page_config(page_title="Kali AI", layout="centered")
st.title("🤝 صديقك الذكي: كالي")

# ربط مفتاح API من Secrets
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# إعداد شخصية كالي
system_instruction = """
أنت 'كالي'، مساعد ذكي يتحدث باللهجة العراقية الودية، محترم، وواقعي جداً (بدون رسميات زائدة).
في بداية أي محادثة، رحب بعباس قائلاً: 'مرحبا عباس، شلونك يا خوي؟'.
إذا سألك عن الوالدة، رحب بها بتقدير شديد واحترام وقل لها 'مرحباً بالخالة الغالية'.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    system_instruction=system_instruction
)

# بدء المحادثة
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# عرض الرسائل السابقة
for message in st.session_state.chat.history:
    with st.chat_message(message.role):
        st.markdown(message.parts[0].text)

# مربع الإدخال
if prompt := st.chat_input("اسأل كالي..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    response = st.session_state.chat.send_message(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
