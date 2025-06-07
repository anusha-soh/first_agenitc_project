# 30-Day OpenAI Project Challenge 🚀

## Project Overview
This repository documents my 30-day journey of building and improving a project using the OpenAI SDK. The goal is to create a portfolio-worthy project while building consistency, learning new skills, and applying knowledge in practical ways.


## 🎯 Goals
- Build a portfolio-worthy project
- Develop consistency in coding and learning
- Master the OpenAI SDK and its applications
- Document the learning journey
- Create something valuable for future career growth

## 🎯 Project Vision

Build an inventory management system where AI agents can:
- Track stock levels and suggest actions
- Auto-reorder items using rules or AI
- Generate daily/weekly reports
- Interact with a user interface or CLI for updates and decisions

## 📅 Daily Progress Log

### Day 1 - Project Setup
- Created initial project structure
- Set up README documentation
- Established project goals and milestones

### Day 2
- Selected project
- Installed dependencies
- Configure API key, set up .env 
- Created a simple agent

### Day 3
- Added exceptional hendling
- Make agent conversational through history 

### Day 4
- Added another file `streaming.py`
- Added streamed response in `streaming.py`(might make this one my main)

### Day 5
- Added simple tool to agent

## 🧩 Tech Stack

- **Frontend:** chainlit
- **Backend:** Python
- **AI/Agents:** OpenAI SDK
- **Database:** 
- **Deployment:** 

## General commands

- `uv init agent_01`
- `uv add openai-agents python-dotenv chainlit`
- `uv run main.py`
- `.venv\Scripts\activate`

    test if Chainlit working
- `uv run chainlit hello`

    run chinlit project
- `uv run chainlit run main.py -w`


## 📚 Learning Journal
This section will be updated daily with new learnings and insights.

### Day 1
- Initial project setup and documentation
- Planning the project structure
- Setting up version control

### Day 2
- Learn about basic inner working of `Runner` and `Agent` clsss.
- Learn about virtual environment.
- Understood how Chainlit's session memory works: you can store agents, config, and history to persist context between turns.

### Day 3
- Learned inner working on how openAI SDK context history through history and make chat conversational
- Explored how user messages are appended to history
- Tried to learn significance of doc strings
- Learned to apply typecasting through `typing` module

### Day 4
- Learned how `@cl.on_chat_start` and `@cl.on_message` act as entry points,one for session setup, the other for every user message.
- Explored how AI responses get streamed token-by-token for a smoother user experience.
- Learned that `cl.Message` isn't just for sending replies — it holds both incoming and outgoing messages.

### Day 5 
- explored the inner workings of Chainlit, custom AI agents, and how to handle streamed responses in a conversational AI app
-  Clarified key Python concepts `hasattr()`.

## 🎯 Project Milestones
- [ ] Project Setup and Planning
- [ ] Basic OpenAI Integration
- [ ] Core Features Implementation
- [ ] UI/UX Development
- [ ] Testing and Optimization
- [ ] Documentation and Deployment

## 🔄 Version History
- v0.1.0 - Initial project setup

## 📈 Future Plans
- [To be updated as we progress]

## 🤝 Contributing
While this is primarily a learning project, suggestions and feedback are welcome!

## 🌐 Links

- **GitHub Repo:** [link](#)
- **Live Demo:** [link](#)
- **LinkedIn Series:** [link](#)

## 📄 License
MIT – Use it, remix it, learn from it.

---
*This README will be updated daily to reflect the project's progress and learning journey.* 