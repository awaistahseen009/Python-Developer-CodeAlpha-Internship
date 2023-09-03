import streamlit as st
import string
import random
st.set_page_config(
    page_title="Password Generator",
    page_icon=":lock:", 
)
st.title("Password Generator")

generation_mode = st.selectbox("Select Generation Mode", ["Manual", "Automatic"])

n_alphabets, n_digits, n_special_chars = 0, 0, 0
password_length = 8 
generated_password=None

if generation_mode == "Manual":
    n_alphabets = st.number_input("Number of Alphabets", min_value=0, step=1, value=0)
    n_digits = st.number_input("Number of Digits", min_value=0, step=1, value=0)
    n_special_chars = st.number_input("Number of Special Characters", min_value=0, step=1, value=0)
elif generation_mode == "Automatic":
    password_length = st.number_input("Password Length", min_value=1, step=1, value=8)
    total_chars = random.randint(1, password_length)
    alphabets = random.randint(0, total_chars)
    digits = random.randint(0, abs(total_chars - alphabets))
    special_chars = abs(total_chars - (alphabets + digits))


def generate_password(alphabets, digits, special_chars, password_length):
    alphabet = string.ascii_letters
    numbers = string.digits
    special_characters = string.punctuation
    if (n_alphabets == 0 and n_digits == 0 and n_special_chars == 0) and generation_mode!='Automatic':
        st.warning("Please select the values of the alphabets , digits and special characters")
        return None
    if (n_alphabets + n_digits + n_special_chars < 8)  and generation_mode!='Automatic' :
        st.warning("Your password length should be equal or greater than 8")
        return None
    if password_length<8:
        st.warning("Please select length of password greater or equal to 8.")
        return None
    password = random.choices(alphabet, k=alphabets)
    password += random.choices(numbers, k=digits)
    password += random.choices(special_characters, k=special_chars)
    remaining_length = password_length - len(password)
    password += random.choices(alphabet + numbers + special_characters, k=remaining_length)

    random.shuffle(password)
    return ''.join(password)

if st.button("Get Password"):
    generated_password = generate_password(n_alphabets, n_digits, n_special_chars, password_length)
    if generated_password:
        st.success("Generated Password Successfully" )
        st.success(generated_password)
if generated_password:
    st.info("To copy the password, select it and use the standard copy keyboard shortcut (e.g., Ctrl+C on Windows, Command+C on macOS).")