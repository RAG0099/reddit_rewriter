import gradio as gr
from scrape_user import get_user_comments
from huggingface_hub import InferenceClient

# === Load HF model (free hosted LLM) ===
# You can swap in another open model if you want
client = InferenceClient("mistralai/Mistral-7B-Instruct-v0.2")

def load_style_examples(username="FixitMir", num_comments=5):
    """Fetch and store Reddit user's style examples once."""
    examples = get_user_comments(username, num_comments)
    return "\n\n".join([f"- {c}" for c in examples])

def rewrite_comment_live(original_comment, username="FixitMir", num_examples=5):
    """Rewrite comment in the style of a Reddit user using HF Inference API."""
    style_examples = load_style_examples(username, num_examples)

    prompt = f"""
Here are some examples of how u/{username} writes on Reddit:
{style_examples}

Now rewrite the following comment so it matches their style:
"{original_comment}"
"""

    response = client.text_generation(prompt, max_new_tokens=200)
    return response.strip()

# === Gradio UI ===
with gr.Blocks(title="Reddit Style Rewriter") as demo:
    gr.Markdown("# 📝 Reddit Persona Style Rewriter")
    gr.Markdown("Rewrite any comment in the style of a Reddit user by fetching their actual posts.")

    with gr.Row():
        username = gr.Textbox(label="Reddit Username", value="FixitMir")
        num_examples = gr.Slider(3, 15, value=5, step=1, label="Number of Style Examples")

    input_comment = gr.Textbox(label="💬 Your Comment", placeholder="Enter a comment to rewrite...")
    output_comment = gr.Textbox(label="🤖 Rewritten in Style", interactive=False)

    rewrite_button = gr.Button("✨ Rewrite")
    
    rewrite_button.click(
        fn=rewrite_comment_live,
        inputs=[input_comment, username, num_examples],
        outputs=output_comment
    )

# === Run on HF ===
if __name__ == "__main__":
    demo.launch()
