import streamlit as st
import pandas as pd
from database import get_dataframe


def show_dashboard():

    st.title("📊 Registration Dashboard")

    df = get_dataframe()

    if df.empty:
        st.warning("No attendees registered yet.")
        return

    # ---------------- Dashboard Cards ----------------

    total = len(df)
    checked = len(df[df["checkin_status"] == "Checked In"])
    pending = len(df[df["checkin_status"] == "Pending"])
    capacity = 500

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("👥 Total", total)
    col2.metric("✅ Checked In", checked)
    col3.metric("⏳ Pending", pending)
    col4.metric("🎯 Capacity", capacity)

    st.markdown("---")

    # ---------------- Search ----------------

    search = st.text_input("🔍 Search Attendee")

    if search:
        df = df[df["name"].str.contains(search, case=False, na=False)]

    # ---------------- Filters ----------------

    col1, col2 = st.columns(2)

    with col1:
        department = st.selectbox(
            "Department",
            ["All"] + sorted(df["department"].dropna().unique().tolist())
        )

    with col2:
        event = st.selectbox(
            "Event",
            ["All"] + sorted(df["event"].dropna().unique().tolist())
        )

    if department != "All":
        df = df[df["department"] == department]

    if event != "All":
        df = df[df["event"] == event]

    st.markdown("---")

    # ---------------- Table ----------------

    st.subheader("📋 Registered Attendees")

    st.dataframe(df, width="stretch")

    # ---------------- Export CSV ----------------

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Export Registrations to CSV",
        data=csv,
        file_name="registrations.csv",
        mime="text/csv"
    )