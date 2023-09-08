'''
Create Date: 2023/08/25
Author: @VincentLi1216, @1chooo
Email: sunnus.tw@gmail.com
Version: v0.1.2
'''

import uvicorn

def main() -> None:
    uvicorn.run(
        app="Refinaid.App.app:app",
        host="127.0.0.1", 
        port=5002,
        reload=True,
    )

if __name__ == '__main__':
    main()
