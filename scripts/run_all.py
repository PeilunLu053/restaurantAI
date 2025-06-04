"""Simple pipeline script to generate and edit a video."""

from backend.services import llm_generator, ai_editor


def run_pipeline(idea: str, video_path: str):
    script = llm_generator.generate_video_script(idea)
    result = ai_editor.automate_editing(video_path, script)
    print(result)


if __name__ == "__main__":
    run_pipeline("Delicious noodles", "data/raw_videos/sample.mp4")
