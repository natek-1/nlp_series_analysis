from series_analysis.components.theme_classification.theme_classification import ThemeClassifier

theme_list = ["friendship","hope","sacrifice","battle","self development","betrayal","love","dialogue", "pain", "hatred", "dream", "hard work", "war"]
subtitles_path = "data/subtitles"
save_path = "output.test.csv"

theme_classifier = ThemeClassifier(theme_list=theme_list)
output_df = theme_classifier.get_themes(subtitles_path, save_path=save_path)

print(output_df)

output_df = output_df[theme_list].sum().reset_index()
output_df.columns = ['Theme','Score']
print("Second print of output df")
print(output_df)