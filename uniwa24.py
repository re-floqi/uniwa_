import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="Πρόγραμμα Μαθημάτων", layout="wide")

    # Έλεγχος πρόσβασης
    password = st.text_input("Εισάγετε κωδικό πρόσβασης:", type="password")
    if password != "uniwa":
        st.warning("Λάθος κωδικός! Δοκιμάστε ξανά.")
        return

    st.title("Πρόγραμμα Μαθημάτων")

    # Δεδομένα μαθημάτων
    data = {
        "Μάθημα": [
            "Αρχιτεκτονική Υπολογιστικών Συστημάτων",
            "Ασφάλεια Πληροφορίας και Συστημάτων",
            "Αρχές Λειτουργικών Συστημάτων (Μαυρομμάτης)",
            "Αρχές Λειτουργικών Συστημάτων (Μάμαλης)",
            "Εισαγωγή στον Αντικειμενοστραφή Προγραμματισμό",
            "Φροντιστηριακό: Αρχές Λειτουργικών Συστημάτων",
            "Φροντιστηριακό: Εισαγωγή στον Αντικειμενοστραφή Προγραμματισμό"
        ],
        "Διδάσκων": [
            "Κ. Ευσταθίου, Ι. Βογιατζής",
            "Στ. Γκρίτζαλης, Ι. Καντζάβελου",
            "Κ. Μαυρομμάτης",
            "Β. Μάμαλης",
            "Ν. Καρανικόλας, Χ. Τρούσσας",
            "Γ. Μελετίου",
            "Γ. Μελετίου"
        ],
        "Παρασκευή": ["17:00-19:30", "19:30-22:00", "", "", "", "", ""],
        "Σάββατο": ["", "", "9.00-11.30", "9.00-11.30", "11.30-14:00", "", ""],
        "Τετάρτη": ["", "", "", "", "", "19:00-21:00", ""],
        "Πέμπτη": ["", "", "", "", "", "", "19:00-21:00"],
        "Σύνδεσμος": [
            "https://teams.microsoft.com/l/meetup-join/19%3a7a4e35dafd32451591b83e2304bbfc9a%40thread.tacv2/1712322265073?context=%7b%22Tid%22%3a%220c8943ee-c370-4bb3-ba51-321f406f32ec%22%2c%22Oid%22%3a%2238e5a68b-7963-4618-9ca6-0542aa70c068%22%7d",
            "https://teams.microsoft.com/l/meetup-join/19%3ameeting_MTExNDc5NTMtYzllYy00Njk3LTljNDYtZTQ1MTMwYjU5YTkx%40thread.v2/0?context=%7b%22Tid%22%3a%220c8943ee-c370-4bb3-ba51-321f406f32ec%22%2c%22Oid%22%3a%222bc3bc36-bfda-4ff4-ad7c-39d9d2f673f9%22%7d",
            "https://teams.microsoft.com/l/meetup-join/19%3aceee4278c2c04576ad80dc4fc946c331%40thread.tacv2/1741957480396?context=%7B%22Tid%22%3A%220c8943ee-c370-4bb3-ba51-321f406f32ec%22%2C%22Oid%22%3A%22d81b9745-8088-472a-89a9-fae6ddafc952%22%7D",
            "https://teams.microsoft.com/l/meetup-join/19%3a303a416e979c4e769f4b8902351bad40%40thread.tacv2/1741297060949?context=%7b%22Tid%22%3a%220c8943ee-c370-4bb3-ba51-321f406f32ec%22%2c%22Oid%22%3a%228ecd2155-69d6-402c-b23f-e4a405366ee7%22%7d",
            "https://teams.microsoft.com/l/meetup-join/19%3ASH6JxB1kyMXY7CMtIKfwFNwuGkE97WZxyS0gB5yqlUM1%40thread.tacv2/1741245033805?context=%7B%22Tid%22%3A%220c8943ee-c370-4bb3-ba51-321f406f32ec%22%2C%22Oid%22%3A%22a45b2cb7-3c9a-4f33-9f43-08a5eb06eeb6%22%7D",
            "https://teams.microsoft.com/l/team/19%3A725fda459269485ea8e4f63a2576fefc%40thread.tacv2/conversations?groupId=69f2fe35-3775-4039-aac7-85608b193b49&tenantId=0c8943ee-c370-4bb3-ba51-321f406f32ec",
            "https://teams.microsoft.com/l/team/19%3A48cb3bc2d43e44e5acf3252871b53b89%40thread.tacv2/conversations?groupId=2077a570-133f-4f6e-a342-bb7115f6b4a7&tenantId=0c8943ee-c370-4bb3-ba51-321f406f32ec"
        ]
    }

    df = pd.DataFrame(data)
    df["Σύνδεσμος"] = df["Σύνδεσμος"].apply(lambda x: f'[LINK]({x})')

    st.write("### Μαθήματα")
    st.table(df)

    st.markdown(
        "<div style='position: fixed; bottom: 10px; left: 10px; font-size: 14px; color: gray;'>Ευχαριστούμε τον Mano Papathanasaki για τα link</div>",
        unsafe_allow_html=True)


if __name__ == "__main__":
    main()
