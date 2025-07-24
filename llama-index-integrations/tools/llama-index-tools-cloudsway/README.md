# Cloudsway for LlamaIndex

Cloudsway provides advanced web search capabilities for LlamaIndex applications via its SmartsearchTool. It enables efficient, multi-language, safe, and structured web search for LLM-powered workflows.

## Features

- **Keyword-based web search**: Retrieve relevant results from the web using natural language queries.
- **Configurable options**: Control result count, language, and safety level to tailor searches to your needs.
- **Structured JSON output**: Results are returned in a machine-friendly format for easy downstream processing.
- **Privacy-focused**: No personal data is collected.
- **Easy integration**: Works seamlessly with LlamaIndex agents.

## Installation

Install the integration package:

```bash
pip install llama-index-tools-cloudsway llama-index-core
```

## Configuration

Set your Cloudsway API credentials as an environment variable:

```bash
export CLOUDSWAY_SERVER_KEY="your-endpoint-accesskey"
```

The value should be in the format:
`endpoint-accesskey`

To get your token and subscribe to a plan, please register at [console.cloudsway.ai](https://console.cloudsway.ai/).

Alternatively, you can set the key interactively in Python:

```python
import getpass, os

if not os.environ.get("CLOUDSWAY_SERVER_KEY"):
    os.environ["CLOUDSWAY_SERVER_KEY"] = getpass.getpass(
        "CLOUDSWAY_SERVER_KEY:\n"
    )
```

## Usage Example

### Instantiation

```python
from llama_index.tools.cloudsway import CloudswayToolSpec
import os

tool = CloudswayToolSpec(server_key=os.environ["CLOUDSWAY_SERVER_KEY"])
tool_list = tool.to_tool_list()
```

### Tool Parameters

| Name         | Type   | Required | Default  | Description                                                     |
| ------------ | ------ | -------- | -------- | --------------------------------------------------------------- |
| `query`      | string | Yes      | -        | Search keyword or question (e.g., "Latest advances in AI 2024") |
| `count`      | number | No       | 10       | Number of results to return (1-50, recommended 3-10)            |
| `offset`     | number | No       | 0        | Pagination offset (e.g., offset=10 means start from result #11) |
| `setLang`    | string | No       | "en"     | Language filter (e.g., "zh-CN", "en", "ja")                     |
| `safeSearch` | string | No       | "Strict" | Content safety level: "Strict", "Moderate", or "Off"            |

### Direct Invocation

```python
import asyncio

results = asyncio.run(
    tool.smartsearch(query="2024 global AI summit highlights", count=10)
)
print(results)
```

### Use with LlamaIndex Agent

```python
from llama_index.core.agent import FunctionCallingAgent
from llama_index.llms.openai import OpenAI

agent = FunctionCallingAgent.from_tools(
    tool_list,
    llm=OpenAI(model="gpt-4o"),
)

response = agent.chat(
    "Show me recent peer-reviewed papers about autonomous vehicles from arxiv.org."
)
print(response)
```

## Supported Components

- **SmartsearchTool**: Advanced web search tool for structured results.

## API Reference

See the [Cloudsway API reference](https://github.com/Cloudsway-AI/langchain-cloudsway) for full documentation on available features and configuration options.

---

Cloudsway empowers your LlamaIndex applications with real-time, safe, and customizable web search.
