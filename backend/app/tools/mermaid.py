import re
import mermaidian as mm
import os


def clean_mermaid_code(code: str) -> str:
    code = code.strip()

    code = re.sub(r"```mermaid", "", code, flags=re.IGNORECASE)
    code = re.sub(r"```", "", code)

    match = re.search(r"(graph\s+(LR|TD|TB|RL)[\s\S]*)", code)
    if match:
        code = match.group(1)

    return "\n" + code.strip()


def generate_flow_diagram(mermaid_code: str, project_path: str) -> str:
    mermaid_code = clean_mermaid_code(mermaid_code)
    if hasattr(mermaid_code, "content"):
        mermaid_code = mermaid_code.content

    image_bytes = mm.get_mermaid_diagram("png", mermaid_code)

    os.makedirs(f"{project_path}/project", exist_ok=True)
    mm.save_diagram_as_image(
        path=f"{project_path}/project/flow_diagram.png", diagram=image_bytes
    )

    return f"File saved to {project_path}/project/flow_diagram.png"
