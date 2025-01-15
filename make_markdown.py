import json

def create_markdown_from_json(json_file, markdown_file):
    """
    Reads a JSON file containing information about open problems in category theory
    and creates a GitHub Markdown file from it.

    Args:
        json_file: The path to the input JSON file.
        markdown_file: The path to the output Markdown file.
    """
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
        return

    with open(markdown_file, 'w') as f:
        f.write("# Open Problems in Category Theory\n\n")

        for problem in data:
            f.write(f"## {problem['title']}\n\n")
            f.write(f"**Tag:** `{problem['tag']}`\n\n")
            f.write(f"**Author:** {problem['author']}\n\n")
            f.write(f"**Link:** [{problem['link']}]({problem['link']})\n\n")
            f.write(f"**Description:**\n\n{problem['body']}\n\n")
            f.write(f"---\n**Status:** {problem['status']}\n\n---\n")
            f.write(f"**Comments:**\n\n{problem['comments']}\n\n---\n\n")

    print(f"Markdown file '{markdown_file}' created successfully.")

# Example usage:
create_markdown_from_json("problems.json", "problems.md")
