import streamlit as st

st.set_page_config(page_title="Eng. Luis Fernando Saboia", layout="wide")
st.markdown("<h1 style='text-align: center;'>Eng. Luis Fernando Saboia</h1>", unsafe_allow_html=True)
st.divider()

# =============== SIDEBAR =============== #
with st.sidebar:
    st.image('eu.jpeg')
    st.link_button("Linkedin", "www.linkedin.com/in/luis-fernando-saboia-369503115", use_container_width=True)
    st.text('📧 lfernandolsj@gmail.com')
    st.text('📞 +55 85 98809-7420')

tab1, tab2 = st.tabs(['Resume', 'Skiils and Experiences'])

with tab1:
# =============== ABOUT ME =============== #
    st.subheader('About me')
    summary_text = """
    Throughout my career, I have developed expertise in structuring and analyzing complex data, statistical modeling, and creating interactive visualization dashboards. My results-oriented approach and advanced technical skills allow me to extract value from data by identifying patterns and trends that drive strategic decision-making.

    I have worked on various challenging projects, leading multidisciplinary teams and collaborating with stakeholders to define requirements and deliver customized solutions. Additionally, I have experience in developing predictive models and machine learning algorithms, using languages such as Python and R, and implementing them in production environments. My key skills include:

    - Data Analysis and BI: Data transformation, cleaning, and structuring; creation of interactive dashboards and reports; interpretation and communication of results.
    - Languages and Tools: Python, R, SQL, Tableau, Power BI, advanced Excel.
    - Statistical Modeling: Linear regression, time series analysis, clustering, decision trees, logistic regression models.
    - Machine Learning: Development of predictive models, classification algorithms, recommendation, and anomaly detection.

    I am always seeking continuous learning and stay updated with the latest trends and advancements in the field of data analysis. I am an effective communicator and possess interpersonal skills that enable me to work in teams and collaborate on complex projects.
    """

    # Exibindo o texto com alguns pontos destacados em uma caixa de info
    st.info(summary_text)
    st.divider()

    # =============== EDUCATION =============== #
    st.subheader('Education')
    education_text = """
    - Bachelor's degree in Metallurgical Engineering: Federal University of Ceará (UFC);
    - MBA in Project Management: Estácio de Sá University.
    """
    st.info(education_text)

with tab2:
    # =============== EXPERIENCE =============== #
    def experiences(company, time, country, description):
        st.subheader(company)
        st.write(time)
        st.write(country)
        st.info(description)

    experience_totvs = """
    - Development of web applications for data analysis using Python;
    - Responsible for data analysis of opportunities, forecasting, and sales;
    - Assisting the Marketing and Sales team with data for creating better strategies.
    - Statistical modeling;
    - Data processing and transformation (ETL);
    - Data analysis using Power BI, R, and Python;
    - Interpretation of data, discovering patterns and trends, using exploration techniques, visualization, and storytelling;
    """

    experience_outcome = """
    - Development and maintenance of databases;
    - Database creation;
    - Modification and updating;
    - Creation of functions, triggers, views, and queries;
    - Proposal of improvements;
    - Importation of tables.
    - Data handling for inclusion in the database.
    - Process automation using Power Automate;
    - Data analysis using Power BI, R, and Python;
    - Interpretation of data, discovering patterns and trends, using exploration techniques, visualization, and storytelling;
    - Agile management with SCRUM.
    """

    experience_delta = """
    - Specialist in industrial strategies;
    - Database (SQL Server) querying for5 the creation of management reports;
    - Statistical modeling;
    - Data processing and transformation (ETL);
    - Regular contact with the IT Manager for new projects and improvements;
    - Preparation of Power BI dashboards, reports, and technical reports;
    - Use of Minitab software for statistical analysis assistance;
    - Author and executor of projects of extreme financial significance for the company, especially during peak pandemic periods where strategies were vital to the company's health;
    - Author and executor of machinery construction projects;
    - Manager of Production, Production Planning and Control (PCP), Quality, Laboratory, Research and Development (P&D), and Maintenance teams;
    - Partnerships with Universities for the selection of new projects and talents;
    - Conducted internal courses such as Applied Mathematics to Production, Basic Statistics for Quality Management, Physical Metallurgy of Ferrous Alloys, Metal Corrosion, and Welding Technology.
    """

    experience_marix = """
    - Creation of the material input and output system (Warehouse and Dispatch);
    - Data analysis using Excel as the primary creation tool;
    - Development and presentation of management reports and technical reports for both the Board of Directors and sales representatives;
    - Internal and external training on product technical details;
    - Author of product improvement projects and manufacturing processes;
    - Negotiation with suppliers.
    """
    experiences("TOTVS S.A - Senior Data Analyst", "Oct 2023 - Present", "Joinville, Santa Catarina, Brasil · Remote", experience_totvs)

    experiences("Outcome - Business Solutions - Senior Data Analyst", "Jan 2023 - Oct 2023", "Fortaleza, Ceará, Brasil · Remote", experience_outcome)

    experiences("Delta Artigos Escolares - Senior Data Analyst", "Feb 2015 - May 2022", "Pindoretama, Ceará, Brasil · Remote", experience_delta)

    experiences("Marix Indústria e Comércio de Ferragens S/A - Industrial Manager", "Jan 2014 - Feb 2015", "Eusébio, Ceará, Brasil · Remote", experience_marix)
    
    st.divider()

    # =============== SKILLS =============== #
    st.subheader('Skiils')
    column1, column2, column3 = st.columns(3)
    
    skill_python = """
    - Python: 2 - 3 years
    """
    skill_pbi = """
    - Power BI: 7 - 8 years
    """
    skill_storytelling = """
    - Storytelling: 7 - 8 years
    """
    skill_sql = """
    - SQL: 3 - 4 years
    """
    skill_english = """
    - English: Intermediary
    """
    skill_statistical = """
    - Statistical Data Analysis: 7 - 8 years
    """

    with column1:
        st.info(skill_python)
        st.info(skill_pbi)
    
    with column2:
        st.info(skill_storytelling)
        st.info(skill_sql)
    
    with column3:
        st.info(skill_english)
        st.info(skill_statistical)
