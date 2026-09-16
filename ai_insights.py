import streamlit as st
from database import get_dataframe


def show_ai_insights():

    st.title("🤖 AI Insights")

    df = get_dataframe()

    if df.empty:
        st.warning("No registrations found.")
        return

    # -----------------------------
    # Summary Metrics
    # -----------------------------
    total = len(df)
    checked = len(df[df["checkin_status"] == "Checked In"])
    pending = len(df[df["checkin_status"] == "Pending"])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("👥 Total Registrations", total)

    with col2:
        st.metric("✅ Checked In", checked)

    with col3:
        st.metric("⏳ Pending", pending)

    st.markdown("---")

    # -----------------------------
    # AI Summary
    # -----------------------------
    st.subheader("📊 AI Registration Analysis")

    st.write("🏫 Most Popular Department:",
             df["department"].mode()[0])

    st.write("🎯 Most Popular Event:",
             df["event"].mode()[0])

    st.write("🏙️ Most Common City:",
             df["city"].mode()[0])

    st.write("👨 Average Age:",
             round(df["age"].mean(), 1))

    st.markdown("---")

    # -----------------------------
    # Recommendations
    # -----------------------------
    st.subheader("🤖 AI Recommendations")

    if pending > checked:
        st.warning(
            "Many attendees have not checked in yet. Consider sending reminder notifications."
        )
    else:
        st.success(
            "Excellent! Most attendees have already completed check-in."
        )

    if total >= 100:
        st.info(
            "High registration count detected. Consider increasing venue capacity."
        )
    else:
        st.info(
            "Registration volume is currently within expected capacity."
        )

    st.markdown("---")

    st.success("🎉 AI Insights Generated Successfully!")