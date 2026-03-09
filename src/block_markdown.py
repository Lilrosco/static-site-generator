def markdown_to_blocks(markdown):
    blocks = []
    sections = markdown.split("\n\n")

    for section in sections:
        cln_section = section.strip()

        if cln_section != "":
            blocks.append(cln_section)
    
    return blocks
