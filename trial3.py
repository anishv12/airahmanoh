import gradio as gr

def create_audio_component(title, file_path, description):
    return gr.Column([
        gr.Audio(value=file_path, label=title, interactive=False, show_label=False),
        gr.Markdown(f"""
        <div style='text-align: center; font-size: 16px; color: #bbb; font-weight: bold; margin-top: 5px;'>
            {description}
        </div>
        """)
    ], elem_id="audio-component")

def audio_samples_interface():
    with gr.Blocks(css="""
        .gradio-container { font-family: 'Arial', sans-serif; max-width: 1200px; margin: auto; padding: 30px; background-color: #0f0f0f; }
        h1 { text-align: center; color: #fff; font-size: 32px; margin-bottom: 20px; }
        h2 { color: #ddd; font-size: 22px; margin-top: 20px; border-bottom: 2px solid #444; padding-bottom: 5px; text-align: center; }
        .gr-column { display: flex; flex-direction: column; align-items: center; gap: 10px; }
        .gr-box { background: #1a1a1a; padding: 15px; border-radius: 8px; box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.1); width: 100%; }
    """) as demo:
        gr.Markdown("""<h1>🎵 Audio Showcase 🎵</h1>
        <p style='text-align: center; color: #bbb;'>Listen to the original audio and its modified versions.</p>""")

        with gr.Tab("MusicGen"):
            gr.Markdown("## 🎼 Genre Steering: Classical to Rock")
            with gr.Column():
                create_audio_component("Sample 1", "mg1.wav", "")
                create_audio_component("Sample 2", "mg2.wav", "")
                create_audio_component("Sample 3", "mg3.wav", "")

            gr.Markdown("## 🎻 Instrument Steering")
            with gr.Column():
                create_audio_component("Original", "og_audio.wav", "Original unmodified audio.")
                create_audio_component("Flute Version", "to_flute.wav", "Converted to flute.")
                create_audio_component("Violin Version", "to_violin.wav", "Rendered with violin.")
                create_audio_component("Xylophone Version", "to_xylophone.wav", "Xylophone adaptation.")
            
            gr.Markdown("## 🎶 Other Transformations")
            with gr.Column():
                create_audio_component("Classical-Electronic Mix", "classical_elec.wav", "Blending classical & electronic.")
                create_audio_component("Electronic Rock", "elec_Rock.wav", "Electrified rock version.")

        with gr.Tab("Groove2Groove"):
            gr.Markdown("## 🥁 Groove Transformations")
            with gr.Column():
                gr.Markdown("## 🥁  Transformation 1")
                create_audio_component("Content: Avengers", "trimmed_content_Avengers.wav", "Extracted from Avengers theme.")
                create_audio_component("Style: Alhiya Bilawal", "trimmed_style_AlhiyaBilawal.wav", "Traditional Alhiya Bilawal style.")
                create_audio_component("Genre Modified", "trimmed_output_v03.wav", "Final transformed version.")
                gr.Markdown("## 🥁  Transformation 2")
                create_audio_component("Content: Pirates", "trimmed_content_Pirates.wav", "Pirates of the Caribbean sample.")
                create_audio_component("Style: Alhiya Bilawal", "trimmed_style_AlhiyaBilawal (1).wav", "Same style transformation.")
                create_audio_component("Genre Modified", "trimmed_output_v03 (1).wav", "Final transformed version.")
                gr.Markdown("## 🥁  Transformation 3")
                create_audio_component("Content: Star Wars", "trimmed_content_Star.wav", "Extracted Star Wars theme.")
                create_audio_component("Style: Bazigar", "trimmed_style_bazigar.wav", "Bazigar musical style applied.")
                create_audio_component("Final Output", "trimmed_output_v02.wav", "Modified genre adaptation.")

    return demo

demo = audio_samples_interface()
demo.launch()
