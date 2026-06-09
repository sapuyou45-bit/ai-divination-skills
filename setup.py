from setuptools import find_packages, setup


setup(
    name="ai-divination-skills",
    version="0.6.1",
    description="Direct, practical divination skills for AI agents.",
    packages=find_packages(include=["ai_divination_skills*"]),
    package_data={"ai_divination_skills": ["templates/*.md"]},
    python_requires=">=3.9",
    install_requires=[],
    extras_require={
        "lunar": ["lunar-python>=1.4.4"],
        "dev": ["build", "twine", "PyYAML>=6"],
    },
    entry_points={
        "console_scripts": [
            "ai-divination=ai_divination_skills.cli:main",
            "ai-divination-mcp=ai_divination_skills.mcp_server:main",
        ],
    },
)
