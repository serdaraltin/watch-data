from weasyprint import HTML

# import google.generativeai as genai
import openai

import io

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
pd.options.mode.chained_assignment = None

# from ..raport_charts import *
from utils.export.raport_charts import *

def month_size(data):
    return True if data["month_of_year"].value_counts().size > 1 else False

def data_preprocessing(data):
    data = data[data["event_type"] == "enter"]

    data["detection_time"] = pd.to_datetime(data["detection_time"])
    data["day_of_week"] = data["detection_time"].dt.day_name()
    data["week_of_month"] = data["detection_time"].dt.day // 7 + 1
    data["month_of_year"] = data["detection_time"].dt.month
    data["hour_of_day"] = data["detection_time"].dt.hour
    data["quarter"] = data["detection_time"].dt.quarter

    days_translation = {
        "Monday": "Pazartesi",
        "Tuesday": "Salı",
        "Wednesday": "Çarşamba",
        "Thursday": "Perşembe",
        "Friday": "Cuma",
        "Saturday": "Cumartesi",
        "Sunday": "Pazar",
    }

    # gender_name = {0: "male", 1: "female"}




    data["day_of_week"] = data["day_of_week"].map(days_translation)
    # data["gender"] = data["gender"].map(gender_name)

    return data



# def generate_comment(data, prompt):

#     GOOGLE_API_KEY = "AIzaSyBg81xPH7jt0U5IpXatZhOY3d96c1Eyxzs"

#     prompt_content = f"""
#         Veri Analizi Raporu:
#         Veri: {data}
#         İstek: {prompt}
#         Rapor Dili: Keskin ve net ifadeler kullanılacak. 'Görünüyor', 'muhtemelen' gibi belirsiz ifadeler yerine 'olmuştur', 'gerçekleşmiştir' gibi kesin ifadeler tercih edilecek.
#         Uzunluk: Maksimum 300 karakter.
#         Not: Bu metin, bir rapora eklenecek. Analiz, doğrudan ve kesin bilgiler içermelidir.
#         Sonuçları düz yazı olarak yaz. Maddeler halinde bir yazı bulunmasın.
#         """

#     genai.configure(api_key=GOOGLE_API_KEY)

#     model = genai.GenerativeModel('gemini-pro')

#     response = model.generate_content(prompt_content)

#     return response.text

def generate_comment(data, prompt):
    openai.api_key = ""  


    prompt_content = f"""
        Veri Analizi Raporu:
        Veri: {data}
        İstek: {prompt}
        Rapor Dili: Keskin ve net ifadeler kullanılacak. 'Görünüyor', 'muhtemelen' gibi belirsiz ifadeler yerine 'olmuştur', 'gerçekleşmiştir' gibi kesin ifadeler tercih edilecek.
        Uzunluk: Maksimum 300 karakter.
        Not: Bu metin, bir rapora eklenecek. Analiz, doğrudan ve kesin bilgiler içermelidir.
        Sonuçları düz yazı olarak yaz. Maddeler halinde bir yazı bulunmasın.
        """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt_content}
        ],
    )

    return response.choices[0].message["content"]

