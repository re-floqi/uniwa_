pip freeze > requirements.txt
import streamlit as st
import pandas as pd
import time

# Ensure that the tabulate library is installed
try:
    import tabulate
except ImportError:
    raise ImportError("The 'tabulate' library is required. Please install it using 'pip install tabulate'.")

# Συνάρτηση για φόρτωση ανακοινώσεων από Google Sheets
def load_announcements():
    url = "https://docs.google.com/spreadsheets/d/1dqBSWQTSJmpDH_bkCg43jZ9rvR2sLVevxLDycrb9XM8/export?format=csv"
    df = pd.read_csv(url)
    df['DATE'] = pd.to_datetime(df['DATE'], dayfirst=True)
    df = df.sort_values(by='DATE', ascending=False)
    return df

# Συνάρτηση για φόρτωση προγράμματος από Google Sheets
def load_schedule():
    url = "https://docs.google.com/spreadsheets/d/1JxGZdDt1iWbKSbbOwIueDzj3kzfzBbINxxW0yATcbV4/export?format=csv"
    df = pd.read_csv(url)
    return df

def main():
    st.set_page_config(page_title="Πανεπιστήμιο Δυτικής Αττικής", layout="wide")

    # Sidebar επιλογές
    menu = ["Ανακοινώσεις", "Πρόγραμμα Μαθημάτων"]
    choice = st.sidebar.radio("Επιλέξτε σελίδα:", menu)

    if choice == "Ανακοινώσεις":
        st.title("Ανακοινώσεις")
        df = load_announcements()
        for index, row in df.iterrows():
            st.subheader(row["TITLE"])
            st.write(f"📅 {row['DATE'].strftime('%d/%m/%Y')}")
            st.write(row["DESCRIPTION"])
            st.markdown("---")

        # Αυτόματη ανανέωση κάθε 10 λεπτά
        time.sleep(600)
        st.experimental_rerun()

    elif choice == "Πρόγραμμα Μαθημάτων":
        # Έλεγχος πρόσβασης
        password = st.text_input("Εισάγετε κωδικό πρόσβασης:", type="password")
        if password != "uniwa":
            st.warning("Λάθος κωδικός! Δοκιμάστε ξανά.")
            return

        st.title("Πρόγραμμα Μαθημάτων")

        # Φόρτωση προγράμματος
        df = load_schedule()

        # Προβολή πίνακα
        st.write(df.to_markdown(index=False), unsafe_allow_html=True)
        # Αυτόματη ανανέωση κάθε 10 λεπτά
        time.sleep(600)
        st.experimental_rerun()
if __name__ == "__main__":
    main()
