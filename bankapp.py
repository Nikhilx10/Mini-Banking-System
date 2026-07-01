import streamlit as st

st.title("🏦 Mini Banking System")

# Balance ko session me store karna
if "balance" not in st.session_state:
    st.session_state.balance = 0

menu = st.selectbox(
    "Choose an Option",
    ["Check Balance", "Deposit Money", "Withdraw Money"]
)

if menu == "Check Balance":
    st.subheader(f"Current Balance: ₹{st.session_state.balance}")

elif menu == "Deposit Money":
    amount = st.number_input(
        "Enter amount to deposit",
        min_value=0.0,
        step=100.0
    )

    if st.button("Deposit"):
        st.session_state.balance += amount
        st.success(f"₹{amount} deposited successfully!")
        st.write(f"New Balance: ₹{st.session_state.balance}")

elif menu == "Withdraw Money":
    amount = st.number_input(
        "Enter amount to withdraw",
        min_value=0.0,
        step=100.0
    )

    if st.button("Withdraw"):
        if amount <= st.session_state.balance:
            st.session_state.balance -= amount
            st.success(f"₹{amount} withdrawn successfully!")
            st.write(f"Remaining Balance: ₹{st.session_state.balance}")
        else:
            st.error("Insufficient balance!")