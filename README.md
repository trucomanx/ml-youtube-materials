# Video Generation Workflow

This project contains the structure and automated tools used for my video generation workflow. It is organized into three main areas to manage assets, final content, and processing scripts.

## Project Structure

The repository is organized as follows:

### 📂 drafts/
Contains all **work-in-progress** video projects.
*   **Subfolders:** Each subfolder corresponds to a specific video project.
*   **Contents:** Includes generation data, raw assets, prompts, and temporary files used during the creation process before the final export.

### 📂 published/
Storage for all **completed and released** videos.
*   **Subfolders:** Organized by project name or date of publication.
*   **Contents:** Final video files along with the specific generation metadata used for the final version (for archival and future reference).

### 📂 tools/
The core of the workflow, containing **automation scripts**.
*   **Contents:** Python, Bash, or other scripts necessary to run the generation pipeline, process data, and move files through the workflow (from *drafts* to *published*).

---

## How to Use
1. Place your initial data or start your project inside the `drafts/` folder.
2. Use the scripts located in `tools/` to process or generate your content.
3. Once the video is finalized and shared, move the project folder and its data to `published/`.

