import streamlit as st
from database import get_dataframe, checkin_attendee


def show_checkin():

    st.title("✅ Attendee Check-in")

    # Load all attendees
    df = get_dataframe()

    if df.empty:
        st.warning("No attendees registered yet.")
        return

    # Select attendee
    selected_name = st.selectbox(
        "Select Attendee",
        df["name"]
    )

    # Get selected attendee details
    attendee = df[df["name"] == selected_name].iloc[0]

    st.markdown("---")
    st.subheader("👤 Attendee Details")

    st.write("**Name:**", attendee["name"])
    st.write("**Email:**", attendee["email"])
    st.write("**Phone:**", attendee["phone"])
    st.write("**College:**", attendee["college"])
    st.write("**Department:**", attendee["department"])
    st.write("**Event:**", attendee["event"])
    st.write("**City:**", attendee["city"])
    st.write("**Age:**", attendee["age"])
    st.write("**Gender:**", attendee["gender"])
    st.write("**Status:**", attendee["checkin_status"])

    st.markdown("---")

    # Check-in button
    if attendee["checkin_status"] == "Pending":

        if st.button("✅ Check In"):

            # Update database
            checkin_attendee(int(attendee["id"]))

            st.success("🎉 Check-in Successful!")

            st.rerun()

    else:

        st.success("✅ Already Checked In")

        st.write("🕒 Check-in Time:", attendee["checkin_time"])