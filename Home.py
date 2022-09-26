# %%
import plotly.express as px
import plotly.io as pio
import re
import json
from pathlib import Path
import streamlit as st
# %%
def read_from_html(filename):
    filename = f"./figs-streamlit/{filename}.html"
    with open(filename) as f:
        html = f.read()
    call_arg_str = re.findall(r'Plotly\.newPlot\((.*)\)', html)[0]
    call_args = json.loads(f'[{call_arg_str}]')
    plotly_json = {'data': call_args[1], 'layout': call_args[2]}    
    return pio.from_json(json.dumps(plotly_json))
# %%
st.title("Home")

st.markdown("""Here is a list of all the figures in the Grokking paper.

You can navigate through the figures using the sidebar on the left.""")

# %%

def create_streamlit_pages():
    """
    Function which writes all streamlit pages, corresponding to the figures in `figs-streamlit` directory.
    """
    p_pages = Path("pages")
    assert len(list(p_pages.iterdir())) == 0, "Please delete contents of `pages` directory before running this function. The function will reconstruct pages from the `figs-streamlit` directory."

    p_figures = Path("figs-streamlit")
    for filepath in p_figures.iterdir():
        name = filepath.name
        stem = filepath.stem
        num, title = name[:3], stem[4:].replace(" ", "_")
        p_write = Path(f"pages/{num}_{title}.py")
        if not p_write.exists():
            with open(str(p_write), "w") as f:
                f.write("from Home import *\n\n")
        with open(str(p_write), "a") as f:
            f.write(f"fig = read_from_html('{stem}')\n")
            f.write("st.plotly_chart(fig)\n")

# create_streamlit_pages()