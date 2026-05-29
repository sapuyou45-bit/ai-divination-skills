from setuptools import setup


setup(
    name="ai-divination-skills",
    version="0.3.0",
    description="Direct, practical divination skills for AI agents.",
    packages=["ai_divination_skills"],
    python_requires=">=3.9",
    install_requires=[],
    extras_require={"lunar": ["lunar-python>=1.4.4"]},
    entry_points={
        "console_scripts": [
            "ai-divination=ai_divination_skills.cli:main",
        ],
    },
)
