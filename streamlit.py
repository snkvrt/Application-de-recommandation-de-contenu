import streamlit as st
import requests
import os
import ast

current_directory = os.getcwd()


# Fonction pour appeler la fonction Azure
def call_azure_function(selected_id):
   

    response = requests.get(f'https://openclassroom-projet-9-alwis.azurewebsites.net/api/httptrigger1?code=N2QuyfeQkzTX7oj7mx7FitPCAd7zVS7E0WzlmGWD-3f5AzFuUy3sXQ%3D%3D&userid={selected_id}', verify=True)



    if response.status_code == 200:
  

        # Assuming recommendation_str is the string representation of the list
        recommendation_str = response.text

        # Use ast.literal_eval to safely convert the string to a Python list
        recommendation_list = ast.literal_eval(recommendation_str)

        return recommendation_list
    else:
        return None

def main():
    st.title("Application de recommandations d'articles")

    user_id = st.text_input("Entrez l'ID de l'utilisateur")

    if st.button("Obtenir les articles"):
        article_ids = call_azure_function(user_id)

        if article_ids is not None:
            st.success(f"Les articles recommandés pour l'utilisateur {user_id} sont : {article_ids}")
        else:
            st.error("Une erreur s'est produite.")

if __name__ == "__main__":
    main()
