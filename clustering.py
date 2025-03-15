import pandas as pd
import plotly.express as px
import gradio as gr


# Function to load and plot 3D graph
def load_and_plot(tsv_points, tsv_labels):
    df_points = pd.read_csv(tsv_points, sep='\t')  # Load points TSV file
    df_labels = pd.read_csv(tsv_labels, sep='\t')  # Load labels TSV file
    
    if len(df_points.columns) < 3 or len(df_labels.columns) < 1:
        return "Error: Points file must have at least three columns, and labels file must have at least one column."
    
    df_points['label'] = df_labels.iloc[:, 0]  # Assign labels from the labels file
    
    fig = px.scatter_3d(df_points, x=df_points.columns[0], y=df_points.columns[1], z=df_points.columns[2], 
                         color='label', title="Interactive 3D Graph with Labels")  # Create 3D plot with color-coded labels
    fig.update_layout(scene=dict(aspectmode="cube"))  # Enable full 3D rotation
    return fig

# Specify local file paths for TSVs
points_file = "residual_conditional_25.tsv"
labels_file = "residual_conditional_instruments_22.tsv"

image_files = {
    "Visualization 1": "cluster.jpg",
    "C" : "C.jpg",
    "D" : "D.jpg",
    "A" : "A.jpg",
    "F" : "F.jpg"
}

with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue")) as demo:
    gr.Markdown("""
    # 🎵 **Clustering** 🎶
    """)

    gr.Markdown("""## Model 1 : Musicgen""")
    
        

    gr.Markdown("""## Interactive Graphs""")
    gr.Markdown("""3D visualization of preloaded data.""")
    plot_output = gr.Plot(value=load_and_plot(points_file, labels_file))
# Specify local file paths for TSVs
    points_file1 = "residual_conditional_26.tsv"
    labels_file1 = "residual_conditional_instruments_21.tsv"
    gr.Markdown("""Clustering of Chords""")
    with gr.Row():
        gr.Image(image_files["C"], label="C")
        gr.Image(image_files["D"], label="D")
        gr.Image(image_files["A"], label="A")
        gr.Image(image_files["F"], label="F")

    

    gr.Markdown("""## Model 2 : Groove2Groove""")
    with gr.Row():
        gr.Image(image_files["Visualization 1"], label="Visualization 1")


 
demo.launch()
