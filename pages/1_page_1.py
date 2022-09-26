# %%
import plotly.express as px
import plotly.io as pio
import re
import json
import streamlit as st
# %%

def read_from_json(filename):
    return pio.read_json(filename)


def read_from_html(filename):
    with open(filename) as f:
        html = f.read()
    call_arg_str = re.findall(r'Plotly\.newPlot\((.*)\)', html[-2**16:])[0]
    call_args = json.loads(f'[{call_arg_str}]')
    plotly_json = {'data': call_args[1], 'layout': call_args[2]}    
    return pio.from_json(json.dumps(plotly_json))

fig_json = read_from_json("./figs-streamlit/test-fig.json")

fig_html = read_from_html("./figs-streamlit/test-fig.html")

st.plotly_chart(fig_json)

st.plotly_chart(fig_json)