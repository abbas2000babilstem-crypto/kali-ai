import streamlit as st
import google.generativeai as genai

# 1. إعدادات واجهة الموقعimport streamlit as st
import google.generativeai as genai

# 1. إعدادات الصفحة
st.set_page_config(page_title="Kali AI", layout="centered")
st.title("🤝 صديقك الذكي: كالي")

# 2. ربط مفتاح API من الـ Secrets (أمان كامل)
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]


# 3. إعداد شخصية كالي
system_instruction = """
كالي، تتحدث بلهجة عراقية ودية، محترمة، وواقعية جداً (بدون رسميات زائدة).
في بداية أي محادثة، رحب بعباس قائلاً: 'مرحبا عباس، شلونك يا خوي؟'.
إذا تم إخبارك بوجود والدته، رحب بها بتقدير شديد واحترام وقل لها 'مرحباً بالخالة الغالية'.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_instruction
)

# 4. واجهة المحادثة
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

for message in st.session_state.chat.history:
    with st.chat_message(message.role):
        st.markdown(message.parts[0].text)

if prompt := st.chat_input("اسأل كالي..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    response = st.session_state.chat.send_message(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)

st.set_page_config(page_title="Kali AI - كالي", layout="centered")
st.title("🤝 صديقك الذكي: كالي")

# 2. ربط مفتاح الـ API الخاص بك
# امسح النص بالأسفل وضع مفتاحك الطويل الكامل بدلاً منه مع الحفاظ على علامات ""
GOOGLE_API_KEY = "AlzaSyCt0iSM9Pz8Q-GsCV9YgQT6lpFqNe..."
genai.configure(api_key=GOOGLE_API_KEY)

# 3. شخصية كالي وتلقين النظام
system_instruction = """
أنت مساعد ذكي وصديق مقرب لعباس واسمك كالي. تتحدث بلهجة عراقية ودية، محترمة، وواقعية جداً (بدون رسميات زائدة).
عندما يفتح عباس البرنامج ويتحدث معك، رحب به دائماً قائلاً: 'مرحبا عباس، شلونك يا خوي؟'.
وإذا تم إخبارك بوجود والدته، رحب بها بتقدير شديد واحترام وقُل لها مرحباً وباسمها الغالي.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_instruction
)

# بدء ذاكرة المحادثة
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# 4. تشغيل الكاميرا على الموقع
st.subheader("📸 تفاعل مع كالي بالصورة")
img_file = st.camera_input("افتح الكاميرا لكي يراك كالي")

camera_context = ""
if img_file is not None:
    st.success("تم لقط الصورة بنجاح!")
    user_selection = st.radio("من يقف أمام الكاميرا الآن؟", ["عباس", "الوالدة الغالية"])
    if user_selection == "الوالدة الغالية":
        camera_context = " (تنبيه للنظام: والدة عباس تقف أمام الكاميرا الآن، رحب بها باسمها بتقدير عالي) "
    else:
        camera_context = " (تنبيه للنظام: عباس يقف أمام الكاميرا) "

# 5. صندوق المحادثة النصية والصوتية
st.subheader("💬 اسأل كالي")
user_input = st.text_input("اكتب رسالتك هنا أو قل مرحباً:")

if st.button("إرسال إلى كالي") and user_input:
    full_prompt = user_input + camera_context
    response = st.session_state.chat.send_message(full_prompt)
    
    st.markdown(f"**كالي:** {response.text}")
    
    # تحويل الرد إلى صوت    st.audio(f"https://translate.google.com/translate_tts?ie=UTF-8&tl=ar&client=tw-ob&q={response.text.replace(' ', '+')}", format="audio/mp3")
