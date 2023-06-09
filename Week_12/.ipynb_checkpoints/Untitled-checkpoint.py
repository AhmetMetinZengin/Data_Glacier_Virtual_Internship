{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ae23d463",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dash is running on http://127.0.0.1:8050/\n",
      "\n",
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "E:\\Anaconda\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3465: UserWarning:\n",
      "\n",
      "To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "import dash\n",
    "from dash import dcc\n",
    "from dash import html\n",
    "from dash.dependencies import Input, Output\n",
    "from plotly.subplots import make_subplots\n",
    "\n",
    "# Load the dataset\n",
    "df = pd.read_csv('C:/Users/ejot9/Data_Glacier_Virtual_Internship/Week_12/master_data.csv')\n",
    "\n",
    "# Initialize the Dash app\n",
    "app = dash.Dash(__name__)\n",
    "\n",
    "\n",
    "# Age vs. Satisfaction Rate (Scatter Plot)\n",
    "fig1 = px.scatter(df, x='Age', y='Satisfaction Rate', color='Satisfaction Rate',\n",
    "                  title='Age vs. Satisfaction Rate',\n",
    "                  labels={'Age': 'Age', 'Satisfaction Rate': 'Satisfaction Rate'},\n",
    "                  trendline='ols')  # Add a trendline for linear regression\n",
    "\n",
    "# Country vs. Satisfaction Rate (Scatter Plot)\n",
    "fig2 = px.scatter(df, x='Country', y='Satisfaction Rate', color='Satisfaction Rate',\n",
    "                  title='Country vs. Satisfaction Rate',\n",
    "                  labels={'Country': 'Country', 'Satisfaction Rate': 'Satisfaction Rate'})\n",
    "\n",
    "# Education Level vs. Satisfaction Rate (Scatter Plot)\n",
    "fig3 = px.scatter(df, x='Education Level', y='Satisfaction Rate', color='Satisfaction Rate',\n",
    "                  title='Education Level vs. Satisfaction Rate',\n",
    "                  labels={'Education Level': 'Education Level', 'Satisfaction Rate': 'Satisfaction Rate'})\n",
    "\n",
    "# Number of Languages Spoken vs. Satisfaction Rate (Scatter Plot)\n",
    "fig4 = px.scatter(df, x='Number of Languages Spoken', y='Satisfaction Rate', color='Satisfaction Rate',\n",
    "                  title='Number of Languages Spoken vs. Satisfaction Rate',\n",
    "                  labels={'Number of Languages Spoken': 'Number of Languages Spoken', 'Satisfaction Rate': 'Satisfaction Rate'})\n",
    "\n",
    "# Gender vs. Satisfaction Rate (Scatter Plot)\n",
    "fig5 = px.scatter(df, x='Gender', y='Satisfaction Rate', color='Satisfaction Rate',\n",
    "                  title='Gender vs. Satisfaction Rate',\n",
    "                  labels={'Gender': 'Gender', 'Satisfaction Rate': 'Satisfaction Rate'})\n",
    "\n",
    "# Marital Status vs. Satisfaction Rate (Scatter Plot)\n",
    "fig6 = px.scatter(df, x='Marital Status', y='Satisfaction Rate', color='Satisfaction Rate',\n",
    "                  title='Marital Status vs. Satisfaction Rate',\n",
    "                  labels={'Marital Status': 'Marital Status', 'Satisfaction Rate': 'Satisfaction Rate'})\n",
    "\n",
    "# Number of Children vs. Satisfaction Rate (Scatter Plot)\n",
    "fig7 = px.scatter(df, x='Number of Children', y='Satisfaction Rate', color='Satisfaction Rate',\n",
    "                  title='Number of Children vs. Satisfaction Rate',\n",
    "                  labels={'Number of Children': 'Number of Children', 'Satisfaction Rate': 'Satisfaction Rate'})\n",
    "\n",
    "# Arrange the subplots in a grid layout\n",
    "fig = make_subplots(rows=4, cols=2, subplot_titles=('Age vs. Satisfaction Rate',\n",
    "                                                    'Country vs. Satisfaction Rate',\n",
    "                                                    'Education Level vs. Satisfaction Rate',\n",
    "                                                    'Number of Languages Spoken vs. Satisfaction Rate',\n",
    "                                                    'Gender vs. Satisfaction Rate',\n",
    "                                                    'Marital Status vs. Satisfaction Rate',\n",
    "                                                    'Number of Children vs. Satisfaction Rate'))\n",
    "\n",
    "fig.add_trace(fig1['data'][0], row=1, col=1)\n",
    "fig.add_trace(fig2['data'][0], row=1, col=2)\n",
    "fig.add_trace(fig3['data'][0], row=2, col=1)\n",
    "fig.add_trace(fig4['data'][0], row=2, col=2)\n",
    "fig.add_trace(fig5['data'][0], row=3, col=1)\n",
    "fig.add_trace(fig6['data'][0], row=3, col=2)\n",
    "fig.add_trace(fig7['data'][0], row=4, col=1)\n",
    "\n",
    "# Define the dropdown options\n",
    "dropdown_options = [\n",
    "    {'label': 'Age vs. Satisfaction Rate', 'value': 'age'},\n",
    "    {'label': 'Country vs. Satisfaction Rate', 'value': 'country'},\n",
    "    {'label': 'Education Level vs. Satisfaction Rate', 'value': 'education'},\n",
    "    {'label': 'Number of Languages Spoken vs. Satisfaction Rate', 'value': 'languages'},\n",
    "    {'label': 'Gender vs. Satisfaction Rate', 'value': 'gender'},\n",
    "    {'label': 'Marital Status vs. Satisfaction Rate', 'value': 'marital_status'},\n",
    "    {'label': 'Number of Children vs. Satisfaction Rate', 'value': 'children'}\n",
    "]\n",
    "\n",
    "# Define the dropdown options\n",
    "dropdown_options = [\n",
    "    {'label': 'Age vs. Satisfaction Rate', 'value': 'age'},\n",
    "    {'label': 'Country vs. Satisfaction Rate', 'value': 'country'},\n",
    "    {'label': 'Education Level vs. Satisfaction Rate', 'value': 'education'},\n",
    "    {'label': 'Number of Languages Spoken vs. Satisfaction Rate', 'value': 'languages'},\n",
    "    {'label': 'Gender vs. Satisfaction Rate', 'value': 'gender'},\n",
    "    {'label': 'Marital Status vs. Satisfaction Rate', 'value': 'marital_status'},\n",
    "    {'label': 'Number of Children vs. Satisfaction Rate', 'value': 'children'}\n",
    "]\n",
    "\n",
    "# Define the layout of the Dash app\n",
    "app.layout = html.Div([\n",
    "    html.H1('Satisfaction Rate Visualizations'),\n",
    "    html.Div([\n",
    "        html.Label('Select a visualization:'),\n",
    "        dcc.Dropdown(\n",
    "            id='dropdown',\n",
    "            options=dropdown_options,\n",
    "            value='age'\n",
    "        )\n",
    "    ]),\n",
    "    html.Div([\n",
    "        dcc.Graph(id='graph')\n",
    "    ])\n",
    "])\n",
    "\n",
    "# Define the callback function to update the graph based on the dropdown selection\n",
    "@app.callback(\n",
    "    Output('graph', 'figure'),\n",
    "    [Input('dropdown', 'value')]\n",
    ")\n",
    "def update_graph(selected_value):\n",
    "    if selected_value == 'age':\n",
    "        return fig1\n",
    "    elif selected_value == 'country':\n",
    "        return fig2\n",
    "    elif selected_value == 'education':\n",
    "        return fig3\n",
    "    elif selected_value == 'languages':\n",
    "        return fig4\n",
    "    elif selected_value == 'gender':\n",
    "        return fig5\n",
    "    elif selected_value == 'marital_status':\n",
    "        return fig6\n",
    "    elif selected_value == 'children':\n",
    "        return fig7\n",
    "\n",
    "# Run the Dash app\n",
    "if __name__ == '__main__':\n",
    "    app.run_server(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a49dc830",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
