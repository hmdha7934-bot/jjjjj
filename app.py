import streamlit as st
import time
import random

# إعدادات الصفحة
st.set_page_config(page_title="JAI | Heart Assistant", layout="centered")

# تصميم بسيط وفخم (Minimalist Dark Theme)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #e0e0e0; }
    /* تنسيق النصوص */
    h1, h2, h3 { color: #00f2fe; font-family: 'Segoe UI', sans-serif; }
    .stTextInput > div > div > input { background-color: #1a1a1a; color: white; border: 1px solid #333; }
    
    /* صندوق بيانات الـ IoT */
    .iot-container {
        border: 1px solid #222;
        padding: 20px;
        border-radius: 10px;
        background: #0a0a0a;
        margin-bottom: 30px;
        text-align: center;
    }
    .pulse-value { font-size: 40px; color: #ff0055; font-weight: bold; }
    
    /* شاشة الشات */
    .chat-area { border-top: 1px solid #222; padding-top: 20px; }
    .role-label { color: #00f2fe; font-weight: bold; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

# العنوان
st.markdown("<h1 style='text-align: center;'>JAI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>نظام الذكاء الاصطناعي لرعاية مرضى القلب (IoT Enabled)</p>", unsafe_allow_html=True)

# --- قسم إنترنت الأشياء (IoT) ---
st.markdown("<div class='iot-container'>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"النبض الحالي<br><span class='pulse-value'>❤️ {random.randint(70, 75)}</span>", unsafe_allow_html=True)
with col2:
    st.markdown("الأكسجين<br><span style='font-size: 25px;'>98%</span>", unsafe_allow_html=True)
with col3:
    st.markdown("حالة الجهاز<br><span style='color: #00f2fe;'>متصل Online</span>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- قسم الشات (بدون فقاعات) ---
if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "ai", "content": "مرحباً، أنا JAI. مساعدك الذكي المتصل بحساسات قلبك. كيف يمكنني مساعدتك اليوم؟"}]

# عرض الشات ببساطة
for msg in st.session_state.messages:
    if msg["role"] == "ai":
        st.markdown(f"<p style='color: #00f2fe; font-weight: bold; direction: rtl; text-align: right;'>🤖 JAI</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='direction: rtl; text-align: right; margin-bottom: 20px;'>{msg['content']}</p>", unsafe_allow_html=True)
    else:
        st.markdown(f"<p style='color: #ffffff; font-weight: bold; direction: rtl; text-align: right;'>👤 أنتِ</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='direction: rtl; text-align: right; margin-bottom: 20px;'>{msg['content']}</p>", unsafe_allow_html=True)

# منطقة الإدخال
st.markdown("<div class='chat-area'>", unsafe_allow_html=True)
user_input = st.text_input("", placeholder="اكتبي رسالتك هنا...", key="input")

if st.button("إرسال") and user_input:
    # إضافة رسالة المستخدم
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # رد JAI
    with st.spinner("JAI يحلل..."):
        time.sleep(0.8)
        if "تعب" in user_input or "ألم" in user_input:
            response = "سلامتك. قمت بتحليل بيانات الحساسات فوراً؛ نبضك مستقر حالياً ولكن سأبقى في حالة تأهب. يفضل أن تأخذي قسطاً من الراحة."
        elif "نصيحة" in user_input:
            response = "بصفتي ذكاء اصطناعي مرتبط بقلبك، أنصحك اليوم بتجنب المجهود البدني العالي وشرب السوائل بانتظام."
        else:
            response = "فهمت عليكِ. أنا هنا لمراقبة مؤشراتك الحيوية ومساعدتك في أي وقت."
        
        st.session_state.messages.append({"role": "ai", "content": response})
        st.rerun()

st.markdown("---")
st.caption("تطوير: الجوري - مشروع إنترنت الأشياء والذكاء الاصطناعي")
