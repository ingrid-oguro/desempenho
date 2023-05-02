import pickle 
from pathlib import Path

import streamlit-authenticator as stauth

names=["Peter Parker","Rebecca Miller"]
usernames = ["pparker","rmiller"]
passwords = ["abc123","def456"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hased_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

