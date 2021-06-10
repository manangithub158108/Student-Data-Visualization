# importing the modules
import plotly.express as px;
import pandas as pd;
import plotly.graph_objects as go;

# reading the csv
csv = pd.read_csv('data.csv');

# asking the user about the name of the person
student_id = input('Enter the Student ID =>> ');

# separating the database of the name
df = csv.loc[csv['student_id'] == student_id];
print('the graph of the given person will open...');

# plotting the graph for the erequired person
fig = px.scatter(df, x = df.groupby('level')["attempt"].mean(), 
y = ["Level 1", "Level 2", "Level 3", "Level 4"], size=df.groupby('level')["attempt"].mean());
fig.show();