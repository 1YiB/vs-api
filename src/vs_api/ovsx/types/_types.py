from typing import Literal

class uid(str):
    def url(self):
        return f"{self.replace('.','/')}"

category = Literal[
    "",
    "Programming Languages",
    "Snippets",
    "Linters",
    "Themes",
    "Debuggers",
    "Formatters",
    "Keymaps",
    "SCM Providers",
    "Other",
    "Extension Packs",
    "Language Packs",
    "Data Science",
    "Machine Learning",
    "Visualization",
    "Notebooks",
]
sortBy = Literal[
    "",
    "relevance",
    "timestamp",
    "downloadCount",
    "averageRating",
]
sortOrder = Literal[
    "",
    "desc",
    "asc"
]
