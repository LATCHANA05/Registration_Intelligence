import streamlit as st
import base64

from registration import show_registration
from dashboard import show_dashboard
from analytics import show_analytics
from checkin import show_checkin
from ai_insights import show_ai_insights


# -----------------------------
# FUNCTION TO LOAD BACKGROUND
# -----------------------------
def get_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="AI Registration Intelligence",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# BACKGROUND IMAGE
# -----------------------------
img = get_base64("assets/images/background.png")

page_bg = f"""
<style>

.stApp {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

[data-testid="stSidebar"] {{
    background: rgba(8,20,40,0.90);
}}

.main-title{{
    text-align:center;
    font-size:46px;
    font-weight:bold;
    color:white;
    text-shadow:2px 2px 8px black;
}}

.sub-title{{
    text-align:center;
    font-size:22px;
    color:white;
    text-shadow:2px 2px 8px black;
}}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🎓 Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "🏠 Home",
        "📝 Registration",
        "📊 Dashboard",
        "📈 Analytics",
        "✅ Check-in",
        "🤖 AI Insights"
    ]
)

# -----------------------------
# HOME PAGE
# -----------------------------
if page == "🏠 Home":

    st.markdown(
        "<div class='main-title'>🎓 AI Registration Intelligence & Attendee Management</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sub-title'>Smart AI Powered Event Registration Platform</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🚀 Current Event")

        st.info("📌 Event : AI Tech Summit 2026")
        st.info("📅 Date : 14 September 2026")
        st.info("📍 Venue : Sona College of Technology")
        st.info("👥 Capacity : 500 Participants")

    with col2:

        st.subheader("✨ Features")

        st.success("✅ Attendee Registration")
        st.success("✅ Registration Dashboard")
        st.success("✅ Analytics")
        st.success("✅ Check-in Tracking")
        st.success("✅ AI Insights")

    st.markdown("---")

    st.subheader("🛠 Technologies Used")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.info("🐍 Python")

    with c2:
        st.info("🌐 Streamlit")

    with c3:
        st.info("💾 SQLite")

    with c4:
        st.info("📊 Pandas")

# -----------------------------
# REGISTRATION PAGE
# -----------------------------
elif page == "📝 Registration":
    show_registration()

# -----------------------------
# DASHBOARD PAGE
# -----------------------------
elif page == "📊 Dashboard":
    show_dashboard()

# -----------------------------
# ANALYTICS PAGE
# -----------------------------
elif page == "📈 Analytics":
    show_analytics()

# -----------------------------
# CHECK-IN PAGE
# -----------------------------
elif page == "✅ Check-in":
    show_checkin()

# -----------------------------
# AI INSIGHTS PAGE
# -----------------------------
elif page == "🤖 AI Insights":
    show_ai_insights()