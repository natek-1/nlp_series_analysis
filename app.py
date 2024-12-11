import os
from dotenv import load_dotenv
import gradio as gr
from series_analysis.components.theme_classification.theme_classification import ThemeClassifier




def get_themes(theme_list_str, subtitles_path, save_path):
    theme_list = theme_list_str.split(",")
    theme_classifier = ThemeClassifier(theme_list)
    output_df = theme_classifier.get_themes(subtitles_path, save_path=save_path)
    
    output_df = output_df[theme_list].sum().reset_index()
    output_df.columns = ['Theme','Score']
    
    output_plot = gr.BarPlot(
        output_df,
        x = "Theme",
        y= "Score",
        title="Series Themes Distribution",
        tooltip = ["Theme", "Score"],
        vertical=False,
        width=500,
        height=260
    )
    return output_plot



def main():
    with gr.Blocks() as iface:
        
        with gr.Row():
            with gr.Column():
                gr.HTML("<h1>Theme Classification of the Naruto Series</h1>")
                with gr.Row():
                    with gr.Column():
                        plot = gr.BarPlot()
                    with gr.Column():
                        theme_list = gr.Textbox(label="Themes")
                        subtitles_path = gr.Textbox(label="Subtitle or script Path")
                        save_path = gr.Textbox(label="Save Path")
                        get_themes_button = gr.Button("Get Themes")
                        get_themes_button.click(get_themes, inputs=[theme_list, subtitles_path, save_path], outputs=[plot])
    iface.launch(share=True)

if __name__ == "__main__":
    main()