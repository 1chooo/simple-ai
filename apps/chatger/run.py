# -*- coding: utf-8 -*-
"""
Create Date: 2023/10/18
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
"""

import uvicorn


def main() -> None:
    uvicorn.run(
        app="Chatter.App.App:app",
        host="127.0.0.1",
        port=5002,
        reload=True,
    )


if __name__ == "__main__":
    main()
