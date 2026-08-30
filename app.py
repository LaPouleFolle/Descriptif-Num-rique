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
        st.write("Bienvenue sur mon site personnel. Spécialisé en modélisation de données, Business Intelligence et analyse décisionnelle, je conçois des solutions orientées performance.")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        cv_path = "assets/Mon cv pro -cdi.pdf"
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
            <h3>Bases de Données & ETL</h3>
            <ul>
                <li><b>SQL avancé :</b> PostgreSQL, Oracle, Sybase</li>
                <li><b>Modélisation :</b> Relationnelle & dimensionnelle (schéma en étoile)</li>
            </ul>
        </div>
        
        <div class='section-card'>
            <h3>Business Intelligence & Dataviz</h3>
            <ul>
                <li>SAS Visual Analytics, Power BI</li>
                <li>Apache Superset, Tableau, Excel</li>
            </ul>
        </div>
        
        <div class='section-card'>
            <h3>Programmation & Analyse</h3>
            <ul>
                <li>SAS Viya</li>
                <li>Python (Pandas, NumPy, Matplotlib)</li>
                <li>R</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_b:
        st.markdown("""
        <div class='section-card'>
            <h3>Statistiques & Data Science</h3>
            <ul>
                <li>Statistiques descriptives & inférentielles</li>
                <li>Régressions, Classification, Clustering</li>
            </ul>
        </div>
        
        <div class='section-card'>
            <h3>Qualité & Méthodes</h3>
            <ul>
                <li>Documentation technique & procédures qualité</li>
                <li>Gouvernance des données, Traitement de demandes ad hoc</li>
                <li>Vulgarisation décisionnelle</li>
            </ul>
        </div>
        
        <div class='section-card'>
            <h3>Gestion de projet</h3>
            <ul>
                <li>Pilotage et structuration de projets data</li>
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