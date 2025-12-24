import streamlit as st
import time
import random

# إعدادات الواجهة (Dark Mode الاحترافي)
st.set_page_config(page_title="JAI | Heart Guard", page_icon="❤️", layout="wide")

# تصميم CSS متطور (خلفية متحركة وتنسيق شات فخم)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp {
        background: radial-gradient(circle, #001524 0%, #000000 100%);
        color: #00f2fe;
        font-family: 'Tahoma', sans-serif;
    }
    
    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 50px;
        text-align: center;
        background: linear-gradient(90deg, #00f2fe, #ff0055);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 20px rgba(0, 242, 254, 0.5);
    }

    .heart-monitor {
        background: rgba(0, 242, 254, 0.05);
        border: 1px solid #00f2fe;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 0 30px rgba(0, 242, 254, 0.2);
    }

    .pulse-rate {
        font-size: 80px;
        color: #ff0055;
        font-weight: bold;
        text-shadow: 0 0 15px #ff0055;
    }

    .ai-chat {
        background: rgba(255, 255, 255, 0.03);
        border-left: 4px solid #00f2fe;
        padding: 20px;
        margin: 15px 0;
        border-radius: 0 15px 15px 0;
        direction: rtl;
        text-align: right;
    }
    </style>
    """, unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown("<h1 class='main-title'>JAI : THE HEART GUARD</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>نظام الجوري الذكي لرعاية مرضى القلب عبر إنترنت الأشياء</p>", unsafe_allow_html=True)

# محاكاة بيانات إنترنت الأشياء (IoT Simulation)
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<div class='heart-monitor'>", unsafe_allow_html=True)
    st.write("📡 **حساس النبض المتصل (IoT Sensor)**")
    bpm = random.randint(72, 78)
    st.markdown(f"<div class='pulse-rate'>❤️ {bpm}</div>", unsafe_allow_html=True)
    st.write("الحالة: مستقرة ✅")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='heart-monitor'>", unsafe_allow_html=True)
    st.write("🩺 **تحليل JAI للبيانات الحيوية**")
    st.write("ضغط الدم: 120/80 mmHg")
    st.write("مستوى الأكسجين: 99%")
    st.progress(99)
    st.write("درجة حرارة الجسم: 37°C")
    st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# نظام المحادثة الذكي (JAI Assistant)
if 'chat' not in st.session_state:
    st.session_state.chat = [{"role": "ai", "text": "أهلاً بك، أنا JAI. لقد قمت بمزامنة بيانات قلبك عبر حساسات إنترنت الأشياء. كيف تشعر اليوم؟"}]

for msg in st.session_state.chat:
    color = "#00f2fe" if msg["role"] == "ai" else "#ffffff"
    st.markdown(f"<div class='ai-chat' style='border-color: {color};'><b>{'🤖 JAI' if msg['role'] == 'ai' else '👤 المريض'}:</b><br>{msg['text']}</div>", unsafe_allow_html=True)

user_msg = st.text_input("تحدث مع JAI...")

if st.button("إرسال") and user_msg:
    st.session_state.chat.append({"role": "user", "text": user_input})
    
    # منطق الذكاء الاصطناعي
    with st.spinner("JAI يحلل طلبك..."):
        time.sleep(1)
        if "ألم" in user_msg or "تعب" in user_msg:
            reply = "🚨 تنبيه طارئ: لاحظت قلقك. قمت الآن بتشغيل بروتوكول فحص القلب المتقدم وإبلاغ الطوارئ بموقعك الجغرافي عبر نظام الـ IoT. ابقَ هادئاً."
        elif "نصيحة" in user_msg:
            reply = "بناءً على بياناتك المسجلة خلال الـ 24 ساعة الماضية، أنصحك بتقليل الكافيين اليوم وزيادة شرب الماء بمقدار 500 مل."
        else:
            reply = f"لقد حللت رسالتك: '{user_msg}'. كذكاء اصطناعي، أنا أتعلم من نمط حياتك لأحميك بشكل أفضل. هل تريد جدولاً غذائياً لليوم؟"
        
        st.session_state.chat.append({"role": "ai", "text": reply})
        st.rerun()

st.markdown("<br><hr><center>تمت البرمجة بواسطة: <b>الجوري</b> ✨ باستخدام تقنيات الذكاء الاصطناعي</center>", unsafe_allow_html=True)
