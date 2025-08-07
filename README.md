# Credit Memo Generator using LLM

Automatically generate credit memos from structured and unstructured customer data using Large Language Models (LLMs).

## Overview

This project demonstrates how LLMs can streamline the credit analysis process by generating clear, standardized memos based on customer data. It supports:

- 🔁 Locally hosted models (via Ollama: Mistral, LLaMA)


The app is built using **Streamlit** and provides a simple interface.

## Problem Statement

Credit analysts often spend hours crafting credit memos using fragmented information. This project uses LLMs to automatically synthesize structured financial data and unstructured text (e.g., notes, comments) into a consistent summary.

## Business Impact

- ⏱️ Reduces time spent on memo writing
- 📄 Standardizes documentation quality
- ⚡ Enables faster and explainable credit decisions

## Tech Stack

- **LLMs**: Mistral / LLaMA (via Ollama)
- **Frameworks**: Streamlit, LangChain, LlamaIndex
- **Data**: Mock structured data (JSON/YAML)
- **Environment**: Python 3.9+, `requirements.txt` included

## How to Run Locally

### Clone the Repo

```bash
git clone https://github.com/yourusername/llm-credit-memo-generator.git
cd llm-credit-memo-generator