def create_rapor_pdf(data, branch_name):
    fig1 = daily_chart(data)
    fig2 = weekly_chart(data)
    fig3 = monthly_chart(data)
    fig4 = daily_chart_gender(data)
    fig5 = weekly_chart_gender(data)
    fig6 = monthly_chart_gender(data)
    fig7 = hourly_chart(data)
    fig8 = hourly_gender_chart(data)
    fig9 = monthly_day_distribution_count(data)
    fig10 = monthly_day_distribution_average(data)
    fig11 = quarter_pie_chart(data)
    fig12 = gender_distribution_pie_chart(data)
    fig13 = heatmap_hour_day(data)

    encoded1 = image_to_ascii(fig1)
    encoded2 = image_to_ascii(fig2)

    if month_size(data):
        encoded3 = image_to_ascii(fig3)
    else:
        encoded3 = ""

    encoded4 = image_to_ascii(fig4)
    encoded5 = image_to_ascii(fig5)

    if month_size(data):
        encoded6 = image_to_ascii(fig6)
    else:
        encoded6 = ""


    encoded7 = image_to_ascii(fig7)
    encoded8 = image_to_ascii(fig8)
    encoded9 = image_to_ascii(fig9)
    encoded10 = image_to_ascii(fig10)
    encoded11 = image_to_ascii(fig11)
    encoded12 = image_to_ascii(fig12)
    encoded13 = image_to_ascii(fig13)

    # ! place 1
    month_names = {
            1: "Ocak", 2: "Şubat", 3: "Mart", 4: "Nisan", 5: "Mayıs", 
            6: "Haziran", 7: "Temmuz", 8: "Ağustos", 9: "Eylül", 
            10: "Ekim", 11: "Kasım", 12: "Aralık"
        }
    data["month_of_year"] = data["detection_time"].dt.month.map(month_names)
    days_of_week_ordered = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
    daily_data1 = data["day_of_week"].value_counts().reindex(days_of_week_ordered)
    daily_data2 = data["day_of_week"].value_counts()


    monthly_data = data["month_of_year"].value_counts()
    monthly_data.index = monthly_data.index.map(month_names)

    if month_size(data):
        data_1 = f"{daily_data1.to_dict()}\n{daily_data2.to_dict()}\n{monthly_data.to_dict()}"
    else:
        data_1 = f"{daily_data1.to_dict()}\n{daily_data2.to_dict()}"

    prompt_1 = """
Yukarıda ki veride bir mağazanın belirlenen bir tarih aralığında günlük, haftalık ve aylık ziyaretçi miktarını belirtiyor.
Bunları göz önünde bulundurarak bu verileri hakkında yorum yapar mısın.
"""
    ai_text_1 = generate_comment(data_1, prompt_1)

    # ! place 2
    days_of_week_ordered = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
    daily_data = data.groupby(['day_of_week', 'gender']).size().unstack()
    daily_data = daily_data.reindex(days_of_week_ordered)

    weekly_data = data.groupby(['day_of_week', 'gender']).size().unstack()

    monthly_data = data.groupby(['month_of_year', 'gender']).size().unstack()


    if month_size(data):
        data_2 = f"{daily_data.to_dict()}\n{weekly_data.to_dict()}\n{monthly_data.to_dict()}"
    else:
        data_2 = f"{daily_data.to_dict()}\n{weekly_data.to_dict()}"

    prompt_2 = """
Yukarıda ki veride bir mağazanın belirlenen bir tarih aralığında günlük, haftalık ve aylık ziyaretçi sayısını cinsiyete göre dağılımı var.
Bunları göz önünde bulundurarak bu verileri hakkında yorum yapar mısın.
"""
    ai_text_2 = generate_comment(data_2, prompt_2)


    # ! place 3
    hourly_data = data['hour_of_day'].value_counts().sort_index()
    hourly_gender_data = data.groupby(['hour_of_day', 'gender']).size().unstack()

    data_3 = f"{hourly_data.to_dict()}\n{hourly_gender_data.to_dict()}"
    prompt_3 = """
Yukarıda ki veride bir mağazanın belirlenen bir tarih aralığında 24 saatlik içeriye giren kişi sayısı zamana ve cinsiyete göre dağılımı var..
Bunları göz önünde bulundurarak bu verileri hakkında yorum yapar mısın.
"""
    ai_text_3 = generate_comment(data_3, prompt_3)




    # ! place 4 
    days_of_week_ordered = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

    data['day_of_week'] = pd.Categorical(data['day_of_week'], categories=days_of_week_ordered, ordered=True)

    month_names = {
        1: "Ocak", 2: "Şubat", 3: "Mart", 4: "Nisan", 5: "Mayıs", 
        6: "Haziran", 7: "Temmuz", 8: "Ağustos", 9: "Eylül", 
        10: "Ekim", 11: "Kasım", 12: "Aralık"
    }
    data["month_of_year"] = data["detection_time"].dt.month.map(month_names)

    grouped_data1 = data.groupby(['month_of_year', 'day_of_week']).size()
    grouped_data2 = data.groupby(['month_of_year', 'day_of_week']).size()
    

    data_4 = f"{grouped_data1.to_dict()}\n{grouped_data2.to_dict()}"
    prompt_4 = """
Yukarıda ki veride bir mağazanın belirlenen bir tarih aralığında her ayın haftanın günlerine göre toplam ziyaretçi sayısı ve ortalaması var.
Bunları göz önünde bulundurarak bu verileri hakkında yorum yapar mısın.
"""
    ai_text_4 = generate_comment(data_4, prompt_4)

    


    # print("\n\n\n")
    # print("#"*100)
    # print(data_1)
    # print("#"*100, end="\n\n")
    # print(data_2)
    # print("#"*100, end="\n\n")
    # print(data_3)
    # print("#"*100, end="\n\n")
    # print(data_4)
    # print("#"*100, end="\n\n")

    start_date = data["detection_time"].min().strftime("%Y-%m-%d")
    end_date = data["detection_time"].max().strftime("%Y-%m-%d")

    # start_date = "start"
    # end_date = "stop"

    rapor_date = f"{start_date} - {end_date}"


    with open("utils/export/wd.jpg", "rb") as image_file:
        encoded_logo = base64.b64encode(image_file.read()).decode()

    html_content = (
        """
    <!DOCTYPE html>
    <html>
    <head>
        <title>WD Report</title>
        <style>
            @page {
                margin: 0mm;
            }


            body {
                margin: 0;
                padding: 0px;
                width: 794px;
                height: 1122px;
                font-family: sans-serif;
            }

            .title {
           
                margin-left: 38px;
                margin-top: 50px;
                padding-left: 20px;
                font-size: 30px;
                font-weight: bold;
                display: flex;
            }

            .wd-title {
                padding: 5px 0px;
                font-size: 16px;
                color: #124b68;
                margin-right: 20px;

            }

            .company-title {
                color: #f32170;
                border-left: 4px solid #50b0fa;
                display: flex;
                padding-left: 20px;
            }

            .chart-row {
                display: flex;
                justify-content: center;
                gap: 5px;
                margin-top: 20px;
                padding-top: 40px;
            }


            .chart-container {
                box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
                
            }

            .chart-container img {
                width: 380px;
            }

            .rapor-date {
                right: 0;
                margin-left: auto;
                margin-right: 30px;
                color: #124b68;
            }

            .ai-text-container {
                padding: 30px 60px;
            }

        </style>
        </style>
    </head>

    """
        + f"""

    



        <body>

       

        <div class="title">
         
            <div class="wd-title">    <img src="data:image/jpeg;base64,{encoded_logo}" style="width: 40px; margin-top: 5px;" alt="Örnek Görsel"></div>

            <div class="company-title">{branch_name.upper()} </div>
            
            <div style="color: #124b68; right: 0; margin-left: auto; margin-right: 30px; font-size: 16px;">{rapor_date}</div> 
        
        

        </div>


        <div class="chart-row">
            <div class="chart-container">
                <img src="data:image/png;base64,{encoded1}"  >
            </div>
            <div class="chart-container">
                <img src="data:image/png;base64,{encoded2}"  >
            </div>

        </div>

        <div class="chart-row">
            <div class="chart-container">
                <img style="width: auto; height: auto;" src="data:image/png;base64,{encoded3}"  >
            </div>
        </div>


        <div class="ai-text-container">
            {ai_text_1 }
        </div>

        <div class="chart-row">
            <div class="chart-container">
                <img src="data:image/png;base64,{encoded4}"  >
            </div>
            <div class="chart-container">
                <img src="data:image/png;base64,{encoded5}"  >
            </div>

        </div>

        <div class="chart-row" style="padding-top: 50px">
            <div class="chart-container">
                <img style="width: auto; height: auto;" src="data:image/png;base64,{encoded6}"  >
            </div>
        </div>


        <div class="ai-text-container">
            {ai_text_2 }
        </div>

        <div class="chart-row" style="padding-top: 50px">
            <div class="chart-container">
                <img style="width: auto; height: auto;" src="data:image/png;base64,{encoded7}"  >
            </div>
        </div>

        <div class="chart-row" style="padding-top: 50px">
            <div class="chart-container">
                <img style="width: auto; height: auto;" src="data:image/png;base64,{encoded8}"  >
            </div>
        </div>

        
        <div class="ai-text-container">
            {ai_text_3 }
        </div>

        <div class="chart-row" style="padding-top: 50px">
            <div class="chart-container">
                <img style="width: auto; height: auto;" src="data:image/png;base64,{encoded9}"  >
            </div>
        </div>

        <div class="chart-row" style="padding-top: 50px">
            <div class="chart-container">
                <img style="width: auto; height: auto;" src="data:image/png;base64,{encoded10}" >
            </div>
        </div>

         <div class="ai-text-container">
            {ai_text_4 }
        </div>

        <div class="chart-row">
            <div class="chart-container">
                <img src="data:image/png;base64,{encoded11}"  >
            </div>
            <div class="chart-container">
                <img src="data:image/png;base64,{encoded12}" >
            </div>

        </div>

        <div class="chart-row" style="padding-top: 50px">
            <div class="chart-container">
                <img style="width: auto; height: auto;" src="data:image/png;base64,{encoded13}"  >
            </div>
        </div>

    </body>
    </html>
    """
    )

    # pdf_dosyasi = "output.pdf"

    # HTML(string=html_content).write_pdf(pdf_dosyasi)

    pdf_byte_stream = io.BytesIO()
    HTML(string=html_content).write_pdf(pdf_byte_stream)

    # Bayt akışının başına dönün
    pdf_byte_stream.seek(0)

    return pdf_byte_stream
