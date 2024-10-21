import pandas as pd
from datetime import datetime, timedelta
import random
import matplotlib.pyplot as plt


import plotly.graph_objs as go
import plotly.io as pio
import base64


colors = ['rgb(229,57,69)', 'rgb(237,173,73)', 'rgb(51,118,189)', 'rgb(0,121,140)', 'rgb(82,73,156)',
          'rgb(229,57,69)', 'rgb(237,173,73)', 'rgb(51,118,189)', 'rgb(0,121,140)', 'rgb(82,73,156)',
          'rgb(229,57,69)', 'rgb(237,173,73)', 'rgb(51,118,189)', 'rgb(0,121,140)', 'rgb(82,73,156)',
          'rgb(229,57,69)', 'rgb(237,173,73)', 'rgb(51,118,189)', 'rgb(0,121,140)', 'rgb(82,73,156)',
          ][::-1]

gender_colors = ['rgb(233, 30, 99)', 'rgb(41, 98, 255)']

single_color = 'rgb(92,186,230)'
single_color_dark = 'rgb(70, 139, 171)'



# def sort_months(data):
   
#     months_order = ["January", "February", "March", "April", "May", "June",
#                     "July", "August", "September", "October", "November", "December"]
#     months_order = ["Ocak", "Subat", "Mart", "Nisan", "Mayis", "Haziran", "Temmuz", "Agustos", "Eylül", "Ekim", "Kasim", "Aralik"]

#     # Sözlüğü DataFrame'e dönüştürme
#     df = pd.DataFrame(list(data.items()), columns=['month', 'count'])

#     # Ay sütununu kategorik bir sütun olarak ayarlama ve sıralı bir şekilde ayarlanmasını sağlama
#     df['month'] = pd.Categorical(df['month'], categories=months_order, ordered=True)

#     # DataFrame'i ay sütununa göre sıralama
#     sorted_df = df.sort_values('month')
#     sorted_df.reset_index(drop=True, inplace=True)

#     return sorted_df


def sort_months(series):
    # Ay adları ve sıralama için bir sözlük oluştur
    month_order = {
        'Ocak': 1, 'Subat': 2, 'Mart': 3, 'Nisan': 4, 'Mayis': 5, 'Haziran': 6,
        'Temmuz': 7, 'Agustos': 8, 'Eylül': 9, 'Ekim': 10, 'Kasim': 11, 'Aralık': 12
    }

    # Seriyi ay sırasına göre sırala
    sorted_series = series.reindex(sorted(series.index, key=lambda x: month_order[x]))
    return sorted_series


def image_to_ascii(fig):
    img_bytes = pio.to_image(fig, format="png")
    return base64.b64encode(img_bytes).decode("ascii")

def daily_chart(data):
    days_of_week_ordered = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
    daily_data = data["day_of_week"].value_counts().reindex(days_of_week_ordered)

    
    data1 = go.Bar(x=daily_data.index, y=daily_data, marker=dict(color=single_color, line=dict(color=single_color_dark, width=2))
)
    fig = go.Figure(data=data1)
    fig.update_layout(
        margin=dict(l=70, r=30, t=45, b=0),
        xaxis_tickangle=-45,
        title={"text": "Günlere Göre Ziyaretçi Sayısı", "x": 0.5},
        title_font_size=30, 
        xaxis_tickfont_size=18, 

        plot_bgcolor='white', 

        yaxis=dict(
            title_font_size=18,
            tickfont_size=24,
            showgrid=True, 
            gridcolor='rgb(200,200,200)' 
        ),

    )  # template="simple_white"
    return fig

