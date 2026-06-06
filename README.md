<div align="center">

<h1>LLM Based Research Orchestration Engine</h1>

<h3>AI-Powered Research Report Generation System Using LangChain Runnables</h3>

<p>
A modular research automation pipeline built using LangChain Expression Language (LCEL), Runnable architecture, and Groq LLMs.
</p>

</div>

<hr>

<h2>Overview</h2>

<p>
LLM Based Research Orchestration Engine is a modular AI workflow system that automates the process of generating structured research reports using LangChain Runnables.
</p>

<p>
The project demonstrates how modern AI systems are engineered using:
</p>

<ul>
<li>RunnableSequence</li>
<li>RunnableParallel</li>
<li>RunnableLambda</li>
<li>RunnablePassthrough</li>
<li>LCEL Pipelines</li>
<li>Modular Prompt Engineering</li>
</ul>

<p>
Instead of relying on a single prompt-response interaction, this system uses a multi-stage orchestration pipeline capable of generating multiple research sections simultaneously and combining them into a professionally formatted report.
</p>

<hr>

<h2>Problem Statement</h2>

<p>
Creating detailed research reports manually is time-consuming and repetitive. Writers, students, analysts, and researchers often spend significant time:
</p>

<ul>
<li>Structuring research topics</li>
<li>Generating section-wise content</li>
<li>Maintaining consistency in writing style</li>
<li>Formatting reports properly</li>
<li>Summarizing findings</li>
</ul>

<p>
This project solves the problem by automating the entire report generation workflow using orchestrated LLM pipelines.
</p>

<hr>

<h2>Project Architecture</h2>

<pre>
User Topic
    ↓
RunnableParallel
 ├── Introduction Chain
 ├── Applications Chain
 └── Challenges Chain
    ↓
RunnableLambda Formatter
    ↓
Final Markdown Report
</pre>

![Uploading Screenshot 2026-06-06 103948.png…]()


<hr>

<h2>Core Concepts Used</h2>

<table>
<tr>
<th>Component</th>
<th>Purpose</th>
</tr>

<tr>
<td>RunnableSequence</td>
<td>Creates sequential AI workflows</td>
</tr>

<tr>
<td>RunnableParallel</td>
<td>Generates multiple report sections simultaneously</td>
</tr>

<tr>
<td>RunnableLambda</td>
<td>Transforms and formats outputs</td>
</tr>

<tr>
<td>RunnablePassthrough</td>
<td>Preserves and propagates workflow state</td>
</tr>

<tr>
<td>Prompt Templates</td>
<td>Provides modular prompting architecture</td>
</tr>

<tr>
<td>LCEL</td>
<td>Enables declarative chain composition</td>
</tr>

</table>

<hr>

<h2>Features</h2>

<ul>
<li>Automated AI-powered research report generation</li>
<li>Parallel section generation using RunnableParallel</li>
<li>Modular chain architecture</li>
<li>Structured prompt engineering</li>
<li>Markdown report formatting</li>
<li>Scalable workflow design</li>
<li>Groq LLM integration</li>
<li>Production-style project structure</li>
</ul>

<hr>

<h2>Project Structure</h2>

<pre>
AI_Research_Report_Generator/
│
├── app.py
│
├── chains/
│   ├── planner_chain.py
│   ├── section_chain.py
│   ├── parallel_chain.py
│   └── formatter_chain.py
│
├── prompts/
│   ├── planner_prompt.py
│   └── section_prompt.py
│
├── utils/
│   └── formatter.py
│
├── outputs/
│   └── report.md
│
├── requirements.txt
│
├── .env
│
└── README.md
</pre>

<hr>

<h2>Workflow Explanation</h2>

<h3>1. Topic Input</h3>

<p>
The user provides a research topic.
</p>

<pre>
Example:
"Future of Generative AI in Healthcare"
</pre>

<h3>2. Parallel Section Generation</h3>

<p>
The system uses RunnableParallel to generate multiple sections simultaneously:
</p>

<ul>
<li>Introduction</li>
<li>Applications</li>
<li>Challenges</li>
</ul>

<h3>3. Formatting Pipeline</h3>

<p>
RunnableLambda combines and formats all generated sections into a structured markdown report.
</p>

<h3>4. Final Output</h3>

<p>
The final report is stored as:
</p>

<pre>
outputs/report.md
</pre>

<hr>

<h2>Technologies Used</h2>

<table>
<tr>
<th>Technology</th>
<th>Purpose</th>
</tr>

<tr>
<td>Python</td>
<td>Core programming language</td>
</tr>

<tr>
<td>LangChain</td>
<td>LLM orchestration framework</td>
</tr>

<tr>
<td>LangChain Core</td>
<td>Runnable architecture and LCEL</td>
</tr>

<tr>
<td>Groq API</td>
<td>LLM inference provider</td>
</tr>

<tr>
<td>LCEL</td>
<td>Chain composition syntax</td>
</tr>

<tr>
<td>dotenv</td>
<td>Environment variable management</td>
</tr>

</table>

<hr>

<h2>Installation</h2>

<h3>1. Clone Repository</h3>

<pre>
git clone https://github.com/your-username/AI_Research_Report_Generator.git

cd AI_Research_Report_Generator
</pre>

<h3>2. Create Virtual Environment</h3>

<pre>
python -m venv venv
</pre>

<h3>3. Activate Virtual Environment</h3>

<h4>Windows</h4>

<pre>
venv\Scripts\activate
</pre>

<h4>Linux / Mac</h4>

<pre>
source venv/bin/activate
</pre>

<h3>4. Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<hr>

<h2>Environment Variables</h2>

<p>
Create a <code>.env</code> file in the root directory:
</p>

<pre>
GROQ_API_KEY=your_api_key_here
</pre>

<hr>

<h2>Running The Project</h2>

<pre>
python app.py
</pre>

<p>
Enter a research topic when prompted.
</p>

<hr>

<h2>Example Output</h2>

<pre>
# Future of Generative AI in Healthcare

## Introduction
...

## Applications
...

## Challenges
...
</pre>

<hr>

<h2>Learning Outcomes</h2>

<p>
This project demonstrates practical understanding of:
</p>

<ul>
<li>LLM Workflow Engineering</li>
<li>Prompt Chaining</li>
<li>Parallel AI Processing</li>
<li>Production-Style AI Architecture</li>
<li>Modular LangChain Development</li>
<li>Runnable Orchestration</li>
<li>State Transformation Pipelines</li>
</ul>

<hr>

<h2>Future Improvements</h2>

<ul>
<li>Dynamic section generation</li>
<li>Executive summary generation</li>
<li>RunnableBranch integration</li>
<li>Audience-specific report styles</li>
<li>Report evaluation chains</li>
<li>Hallucination detection</li>
<li>Streamlit frontend</li>
<li>PDF export support</li>
<li>RAG integration</li>
<li>Multi-agent orchestration</li>
</ul>

<hr>

<h2>Version</h2>

<p>
Version 1.0
</p>

<hr>

<h2>Author</h2>

<p>
Ashutosh Pandey
</p>

<p>
Generative AI Research Analyst | AI Workflow Engineering Enthusiast
</p>
