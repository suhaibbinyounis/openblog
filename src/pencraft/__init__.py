"""Pencraft - AI-powered blog writing toolkit.

Pencraft automates blog creation through AI, leveraging LangChain and
OpenAI-compatible APIs to research topics, create structured outlines,
and generate publish-ready blog posts in markdown format.
"""

__version__ = "0.1.0"
__author__ = "Suhaib Bin Younis"
__license__ = "MIT"

from pencraft.config.settings import Settings, get_settings

__all__ = ["Settings", "get_settings", "__version__"]
