import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

users = {'usernames': {'utilisateur': {'name': 'utilisateur',
                                       'password': 'utilisateurMDP',
                                       'email': 'utilisateur@gmail.com'
                                       }}}

authenticator = Authenticate(
    users,  # Les données des comptes
    "cookie name",  # Le nom du cookie, un str quelconque
    "cookie key",  # La clé du cookie, un str quelconque
    30,  # Le nombre de jours avant que le cookie expire
)

authenticator.login()

if st.session_state.get("authentication_status"):
    authenticator.logout("Déconnexion")
    st.title(f"Bienvenue {users['usernames']['utilisateur']['name']}")

    selection = option_menu(
        menu_title=None,
        options=["Accueil", "Photos"],
        orientation="horizontal"
    )

    if selection == "Accueil":
        st.write("Bienvenue sur ma page !")
        st.image(r"https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExODZlcTN2OWY4NjBhaWduN294MDI5Z2FmZnFmdmViNjgzcjdjZG5qdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GRPy8MKag9U1U88hzY/giphy.gif")

    elif selection == "Photos":
        st.write("Bienvenue sur mon album photo")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("A cat")
            st.image(r"https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDV1ZW5lc2IyZmY3MDh1c21ieGF3am5lbzN3dGpnZW1xNzNvcjQxdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o85xoi6nNqJQJ95Qc/giphy.gif")

        with col2:
            st.header("Another cat")
            st.image(r"https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWE2aGt6NHA1aTJmY3Z5ZmI3azFrcW9yOWtrdHV1c3hzbHF6NTQ2MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lJNoBCvQYp7nq/giphy.gif")

        with col3:
            st.header("Another cat")
            st.image(r"https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmh1emM1YjZhMzE5c3V0eXoxaDJ3ZHVsbmcwZ2JmdWk0aHZmMWQxZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/mlvseq9yvZhba/giphy.gif")

elif st.session_state.get("authentication_status") is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state.get("authentication_status") is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
