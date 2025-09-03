from typing import List
from agents.mcp.server import MCPServer, MCPServerStdio, MCPServerSse
from .config import MCP_STDIO_CMD, MCP_STDIO_ARGS, MCP_SSE_URL, MCP_SSE_HEADERS

def build_mcp_servers() -> List[MCPServer]:
    """Build optional MCP servers from environment variables (stdio or SSE)."""
    servers: List[MCPServer] = []

    if MCP_STDIO_CMD:  # Local MCP server (e.g. filesystem)
        servers.append(MCPServerStdio(params={"command": MCP_STDIO_CMD, "args": MCP_STDIO_ARGS or []}))

    if MCP_SSE_URL:  # Remote HTTP(S) MCP server
        servers.append(MCPServerSse(params={"url": MCP_SSE_URL, "headers": MCP_SSE_HEADERS or {}}))

    return servers