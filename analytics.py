
import streamlit as st
import plotly.express as px
from database import get_dataframe


def show_analytics():

    st.header("📈 Registration Analytics")

    df = get_dataframe()

    if df.empty:
        st.warning("No registration data available.")
        return

    # -------- Statistics --------

    col1, col2, col3 = st.columns(3)

    col1.metric("👥 Total Registrations", len(df))
    col2.metric("🏫 Departments", df["department"].nunique())
    col3.metric("🎯 Events", df["event"].nunique())

    st.markdown("---")

    # -------- Department Chart --------

    st.subheader("📊 Department-wise Registrations")

    dept = df["department"].value_counts().reset_index()
    dept.columns = ["Department", "Count"]

    fig1 = px.bar(
        dept,
        x="Department",
        y="Count",
        color="Department",
        text="Count"
    )

    st.plotly_chart(fig1, use_container_width=True)

    # -------- Gender Chart --------

    st.subheader("👨‍🎓 Gender Distribution")

    fig2 = px.pie(
        df,
        names="gender",
        hole=0.45
    )

    st.plotly_chart(fig2, use_container_width=True)

    # -------- Event Chart --------

    st.subheader("🎯 Event Registrations")

    event = df["event"].value_counts().reset_index()
    event.columns = ["Event", "Count"]

    fig3 = px.bar(
        event,
        x="Event",
        y="Count",
        color="Event",
        text="Count"
    )

    st.plotly_chart(fig3, use_container_width=True)

    # -------- City Chart --------

    st.subheader("🏙️ City-wise Registrations")

    city = df["city"].value_counts().reset_index()
    city.columns = ["City", "Count"]

    fig4 = px.bar(
        city,
        x="City",
        y="Count",
        color="City",
        text="Count"
    )

    st.plotly_chart(fig4, use_container_width=True)