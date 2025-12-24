import streamlit as st
import time
import random

# إعدادات الصفحة
st.set_page_config(page_title="JAI | مساعد مرضى القلب الذكي", page_icon="❤️", layout="centered")

# تصميم واجهة JAI الطبية
st.markdown("""
    <style>
    .stApp { background-color: #000a12; color: white; }
    .jai-card { background: rgba(0, 255, 255, 0.05); border: 2px solid #00f2fe; padding: 25px; border-radius: 20px; text-align: center; box-shadow: 0 0 20px #00f2fe; }
    .pulse-text { font-size: 50px; color: #ff0055; font-weight: bold; animation: heartbeat 1s infinite; }
    @keyframes heartbeat { 0% { transform: scale(1); } 50% { transform: scale(1.1); } 100% { transform: scale(1); } }
    .chat-bubble { padding: 15px; border-radius: 15px; margin: 10px 0; direction: rtl; text-align: right; }
    .ai-bubble { background-color: #1a2a3a; border-right: 5px solid #00f2fe; }
    .user-bubble { background-color: #2c3e50; border-left: 5px solid #ff0055; }
    </style>
    """, unsafe_allow_html=True)

# الذاكرة
if 'chat_history' not in st.session_state: st.session_state.chat_history = []
if 'iot_active' not in st.session_state: st.session_state.iot_active = False

# العنوان
st.markdown("<h1 style='text-align: center; color: #00f2fe;'>🤖 JAI: قلبك في أمان</h1>", unsafe_allow_html=True)
st.write("---")

# --- الجزء الأول: محاكاة إنترنت الأشياء (IoT) ---
with st.container():
    st.markdown("<div class='jai-card'>", unsafe_allow_html=True)
    st.write("### 📊 بيانات الحساسات الحية (IoT)")
    
    col1, col2 = st.columns(2)
    with col1:
        pulse = random.randint(70, 85) if not st.session_state.iot_active else random.randint(110, 140)
        st.markdown(f"نبض القلب الآن: <br><span class='pulse-text'>{pulse} BPM</span>", unsafe_allow_html=True)
    with col2:
        st.write("حالة الأكسجين: 98%")
        st.write("ضغط الدم: 120/80")
    
    if st.button("محاكاة حالة طوارئ (ارتفاع نبض) 🚨"):
        st.session_state.iot_active = True
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- الجزء الثاني: المساعد الذكي JAI (المحادثة) ---
st.write("---")
st.write("### 💬 تحدث مع JAI (مساعدك الشخصي)")

# عرض المحادثة السابقة
for msg in st.session_state.chat_history:
    style = "user-bubble" if msg["role"] == "user" else "ai-bubble"
    st.markdown(f"<div class='chat-bubble {style}'><b>{msg['author']}:</b> {msg['content']}</div>", unsafe_allow_html=True)

# إدخال المستخدم
user_text = st.text_input("اسأل JAI عن حالتك الصحية أو اطلب نصيحة:")

if st.button("إرسال إلى JAI"):
    if user_text:
        st.session_state.chat_history.append({"role": "user", "author": "المريض", "content": user_text})
        
        # منطق JAI الذكي
        with st.spinner("JAI يحلل بياناتك..."):
            time.sleep(1)
            if "تعبان" in user_text or "ألم" in user_text:
                response = "يا لطيف، سلامتك! JAI لاحظ ارتفاع بسيط في نبضك. تنفس بعمق، سأقوم الآن بإرسال تنبيه لعائلتك ولطبيبك الخاص فوراً."
            elif "نصيحة" in user_text or "أكل" in user_text:
                response = "بصفتي مساعدك الذكي JAI، أنصحك اليوم بتقليل الملح في الطعام وشرب كمية كافية من الماء. نبضك اليوم مستقر وممتاز!"
            elif "مرحبا" in user_text or "مين" in user_text:
                response = "أهلاً بك! أنا JAI، نظام ذكاء اصطناعي من تطوير المبرمجة الجوري. أنا هنا لأراقب قلبك عبر تقنية إنترنت الأشياء وأسولف معك وأطمنك دائماً."
            else:
                response = "فهمت عليك. بياناتي الحالية تقول إن وضعك الصحي مستقر. هل تشعر بأي شيء آخر تود إخباري به؟"
        
        st.session_state.chat_history.append({"role": "ai", "author": "🤖 JAI", "content": response})
        st.rerun()

# مسح
if st.button("إعادة ضبط النظام 🧹"):
    st.session_state.clear()
    st.rerun()

st.write("---")
st.caption("تم تطوير نظام JAI بواسطة المبدعة الجوري لخدمة مرضى القلب عبر تقنيات الذكاء الاصطناعي وإنترنت الأشياء.")

# سأقوم بحفظ تفضيلاتك حول البرنامج.
