Architecture diagram (text version for docs)

                 ┌──────────────────────────────┐
                 │   Supply Chain Simulator     │
                 │ (vineyard → bottle → retail) │
                 └───────────────┬──────────────┘
                                 │ events
                                 ▼
                                 
                 ┌──────────────────────────────┐
                 │       Blockchain Engine      │
                 │ (blocks, hashes, validation) │
                 └───────────────┬──────────────┘
                                 │ blocks
                                 ▼
                                 
                 ┌──────────────────────────────┐
                 │    Visual Mapping Layer      │
                 │ (event → visual parameters)  │
                 └───────────────┬──────────────┘
                                 │ JSON over WebSocket
                                 ▼
                                 
        ┌────────────────────────────────────────────────┐
        │                  Frontend (Web)                │
        │  ┌──────────────────────────────────────────┐  │
        │  │        Generative Art Renderer           │  │
        │  │   (p5.js / Three.js, 60 FPS visuals)     │  │
        │  └──────────────────────────────────────────┘  │
        │  ┌──────────────────────────────────────────┐  │
        │  │        UI Layer (Ledger + Timeline)      │  │
        │  └──────────────────────────────────────────┘  │
        └────────────────────────────────────────────────┘

