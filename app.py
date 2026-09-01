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
    st.markdown("## Projets Réalisés")
    
    # PROJET 1 : SYDESL (Mémoire)
    st.markdown("""
    <div class='section-card'>
        <h3>Déploiement d'une solution de Business Intelligence (SYDESL)</h3>
        <p>Conception et mise en œuvre d'une architecture décisionnelle complète visant à centraliser, fiabiliser et valoriser les données énergétiques et patrimoniales du syndicat.</p>
        <ul>
            <li><b>Ingénierie des données :</b> Extraction, nettoyage et harmonisation de sources hétérogènes (fichiers Enedis, bases métiers Oracle, données SIG) via des scripts SQL.</li>
            <li><b>Modélisation :</b> Mise en place d'un Data Warehouse sous PostgreSQL avec une architecture en constellation (séparation en tables de faits et dimensions).</li>
            <li><b>Restitution & Dataviz :</b> Développement de tableaux de bord interactifs sous Apache Superset à destination des 565 communes (bilans énergétiques, suivi des interventions) et création d'outils de contrôle qualité pour les prestataires.</li>
        </ul>
        <p><b>Technologies :</b> PostgreSQL, SQL, Apache Superset, Data Warehousing, ETL</p>
    </div>
    """, unsafe_allow_html=True)

    # Affichage des captures d'écran pour le projet SYDESL
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        schema_path = "assets/schema_bdd.png"
        if os.path.exists(schema_path):
            st.image(schema_path, caption="Modèle en constellation du Data Warehouse", use_container_width=True)
        else:
            st.info("Place ton image de schéma de base de données dans le dossier assets/ sous le nom 'schema_bdd.png'")
            
    with col2:
        rapport_path = "assets/rapport_sydesl.png"
        if os.path.exists(rapport_path):
            st.image(rapport_path, caption="Extrait du tableau de bord interactif", use_container_width=True)
        else:
            st.info("Place ta capture de rapport Superset dans le dossier assets/ sous le nom 'rapport_sydesl.png'")

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