def weekly_chart(data):
    daily_data = data["week_of_month"].value_counts()
    x_labels = [f"{i}. Hafta" for i in range(1, 6)]

 

    data1 = go.Bar(x=x_labels, y=daily_data, marker=dict(color=single_color, line=dict(color=single_color_dark, width=2)))
    fig = go.Figure(data=data1)
    fig.update_layout(
        margin=dict(l=30, r=70, t=45, b=0),
        xaxis_tickangle=-45,
        title={"text": "Haftalara Göre Ziyaretçi Sayısı", "x": 0.5},
        title_font_size=30, 
        xaxis_tickfont_size=18,  

        plot_bgcolor='white', 

        yaxis=dict(
            title_font_size=18,
            tickfont_size=24,
            showgrid=True, 
            gridcolor='rgb(200,200,200)' 
        ),

    )  
    return fig

def monthly_chart(data):
    monthly_data = data["month_of_year"].value_counts()
    
    month_names = {
        1: "Ocak",
        2: "Subat",
        3: "Mart",
        4: "Nisan",
        5: "Mayis",
        6: "Haziran",
        7: "Temmuz",
        8: "Agustos",
        9: "Eylül",
        10: "Ekim",
        11: "Kasim",
        12: "Aralık",
    }

    monthly_data.index = monthly_data.index.map(month_names)
    monthly_data = sort_months(monthly_data)


   

    data1 = go.Bar(x=monthly_data.index , y=monthly_data)
    fig = go.Figure(data=data1)

    fig.update_layout(
        width=700,
        height=300,
        margin=dict(l=0, r=0, t=30, b=0),
        xaxis_tickangle=-45,
        title={"text": "Aylara Göre Ziyaretçi Sayısı", "x": 0.5},

        plot_bgcolor='white', 
    )  

    return fig


def daily_chart_gender(data):
    days_of_week_ordered = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

    daily_data = data.groupby(['day_of_week', 'gender']).size().unstack()
    daily_data = daily_data.reindex(days_of_week_ordered)
    # colors = ['rgb(92, 186, 230)', 'rgb(92, 156, 204)']  

    fig = go.Figure()
    for i, gender in enumerate(daily_data.columns):
        fig.add_trace(go.Bar(x=daily_data.index, y=daily_data[gender], name=gender, marker_color=gender_colors[i]))

    fig.update_layout(
        barmode='group',
        margin=dict(l=70, r=30, t=45, b=0),
        xaxis_tickangle=-45,
        title={'text': 'Haftanın Günlerine Göre Cinsiyet Dağılımı', 'x': 0.5},
        legend=dict(
            x=0.5, y=-0.40,
            orientation="h",
            xanchor="center",
            yanchor="bottom",
            font=dict(size=30)  

        ),
        title_font_size=30, 
        xaxis_tickfont_size=18,
        plot_bgcolor='white',  

        yaxis=dict(
            title_font_size=18,
            tickfont_size=24,
            showgrid=True, 
            gridcolor='rgb(200,200,200)' 
        ),
    )

    return fig


def weekly_chart_gender(data):
    weekly_data = data.groupby(['week_of_month', 'gender']).size().unstack()
    x_labels = [f"{i}. Hafta" for i in range(1, 6)]

    fig = go.Figure()
    for i, gender in enumerate(weekly_data.columns):
        fig.add_trace(go.Bar(x=x_labels, y=weekly_data[gender], name=gender, marker_color=gender_colors[i]))

    fig.update_layout(
        barmode='group',
        margin=dict(l=30, r=70, t=45, b=0),
        xaxis_tickangle=-45,
        title={'text': 'Haftalık Cinsiyet Dağılımı', 'x': 0.5},

        legend=dict(
                    x=0.5, y=-0.40,
                    orientation="h",
                    xanchor="center",
                    yanchor="bottom",
                    font=dict(size=30)              

                ),
        title_font_size=30, 
        xaxis_tickfont_size=18,
        plot_bgcolor='white', 

        yaxis=dict(
            title_font_size=18,
            tickfont_size=24,
            showgrid=True, 
            gridcolor='rgb(200,200,200)' 
        ),
        )

    return fig

