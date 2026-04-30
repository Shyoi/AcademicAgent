## ✂️ Academic-Tailor-Agent

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![LlamaIndex](https://img.shields.io/badge/Framework-LlamaIndex-brightgreen) ![LLM](https://img.shields.io/badge/LLM-GPT--4o--mini-orange) ![Streamlit](https://img.shields.io/badge/UI-Streamlit-red) 

**Academic-Tailor-Agent** is an advanced AI-driven system designed to automate the deep analysis and modular reconstruction of academic literature. By leveraging Retrieval-Augmented Generation (RAG) and multi-agent collaboration, it helps researchers rapidly evaluate the feasibility of cross-paper algorithm integration. 

---

## 🎯 Core Pain Points Solved

Computer vision researchers frequently rely on an "academic tailoring" strategy—integrating authenticated, feasible modules from existing papers to construct novel architectures without reinventing the wheel. However, this process faces significant bottlenecks: 

1. **High Trial-and-Error Costs in Module Decoupling:** It is extremely time-consuming to manually determine if a specific component can be detached from its original architecture. For instance, evaluating whether an illumination-aware sub-network and its corresponding loss functions can be decoupled from a progressive fusion mechanism and repurposed into a "feature extraction then fusion" paradigm. 
2. **Complexity in Cross-Paper Architecture Alignment:** Searching through massive PDF repositories to check the compatibility of different foundational units (e.g., verifying if the basic window and shifted window attention blocks from a Swin Transformer can seamlessly integrate with targeted illumination-handling modules for nighttime scenes). 3. **Information Overload:** Traditional keyword searches only retrieve shallow abstracts, failing to extract the deep mathematical definitions and specific network sub-structures required for actual coding and architectural design. Academic-Tailor-Agent directly addresses these issues by automating the extraction, comparison, and feasibility assessment of specific algorithmic blocks. 

---

## 🧠 Core Logic Flow 

The system architecture is built upon a robust **Multi-Agent Collaboration** framework, utilizing **Long-Chain Reasoning** to process complex academic logic rather than simple keyword matching. 

### 1. Retrieval Agent (Knowledge Base Construction) 

* **Function:** Automatically scans local PDF repositories, chunks academic texts, and parses complex mathematical formulas and architectural diagrams. 
*  **Mechanism:** Builds a high-dimensional Vector Store using LlamaIndex, transforming unstructured PDFs into a queryable RAG (Retrieval-Augmented Generation) knowledge base. 

### 2. Reasoning Agent (Long-Chain Execution) 

* **Function:** Executes multi-step, cross-document logical reasoning based on user-defined architectural proposals. 
* **Mechanism:**   
  * **Step 1:** Recalls the top-K most relevant network structures and loss function definitions from the vector space.  
  * **Step 2:** Applies customized Prompt Chaining to force the LLM to focus strictly on foundational building blocks (ignoring broad, generic summaries).  
  * **Step 3:** Conducts a logical collision test—evaluating the theoretical and engineering feasibility of stitching the queried modules together.

 ### 3. Synthesis Agent (Structured Output Generation) *

* **Function:** Consolidates the fragmented insights from the Reasoning Agent into a cohesive, professional deliverable.
* **Mechanism:** Reorganizes the analytical data into a standardized Markdown report, detailing the core targets, module teardowns, fusion feasibility assessments, and actionable R&D suggestions. 

---

## 🛠️ Tech Stack

* **Backend & AI Agent Framework:** Python, LlamaIndex, OpenAI API *
*  **Frontend & Interactive UI:** Streamlit 
* **Document Processing:** SimpleDirectoryReader (PDF Parsing) 