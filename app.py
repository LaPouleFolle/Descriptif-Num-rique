import os
import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Arsène Gaby Mbabeh Meye",
    layout="wide",
)

# Fonction pour charger le fichier CSS externe
def load_css(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Chargement du style
load_css("assets/style.css")

# --- MENU DE NAVIGATION ---
selected_tab = st.radio(
    "Navigation", 
    ["Accueil & CV", "Compétences & Expertises", "Projets", "Contact"], 
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("<br>", unsafe_allow_html=True)

# ================= PAGE 1 : ACCUEIL & CV =================
if selected_tab == "Accueil & CV":
    col1, col2 = st.columns([1.2, 2], gap="large")

    with col1:
        photo_path = "assets/photo.jpg"
        if os.path.exists(photo_path):
            st.image(photo_path, use_container_width=True)
        else:
            alt_photos = [f"assets/{f}" for f in os.listdir("assets") if f.startswith("WhatsApp")]
            if alt_photos:
                st.image(alt_photos[0], use_container_width=True)
            else:
                st.info("Photo non trouvée dans assets/")

    with col2:
        st.markdown("<h1 style='font-size: 3rem; line-height: 1.1; color: #0284c7;'>ARSÈNE GABY<br>MBABEH MEYE</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #334e68 !important;'>Data Analyst & Business Intelligence</h3>", unsafe_allow_html=True)
        st.write("Data Analyst fort de quatre années d'expérience en alternance. De la structuration des bases de données à la création d'outils de Business Intelligence, je transforme les données brutes en informations claires pour faciliter la prise de décision stratégique.")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        cv_path = "assets/Mon cv pro.pdf"
        if os.path.exists(cv_path):
            with open(cv_path, "rb") as f:
                st.download_button(
                    label="Télécharger mon CV officiel",
                    data=f,
                    file_name="CV_Arsene_Mbabeh_Meye.pdf",
                    mime="application/pdf",
                )
        else:
            st.warning("CV introuvable dans le dossier assets.")

# ================= PAGE 2 : COMPÉTENCES & EXPERTISES =================
elif selected_tab == "Compétences & Expertises":
    st.markdown("## Mes Domaines d'Expertise")
    
    col_a, col_b = st.columns(2, gap="medium")
    
    with col_a:
        st.markdown("""
        <div class='section-card'>
            <h3>Bases de Données & Architecture</h3>
            <ul>
                <li><b>SQL avancé :</b> PostgreSQL, Oracle, Sybase</li>
                <li><b>Modélisation :</b> Création de Data Warehouse, architecture en constellation, schéma en étoile</li>
                <li><b>Traitement :</b> Processus ETL, nettoyage et harmonisation de sources de données hétérogènes</li>
            </ul>
        </div>
        
        <div class='section-card'>
            <h3>Programmation & Outils</h3>
            <ul>
                <li><b>Python :</b> Pandas, NumPy, Matplotlib, Streamlit</li>
                <li><b>Écosystème SAS :</b> SAS Viya</li>
                <li><b>Autres langages :</b> SQL, R, HTML, CSS, PHP </li>
                <li><b>Développement :</b> Git, GitHub, environnement Onyxia</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_b:
        st.markdown("""
        <div class='section-card'>
            <h3>Business Intelligence & Dataviz</h3>
            <ul>
                <li><b>Outils open-source :</b> Apache Superset</li>
                <li><b>Outils propriétaires :</b> SAS Visual Analytics, Power BI, Tableau</li>
                <li><b>Restitution :</b> Création de tableaux de bord dynamiques, indicateurs de pilotage, reporting sous Excel</li>
            </ul>
        </div>
        
        <div class='section-card'>
            <h3>Méthodologie & Pilotage</h3>
            <ul>
                <li>Analyse exploratoire et statistiques (descriptives, inférentielles, régressions)</li>
                <li>Documentation technique et cartographie des processus métiers</li>
                <li>Gouvernance des données et création de tableaux de contrôle qualité</li>
                <li>Vulgarisation décisionnelle auprès des interlocuteurs métiers</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)


 # ================= PAGE 3 : PROJETS =================
elif selected_tab == "Projets":
    st.markdown("## 💼 Projets Réalisés")
    
    # PROJET 1 : SYDESL (Mémoire)
    st.markdown("""
    <div class='section-card'>
        <h3> Déploiement d'une solution de Business Intelligence (SYDESL)</h3>
        <p>Dans le cadre du développement des tableaux de bord communaux, il était essentiel de structurer les données collectées de manière cohérente et interrogeable efficacement. Pour cela, j’ai mis en place une architecture décisionnelle reposant sur un modèle en constellation, entièrement implémentée dans PostgreSQL.</p>
        <p>Les données exploitées provenaient de plusieurs environnements distincts, qu’il a fallu consolider dans une logique commune :</p>
        <ul>
            <li><b>Données métiers :</b> Issues de la base Oracle du SYDESL, consultées à travers des <i>foreign tables</i> PostgreSQL.</li>
            <li><b>Fichiers externes :</b> Intégration et retraitement des données transmises par Enedis.</li>
            <li><b>Tables locales :</b> Créées directement dans PostgreSQL pour structurer, compléter l'information et alimenter les tableaux de bord sur Apache Superset.</li>
        </ul>
        <p><b>Technologies :</b> PostgreSQL, Oracle, Apache Superset (pour la création du dashboard), SQL avancée , Modèle en constellation, Data Warehousing</p>
    </div>
    """, unsafe_allow_html=True)

    # Affichage des captures d'écran pour le projet SYDESL
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        schema_path = "assets/schema_bdd.png"
        if os.path.exists(schema_path):
            st.image(schema_path, caption="Modèle en constellation du Data Warehouse", use_container_width=True)
        else:
            st.info("Image base de donnée : 'schema_bdd.png'")
            
    with col2:
        rapport_path = "assets/rapport_sydesl.png"
        if os.path.exists(rapport_path):
            st.image(rapport_path, caption="Extrait du tableau de bord interactif", use_container_width=True)
        else:
            st.info("capture d'écran superset : 'rapport_sydesl.png'")

# ================= PAGE 4 : CONTACT =================
elif selected_tab == "Contact":
    st.markdown("## Me contacter")
    st.write("Un projet, une opportunité ou une question ? N'hésite pas à me contacter directement via les canaux ci-dessous :")
    
    st.markdown("""
    <div class='section-card' style='text-align: center;'>
        <p><b>LinkedIn :</b> <a href='https://www.linkedin.com/in/arsène-mbabeh-meye-4823a9258' target='_blank' style='color: #0284c7;'>Mon profil LinkedIn</a></p>        <p><b>GitHub :</b> <a href='https://github.com/LaPouleFolle' target='_blank' style='color: #0284c7;'>Mes dépôts GitHub</a></p>
        <p><b>Email :</b>arsenemeye.mb@gmail.com</p>
    </div>
    """, unsafe_allow_html=True)