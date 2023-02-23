import pandas as pd
import numpy as np
# import pygal
# # from project_module import project

# def main():
#     """ Main function """
#     df = pd.read_csv('vgsales.csv')
#     create_chart(df)

# def create_chart(df):
#     """ For creating chart """
#     data = np.array(df.groupby('Genre', as_index=False).count()[['Genre', 'Rank']]).tolist()

#     chart = pygal.Pie()

#     for i in data:
#         chart.add(i[0], [{'value': i[1], 'label': '{:.2f}%'.format(100*i[1]/sum([j[1] for j in data]))}])

#     chart.legend_at_bottom = True
#     chart.legend_box_size = 16
#     # chart.render_to_file('overview_genre.svg')

# main()

import pandas as pd
import matplotlib.pyplot as plt

# creating dataframe
df = pd.read_csv('vgsales.csv')

# plot a Pie Chart for Registration Price column with label Car column
plt.pie(df["Genre"])
plt.show()