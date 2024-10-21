from weasyprint import HTML

import plotly.graph_objs as go
import plotly.io as pio
import base64


data1 = go.Scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13])
fig1 = go.Figure(data1)

data2 = go.Scatter(x=[2, 3, 4, 5], y=[15, 16, 17, 18])
fig2 = go.Figure(data2)

img_bytes1 = pio.to_image(fig1, format='png')
encoded1 = base64.b64encode(img_bytes1).decode('ascii')

img_bytes2 = pio.to_image(fig2, format='png')
encoded2 = base64.b64encode(img_bytes2).decode('ascii')

html_content = '''
<!DOCTYPE html>
<html>
<head>
    <title>PDF Example</title>
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
            border-left: 4px solid #50b0fa;
            margin-left: 38px;
            margin-top: 50px;
            padding-left: 20px;
            font-size: 30px;
            font-weight: bold;

        }

        .wd-title {
            padding: 5px 0px;
            color: #124b68;

        }

        .company-title {
            font-size: 16px;
            color: #f32170;

        }

       .chart-row {
            display: flex;
            justify-content: center;
            gap: 5px;
            margin-top: 20px;
        }


        .chart-container {
            box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
        }
    </style>
    </style>
</head>

''' + f'''

  



    <body>

    <div class="title">
        <div class="wd-title">Watch Data Rapor</div>
        <div class="company-title">KELEBEK MOBİLYA</div>
    </div>

    <div class="chart-row">
        <div class="chart-container">
            <img style="width: 250px;" src="data:image/png;base64,{encoded1}" alt="Plotly Graph 1">
        </div>
        <div class="chart-container">
            <img style="width: 250px;" src="data:image/png;base64,{encoded2}" alt="Plotly Graph 2">
        </div>

        <div class="chart-container">
            <img style="width: 250px;" src="data:image/png;base64,{encoded2}" alt="Plotly Graph 2">
        </div>
    </div>

     


</body>
</html>
'''

pdf_dosyasi = 'export.pdf'

HTML(string=html_content).write_pdf(pdf_dosyasi)

print(f"PDF oluşturuldu: {pdf_dosyasi}")
