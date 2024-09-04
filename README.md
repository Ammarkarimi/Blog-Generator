# Blog Generation App

This is a Streamlit application that generates blog posts based on user inputs. The application leverages the CTransformers library with a LLaMA model to produce high-quality content. The user can customize the blog based on the target audience, tone, content focus, and preferred structure.

## Features

- **Customizable Inputs**: 
  - Blog Topic
  - Target Audience Level (Beginner, Intermediate, Advanced)
  - Tone of Writing (Formal, Informal, Conversational, Technical)
  - Content Focus (Overview, In-depth Analysis, Practical Tips, Case Study)
  - Preferred Structure (Listicle, Step-by-Step Guide, Narrative, Comparison)
  - Writing Style (Researcher, Data Scientist, Common People)

- **GPU Acceleration**: 
  - Automatically uses GPU if available for faster processing.

## Requirements

- Python 3.8+
- Streamlit
- Langchain
- CTransformers
- PyTorch

## Installation

1. Clone the repository:

    ```bash
    https://github.com/Ammarkarimi/Blog-Generator.git
    cd Blog-Generator
    ```

2. Set up a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - **Windows**:

        ```bash
        venv\Scripts\activate
        ```

    - **macOS/Linux**:

        ```bash
        source venv/bin/activate
        ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

5. Download the LLaMA model and place it in the appropriate directory (`model\`).

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run main.py
    ```

2. Open the web interface in your browser. You should see the "Generate Blogs" interface.

3. Enter the following inputs:
   - **Blog Topic**: The main subject of the blog.
   - **Writing Style**: The audience you're writing for (Researcher, Data Scientist, Common People).
   - **Target Audience Level**: The level of knowledge of the target audience.
   - **Tone of Writing**: The tone to use in the blog.
   - **Content Focus**: The focus of the content (Overview, In-depth Analysis, etc.).
   - **Preferred Structure**: The structure to follow (Listicle, Step-by-Step Guide, etc.).

4. Click on the **Generate** button to create the blog. The generated content will be displayed on the page.

## Customization

- **Temperature Setting**: The temperature can be adjusted in the `getLlamaResponse` function in `main.py` to control the creativity of the generated text.
- **Model Path**: Modify the path to the LLaMA model in the code if it's stored in a different location.

## Troubleshooting

- If the app is running slow, ensure that your GPU is properly configured and recognized by PyTorch. Check your installation using:

    ```bash
    python -c "import torch; print(torch.cuda.is_available())"
    ```

- If you encounter any errors, ensure that all dependencies are properly installed and that the LLaMA model is correctly downloaded.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- Thanks to the developers of [Streamlit](https://www.streamlit.io/), [Langchain](https://www.langchain.com/), and [CTransformers](https://github.com/Cedeel/CTransformers) for making this project possible.

