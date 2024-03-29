# Instructions for adding more plots

The plots are stored in the directory `figs-streamlit`, with names like `090 Trig Loss Ratio.html`.

The tens digit determines which page the plot is on (so if 2 plots have numbers `090` and `095` then they're on the same page). The text after that is the title of the page (as it appears on the sidebar), e.g. the title of the previously mentioned page is `Trig Loss Ratio`.

You can save plots which you generate in your notebook or colab, using code like this:

```
def write_to_html(fig, filename):
    with open(f"figs-streamlit/{filename}.html", "w") as f:
        f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))
    
write_to_html(fig, '090 Trig Loss Ratio.html')
```

In order to add new plots, do the following:

1. Write the figure to html, using the code above.
2. Delete all the files in the directory `pages`.
3. Uncomment the function `create_streamlit_pages` in the file `Home.py`, and run it. This will re-populate the `pages` directory, using the (new) contents of the `figs-streamlit` directory.
4. Update the GitHub repo with the changes you've made, and reload the Streamlit page. You should now have new plots.

Note - as an alternative to steps 2 & 3, you can just duplicate one of the pages in the `pages` directory, and edit the code & title of page appropriately. 
