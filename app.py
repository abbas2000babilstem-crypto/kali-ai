import streamlit as st
import google.generativeai as genai

# إعداد الصفحة
st.set_page_config(
    page_title="Kali AI",
    page_icon="🤝",
    layout="centered"
)

st.title("🤝 صديقك الذكي: كالي")

# قراءة API KEY من Secrets
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

# تفعيل Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# تعليمات الشخصية
system_instruction = """
أنت كالي، مساعد ذكي يتحدث باللهجة العراقية بشكل ودي ومحترم.

في بداية أي محادثة قل:
مرحبا عباس، شلونك يا خوي؟

إذا تم ذكر الوالدة قل:
مرحباً بالخالة الغالية.
"""

# إنشاء الموديل
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash",
    system_instruction=system_instruction
)

# حفظ المحادثة
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# عرض الرسائل السابقة
for message in st.session_state.chat.history:
    role = "assistant"

    try:
        if message.role == "user":
            role = "user"
    except:
        pass

    with st.chat_message(role):
        try:
            st.markdown(message.parts[0].text)
        except:
            pass

# صندوق الكتابة
prompt = st.chat_input("اسأل كالي...")

if prompt:

    # عرض رسالة المستخدم
    with st.chat_message("user"):
        st.markdown(prompt)

    # إرسال الرسالة
    try:
        response = st.session_state.chat.send_message(prompt)

        # عرض الرد
        with st.chat_message("assistant"):
            st.markdown(response.text)

    except Exception as e:
        st.error("حدث خطأ، تأكد من API KEY")
        st.code(str(e))
