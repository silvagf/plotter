# import pandas as pd
# import plotly.express as px

# artefatos = pd.read_excel('Database verdadeira.xlsx')


# fig = px.scatter_3d(artefatos, x='x', y='y', z='z', symbol='Material', color='Material',
#             color_discrete_sequence=['indianred', 'darkturquoise', 'dimgray', 'black', 'red', 'orange'],
#                     symbol_sequence=['circle','diamond','cross','square','x','circle-open'])

# fig.update_layout(scene_aspectmode='manual', scene_aspectratio = dict(x=5, y=1, z=0.4), title_text = 'RS-TQ-141')
# fig.update_layout(
#     scene = dict(
#         xaxis = dict(nticks=50, range=[0,2500],),
#                      yaxis = dict(nticks=7, range=[0,500],),
#                      zaxis = dict(nticks=3, range=[-220,0],)))

# fig.update_layout(legend=dict(title_font_family="Arial",
#                               font=dict(size= 24)))

# fig.show()
# fig.write_html('/home/v/Desktop/pato/arqueologia/htmls/plot_rs-tq-141.html')


# import pandas as pd
# import plotly.express as px

# def read_excel_file(file_path):
#     # Função para ler o arquivo xlsx e retornar um dataframe
#     artefatos = pd.read_excel(file_path)
#     return artefatos

# def generate_plotly_html(df):
#     # Função para gerar o plotly e salvar em um arquivo html
#     fig = px.scatter_3d(df, x='x', y='y', z='z', symbol='Material', color='Material',
#             color_discrete_sequence=['indianred', 'darkturquoise', 'dimgray', 'black', 'red', 'orange'],
#                     symbol_sequence=['circle','diamond','cross','square','x','circle-open'])

#     fig.update_layout(scene_aspectmode='manual', scene_aspectratio = dict(x=5, y=1, z=0.4), title_text = 'RS-TQ-141')
#     fig.update_layout(
#         scene = dict(
#             xaxis = dict(nticks=50, range=[0,2500],),
#                          yaxis = dict(nticks=7, range=[0,500],),
#                          zaxis = dict(nticks=3, range=[-220,0],)))

#     fig.update_layout(legend=dict(title_font_family="Arial",
#                                   font=dict(size= 24)))

#     fig.show()
#     fig.write_html('/home/v/Desktop/pato/arqueologia/plotter/htmls/plot_rs-tq-141.html')

# file_path = 'Database verdadeira.xlsx'
# df = read_excel_file(file_path)
# generate_plotly_html(df)

##################################################################################################

import pandas as pd
import plotly.express as px
from plotly.offline import plot
import time
import os

timestamp = time.strftime('%d-%m-%Y(@%H:%M:%S)')

def read_excel_file(file_path):
    # Função para ler o arquivo xlsx e retornar um dataframe
    artefatos = pd.read_excel(file_path)
    return artefatos

def ask_plot_option():
    while True:
        print("Escolha uma das opções abaixo:")
        print("1 - Plotar uma única sondagem")
        print("2 - Plotar mais de uma sondagem")
        print("3 - Plotar a área total da escavação")
        plot_option = input("Digite o número correspondente à opção escolhida: ")
        if plot_option in ['1', '2', '3']:
            return plot_option
        else:
            print("Opção inválida. Por favor, digite '1', '2' ou '3'.")

def generate_plotly_html(df, option):
    
    html_dir = "htmls"
    if not os.path.exists(html_dir):
        os.makedirs(html_dir)

    if option == '1':
        quadrante = input("Digite o número do quadrante que deseja plotar: ")
        sondagem = input("Digite o número da sondagem que deseja plotar: ")
        filtered_df = df.loc[(df['Quadrante'] == quadrante) & (df['Sondagem'] == sondagem), :]
        fig = px.scatter_3d(filtered_df, x='x', y='y', z='z', symbol='Material', color='Material',
                            color_discrete_sequence=['indianred', 'darkturquoise', 'dimgray', 'black', 'red', 'orange'],
                            symbol_sequence=['circle','diamond','cross','square','x','circle-open'], hover_data=df.columns)
        fig.update_traces(marker_size=10)
        fig.update_layout(title_text=f"Sondagem {sondagem} no quadrante {quadrante}")
        fig.update_layout(scene=dict(zaxis=dict(nticks=3, range=[-220, 0], autorange=False)))
        fig.show()
        return plot(fig, output_type='div')



    
    elif option == '2':
        return None
   
    elif option == '3':
        fig = px.scatter_3d(df, x='x', y='y', z='z', symbol='Material', color='Material',
                            color_discrete_sequence=['indianred', 'darkturquoise', 'dimgray', 'black', 'red', 'orange'],
                            symbol_sequence=['circle','diamond','cross','square','x','circle-open'], hover_data=df.columns)
        fig.update_layout(scene_aspectmode='manual', scene_aspectratio = dict(x=5, y=1, z=0.4), title_text = 'RS-TQ-141')
        fig.update_layout(scene=dict(xaxis=dict(nticks=50, range=[0,2500]), yaxis=dict(nticks=7, range=[0,500]), zaxis=dict(nticks=3, range=[-220,0])))
        fig.update_layout(legend=dict(title_font_family="Arial", font=dict(size= 24)))
        fig.show()
        file_name = f'plot_total_rs-tq-141_{timestamp}.html'
        fig.write_html(os.path.join(html_dir, file_name))


def plote():
    plot_option = ask_plot_option()
    file_path = 'Database verdadeira.xlsx'
    df = read_excel_file(file_path)
    df['Quantia'].fillna(1, inplace=True)
    df.fillna('*NÃO CONSTA*', inplace=True)
    generate_plotly_html(df, plot_option)

plote()