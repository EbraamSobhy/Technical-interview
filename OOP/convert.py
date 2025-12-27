import pypandoc
import os

def md_to_pdf(
    md_file: str,
    output_pdf: str,
    title: str = "OOP-Notes"
):
    if not os.path.exists(md_file):
        raise FileNotFoundError(f"{md_file} not found")

    extra_args = [
        "--pdf-engine=xelatex",

        # Metadata
        "-V", f"title={title}",
        "-V", "geometry:margin=1in",

        # Dark mode colors
        "-V", "mainfont=DejaVu Sans",
        "-V", "monofont=DejaVu Sans Mono",
        "-V", "colorlinks=true",
        "-V", "linkcolor=cyan",
        "-V", "urlcolor=cyan",

        # LaTeX color setup
        "-V", "header-includes=\\usepackage{xcolor}",
        "-V", "header-includes=\\pagecolor{white}",
        "-V", "header-includes=\\color{black}",

        # Code block styling
        "--highlight-style=monochrome",

        # Table of contents
        "--toc"
    ]

    pypandoc.convert_file(
        source_file=md_file,
        to="pdf",
        outputfile=output_pdf,
        extra_args=extra_args
    )

    print(f"✅ Dark mode PDF created: {output_pdf}")

if __name__ == "__main__":
    md_to_pdf(
        md_file="OOP-Notes.md",
        output_pdf="OOP-Notes.pdf",
        title="OOP-Notes"
    )