def monthly_chart_gender(data):
    monthly_data = data.groupby(['month_of_year', 'gender']).size().unstack()
    month_names = ["Ocak", "Subat", "Mart", "Nisan", "Mayis", "Haziran", "Temmuz", "Agustos", "Eylül", "Ekim", "Kasim", "Aralik"]

    month_names = {
        1: "Ocak",
        2: "Subat",
        3: "Mart",
        4: "Nisan",
        5: "Mayis",
        6: "Haziran",
        7: "Temmuz",
        8: "Agustos",
        9: "Eylül",
        10: "Ekim",
        11: "Kasim",
        12: "Aralık",
    }

    monthly_data.index = monthly_data.index.map(month_names)
    monthly_data = sort_months(monthly_data)
    # print(monthly_data)

    fig = go.Figure()
    for i, gender in enumerate(monthly_data.columns):
        fig.add_trace(go.Bar(x=monthly_data.index, y=monthly_data[gender], name=gender, marker_color=gender_colors[i]))

    fig.update_layout(
        width=700,
        height=300,
        margin=dict(l=0, r=0, t=30, b=0),
        title={"text": "Aylık Cinsiyet Dağılımı", "x": 0.5},
        xaxis_tickangle=-45,
        plot_bgcolor='white', 

        legend=dict(
                x=0.5, y=-0.40,
                orientation="h",
                xanchor="center",
                yanchor="bottom",
                font=dict(size=12)  
            ),

        # yaxis=dict(
        #     title_font_size=18,
        #     tickfont_size=24,
        #     showgrid=True, 
        #     gridcolor='rgb(200,200,200)' 
        # ),
        
    )  


    return fig

def hourly_chart(data):
    hourly_data = data['hour_of_day'].value_counts().sort_index()
    hour_names = [f"{i:02d}:00" for i in range(1, 25)]

    fig = go.Figure(data=go.Bar(x=hour_names, y=hourly_data))

    fig.update_layout(
        title={'text': 'Saatlere Göre Dağılım', 'x': 0.5},
        width=700,
        height=300,
        xaxis_tickangle=-45,
        margin=dict(l=0, r=0, t=30, b=0),

        plot_bgcolor='white', 


        # yaxis=dict(
        #     title_font_size=18,
        #     tickfont_size=24,
        #     showgrid=True, 
        #     gridcolor='rgb(200,200,200)' 
        # ),
    )
    return fig

def hourly_gender_chart(data):
    hourly_gender_data = data.groupby(['hour_of_day', 'gender']).size().unstack()
    hour_names = [f"{i:02d}:00" for i in range(1, 25)]

    fig = go.Figure()
    for i, gender in enumerate(hourly_gender_data.columns):
        fig.add_trace(go.Bar(x=hour_names, y=hourly_gender_data[gender], name=gender, marker_color=gender_colors[i]))

    fig.update_layout(
        title={'text': 'Saatlere Göre Cinsiyet Dağılımı', 'x': 0.5},
        width=700,
        height=300,
        barmode='group',
        margin=dict(l=0, r=0, t=30, b=0),
        xaxis_tickangle=-45,

        plot_bgcolor='white', 

        legend=dict(
                    x=0.5, y=-0.40,
                    orientation="h",
                    xanchor="center",
                    yanchor="bottom",
                    font=dict(size=12)  
                ),

        # yaxis=dict(
        #     title_font_size=18,
        #     tickfont_size=24,
        #     showgrid=True, 
        #     gridcolor='rgb(200,200,200)' 
        # ),
    )

    return fig

def monthly_day_distribution_count(data):
    days_of_week_ordered = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
    month_names = ["Ocak", "Subat", "Mart", "Nisan", "Mayis", "Haziran", "Temmuz", "Agustos", "Eylül", "Ekim", "Kasim", "Aralik"]

    data['day_of_week'] = pd.Categorical(data['day_of_week'], categories=days_of_week_ordered, ordered=True)

    grouped_data = data.groupby(['month_of_year', 'day_of_week']).size().reset_index(name='count')

    fig = go.Figure()
    i = 0
    for month in sorted(grouped_data['month_of_year'].unique()):
        month_data = grouped_data[grouped_data['month_of_year'] == month]
        fig.add_trace(go.Bar(x=month_data['day_of_week'], y=month_data['count'], name=month_names[month-1], marker_color=colors[i]))
        i += 1

    fig.update_layout(
        title={'text': 'Aylara Göre Günlerin Sayım Dağılımı', 'x': 0.5},
        width=700,
        height=300,
        barmode='group',
        margin=dict(l=0, r=0, t=30, b=0),
        xaxis_tickangle=-45,
        plot_bgcolor='white'
    )

    return fig





