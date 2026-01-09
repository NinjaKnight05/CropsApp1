import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import base64 

st.set_page_config(page_title='Crops Analysis',page_icon="🌽")
menu= option_menu(menu_title='', options=['Home','Analysis','Contact'], icons=['house-fill','info-square-fill','phone-fill','book-fill'], orientation='horizontal')

if menu=='Home':
    st.title('Reliable Crop Supply for Retailers & Bulk Buyers')
    video="https://www.pexels.com/download/video/1649831/"
    components.html( 
        f"""
        <video autoplay muted loop playsline width="100%">
            <source src="{video}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        """,
        height=400,
     )
    st.write('Harvesting machines play a crucial role in modern agriculture, significantly enhancing the efficiency and speed of crop collection. From large-scale farms to smaller operations, various types of harvesting equipment are designed to suit different crops and farming practices. In this blog, we’ll explore the different types of harvesting machines and their specific uses. Harvesting includes reaping or cutting, threshing or sifting grains from the chaff. Harvesting done with hands is a very time-consuming and tiring task. In addition, one needs to take extra care while collecting crops as fragile crops can be accidentally ignored and crushed. Also, working long hours in the field has its own problems, as farmers must work even in bad weather conditions. With the most adaptable harvesting machinery, the harvesting process can become less tiring and more time-saving and productive. Although there is no fixed classification of harvesting machines, here are few types used widely in farming.')
    st.title('-------------About Farmers--------------')
    st.image("https://www.openaccessgovernment.org/wp-content/uploads/2021/02/dreamstime_xxl_183417536.jpg")
   
    st.write("India is a country of farmers. About 70 to 80 percent of the population is still directly or indirectly dependent on agriculture, That is why a great country like India is known as an agricultural country in the world. Farmer is an important part of our life, Indian farmer fulfills the basic needs of 125 crore people in the country. Farmers are most important in terms of the development of the nation. Farmers are the backbone of our country and society, on whose strength our economy stands.")

    st.title('< < < < Facts > > > > ')   
    st.subheader('wheat')
    st.write('one of the oldest and most important cereal crops, providing essential nutrients and serving as a staple food for billions worldwide.')
    st.write('Wheat is a stout grass of medium to tall height. Its stem is jointed and usually hollow, forming a straw. There can be many stems on one plant. It has long narrow leaves, their bases sheathing the stem, one above each joint. At the top of the stem is the flower head, containing some 20 to 100 flowers.')

    st.image("https://www.artchive.com/wp-content/uploads/2024/04/Wheat-Threshing-Ancient-Egypt-c.1422-c.1411-BC-.jpg")

    st.subheader('Rice')
    st.write('Staple Food: Rice is a primary food source for more than 3.5 billion people, especially in Asia, where it forms the basis of many traditional dishes. It provides essential carbohydrates and energy. Nutritional Value: Brown rice is more nutritious than white rice, retaining its bran and germ, which provide fiber, vitamins, and minerals. Rice is naturally gluten-free, making it suitable for those with gluten intolerance.')

    st.image('https://i0.wp.com/herbaria3.org/wp-content/uploads/2021/03/iiif-service_asian_lcnclscd_2014514379_1A001_05b06a-3390x490x2997x3735-866x-0-default.jpg?w=866&ssl=1')
    
    st.subheader('Corn')
    st.write('Maize (/meɪz/; Zea mays), also known as corn in North American English, is a tall stout grass that produces cereal grain. The leafy stalk of the plant gives rise to male inflorescences or tassels which produce pollen, and female inflorescences called ears')
    st.image('https://tse4.mm.bing.net/th/id/OIP.bG8LtZ9zce2tUXH9PAJqRgHaFi?rs=1&pid=ImgDetMain&o=7&rm=3')

    st.subheader('Ancient Time Harvesting')
    st.image('https://static.wixstatic.com/media/6a4453_a42a668a82074c4897fd80b20886b224~mv2.jpg/v1/fill/w_980,h_412,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/6a4453_a42a668a82074c4897fd80b20886b224~mv2.jpg')
    st.write('Ancient harvesting and processing methods were primarily manual labor with simple tools. Early societies relied on hands, sickles, and scythes fashioned from stone, bone, or wood to cut crops at maturity. This method allowed for selective harvesting and minimal wastage. Crops such as grains were gathered through gathering by hand or using rudimentary tools to ensure only the ripe produce was collected. The use of natural elements, like the sun and wind, aided in drying and preserving harvested crops. These basic techniques were vital for early agriculture, as they maximized resource efficiency with limited technology.')

    st.write('')
    st.title('History') 
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/KITLV_40091_-_Kassian_C%C3%A9phas_-_Relief_of_the_hidden_base_of_Borobudur_-_1890-1891.jpg/600px-KITLV_40091_-_Kassian_C%C3%A9phas_-_Relief_of_the_hidden_base_of_Borobudur_-_1890-1891.jpg')

    
    col3,col4=st.columns(2)
    with col3:
       st.write('')
       st.write('Agriculture began independently in different parts of the globe, and included a diverse range of taxa. At least eleven separate regions of the Old and New World were involved as independent centers of origin. The development of agriculture about 12,000 years ago changed the way humans lived. They switched from nomadic hunter-gatherer lifestyles to permanent settlements and farming Wild grains were collected and eaten from at least 104,000 years ago. However, domestication did not occur until much later. The earliest evidence of small-scale cultivation of edible grasses is from around 21,000 BC with the Ohalo II people on the shores of the Sea of Galilee. By around 9500 BC, the eight Neolithic founder crops – emmer wheat, einkorn wheat, hulled barley, peas, lentils, bitter vetch, chickpeas, and flax – were cultivated in the Levant.[4] Rye may have been cultivated earlier, but this claim remains controversial.')

    with col4:
       st.title('')
       st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Maler_der_Grabkammer_des_Sennudem_001.jpg/960px-Maler_der_Grabkammer_des_Sennudem_001.jpg')

    st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0e1117;
        color: #ffffff;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        z-index: 100;
    }
    </style>

    <div class="footer">
        © 2026 Coder Roots | Built with Tobi
    </div>
    """,
    unsafe_allow_html=True
)

elif menu=='Analysis':
     
     st.title('ALL STATES 2026 CROPS SALES🌾')
     st.subheader('Analysis🧠')
     df=pd.read_csv('corn.csv')
     df.columns=df.columns.str.strip()

     st.write(df)
     # show=df["Commodity Group"].unique()
     # st.write(show)
     # res_index=df.loc[:,"Commodity Group"].value_counts().index

     with st.sidebar:
       selected_res = st.selectbox('Select', options=df['Commodity Group'].unique())
       df_selected = df[df['Commodity Group'] == selected_res]
     
     # st.write(df_selected1)
     st.subheader('3D View Of Stocks')
     chart1=px.scatter_3d(df_selected,x='Commodity',y='Quantity',z='Commodity Group',color="Commodity")
     st.plotly_chart(chart1)
     
     st.write(df_selected)
     
     st.subheader('Total Stock in Cold-Store')
     chart0=px.pie(df,names='Commodity',values='Quantity')
     st.plotly_chart(chart0)

     st.subheader('Price Of Corps On 1 Jan 2026')
     chart2=px.bar(df_selected,x="Commodity",y="Price 0",color='Arrived Material 1')
     st.plotly_chart(chart2)

     st.subheader('Price Of Corps On 2 Jan 2026')
     chart4=px.bar(df_selected,x="Commodity",y="Price 1",color="Arrival Material 2")
     st.plotly_chart(chart4)

     st.subheader('Price Of Corps On 3 Jan 2026')
     chart5=px.bar(df_selected,x='Commodity',y='Price 2',color="Arrival Material 3" )
     st.plotly_chart(chart5)
     
     st.subheader('New Arrived Material')
     chart3=px.line(df_selected,x="Commodity",y="Total Arrival")
     st.plotly_chart(chart3)

     
     with open('lst.jpg','rb') as f:
      file=f.read()
      img= base64.b64encode(file).decode()
     css=f"""
          <style>
           [data-testid="stAppViewContainer"]{{
            background-image:url('data:image/jpg;base64,{img}');
            background-size:cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
       """
     st.markdown(css, unsafe_allow_html=True)

elif menu == 'Contact':
    st.title("CONTACT US 👾")
    import sqlite3

    conn = sqlite3.connect("contacts.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        name TEXT,
        email TEXT,
        phone TEXT,
        message TEXT
    )
    """)
    conn.commit()

    with st.form(key='contact'):
        name1 = st.text_input('Name', max_chars=30, placeholder='Name...')
        email = st.text_input('Email', placeholder='Your Email...')
        phone = st.text_input("Phone Number", placeholder="+91...")
        message = st.text_area('Message', placeholder='Write your message...')
        btn1 = st.form_submit_button('Send')

    if btn1:
        if not name1 or not email or not message:
            st.error("Name, Email and Message are required.")
        else:
            c.execute(
                "INSERT INTO contacts VALUES (?, ?, ?, ?)",
                (name1, email, phone, message)
            )
            conn.commit()
            st.success("✅ Message sent successfully! We’ll contact you soon.")

    conn.close()


