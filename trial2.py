import gradio as gr

def create_audio_component(title, file_path, description):
    return gr.Column([
        gr.Audio(value=file_path, label=title, interactive=False, show_label=False),
        gr.Markdown(f"<div style='text-align: center; font-size: 16px; color: #eee; font-weight: bold; margin-top: 5px;'>{description}</div>")
    ])

def audio_samples_interface():
    with gr.Blocks(css="""
        .gradio-container { font-family: 'Arial', sans-serif; max-width: 1000px; margin: auto; padding: 20px; }
        h1 { text-align: center; color: #fff; font-size: 28px; }
        h2 { color: #ddd; font-size: 20px; margin-top: 20px; border-bottom: 2px solid #555; padding-bottom: 5px; text-align: center; }
        .gr-row { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 20px; }
    """) as demo:
        gr.Markdown("# Audio Samples")
        
        with gr.Tab("MusicGen"):
            gr.Markdown("## Genre Steering (Classical to Rock)")
            with gr.Row():
                create_audio_component("Sample 1", "mg1.wav","")
                create_audio_component("Sample 1", "mg2.wav","")
            with gr.Row():
                create_audio_component("Sample 1", "mg3.wav","")
            gr.Markdown("")
            
            gr.Markdown("## Instrument Steering")
            with gr.Row():
                create_audio_component("Sample 4", "og_audio.wav", "Original unmodified audio sample.")
                create_audio_component("Sample 5", "to_flute.wav", "Converted to a flute-based melody.")
            with gr.Row():
                create_audio_component("Sample 6", "to_violin.wav", "Same tune rendered with violin.")
                create_audio_component("Sample 7", "to_xylophone.wav", "Xylophone version of the sample.")
            gr.Markdown("")
            
            gr.Markdown("## Other Samples")
            with gr.Row():
                create_audio_component("Sample 8", "classical_elec.wav", "Hybrid classical and electronic mix.")
                create_audio_component("Sample 9", "elec_Rock.wav", "Electrified rock-style transformation.")
        
        with gr.Tab("Groove2Groove"):
            gr.Markdown("## Groove Transformations")
            with gr.Row():
                create_audio_component("Content 1", "trimmed_content_Avengers.wav", "Extracted content from Avengers theme.")
                create_audio_component("Style 1", "trimmed_style_AlhiyaBilawal.wav", "Traditional Alhiya Bilawal musical style.")
            with gr.Row():
                create_audio_component("Genre 1", "trimmed_output_v03.wav", "Genre transformation applied.")
            gr.Markdown("")
            
            with gr.Row():
                create_audio_component("Content 2", "trimmed_content_Pirates.wav", "Pirates of the Caribbean orchestral sample.")
                create_audio_component("Style 2", "trimmed_style_AlhiyaBilawal (1).wav", "Same style transformation applied.")
            with gr.Row():
                create_audio_component("Genre 2", "trimmed_output_v03 (1).wav", "Genre modified output.")
            gr.Markdown("")
            
            with gr.Row():
                create_audio_component("Content 3", "trimmed_content_Star.wav", "Star Wars theme extracted content.")
                create_audio_component("Style 3", "trimmed_style_bazigar.wav", "Bazigar musical style applied.")
            with gr.Row():
                create_audio_component("Genre 3", "trimmed_output_v02.wav", "Final output with genre modifications.")
    
    return demo

demo = audio_samples_interface()

demo.launch()