def monthly_day_distribution_average(data):
    days_of_week_ordered = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
    month_names = ["Ocak", "Subat", "Mart", "Nisan", "Mayis", "Haziran", "Temmuz", "Agustos", "Eylül", "Ekim", "Kasim", "Aralik"]

    data['day_of_week'] = pd.Categorical(data['day_of_week'], categories=days_of_week_ordered, ordered=True)

    grouped_data = data.groupby(['month_of_year', 'day_of_week'])['confidence'].mean().reset_index()

    fig = go.Figure()
    i = 0
    for month in sorted(grouped_data['month_of_year'].unique()):
        month_data = grouped_data[grouped_data['month_of_year'] == month]
        fig.add_trace(go.Bar(x=month_data['day_of_week'], y=month_data['confidence'], name=month_names[month-1], marker_color=colors[i]))
        i += 1

    fig.update_layout(
        title={'text': 'Aylara Göre Günlerin Ortalaması Dağılımı', 'x': 0.5},
        width=700,
        height=300,
        barmode='group',
        margin=dict(l=0, r=0, t=30, b=0),
        xaxis_tickangle=-45,
        plot_bgcolor='white'
    )

    return fig





def quarter_pie_chart(data):
    quarter_counts = data['quarter'].value_counts()
    x_labels = ["Q1", "Q2", "Q3", "Q4"]

    fig = go.Figure(data=go.Pie(
        labels=x_labels,
        values=quarter_counts,
        hole=.3,
        textinfo='percent',  
        textfont=dict(size=20, color='white')
        ))

    fig.update_layout(
        title={'text': 'Yılın Çeyreklerine Göre Dağılım', 'x': 0.5},
        plot_bgcolor='white', 

        legend=dict(
                    x=0.5, y=-0.40,
                    orientation="h",
                    xanchor="center",
                    yanchor="bottom",
                    font=dict(size=30)  
                ),

       
    )

    return fig




def gender_distribution_pie_chart(data):
    gender_counts = data['gender'].value_counts()

    fig = go.Figure(data=go.Pie(
        labels=gender_counts.index, 
        values=gender_counts, 
        hole=.3,
        textinfo='percent',  
        textfont=dict(size=20, color='white'),  
        marker=dict(colors=gender_colors)  
    ))
    fig.update_layout(
        title={'text': 'Cinsiyet Dağılımı', 'x': 0.5},
        plot_bgcolor='white',
        legend=dict(
            x=0.5, y=-0.40,
            orientation="h",
            xanchor="center",
            yanchor="bottom",
            font=dict(size=30)  
        ),
    )
    return fig






def heatmap_hour_day(data):
    days_of_week_ordered = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"][::-1]

    grouped_data = data.groupby(['day_of_week', 'hour_of_day']).size().reset_index(name='count')
    heatmap_data = grouped_data.pivot(index='day_of_week', columns='hour_of_day', values='count')

    heatmap_data = heatmap_data.reindex(days_of_week_ordered)

    hour_names = [f"{i:02d}:00" for i in range(1, 25)]

    fig = go.Figure(data=go.Heatmap(
        z=heatmap_data.values,
        x=hour_names,
        y=heatmap_data.index,
        colorscale='Viridis'
    ))

    fig.update_layout(
        title={'text': 'Gün ve Saat Kombinasyonlarına Göre Ziyaretçi Yoğunluğu', 'x': 0.5},
        width=700,
        height=400,
        xaxis_title="Saat",
        xaxis_tickangle=-45,
        
        plot_bgcolor='white', 


    )

    return fig


