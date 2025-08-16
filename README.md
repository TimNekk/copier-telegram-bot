<div align="center">
    <h1><code>Telegram Bot Template</code></h1>
    <div>
        <a href="https://github.com/copier-org/copier">
            <picture>
                <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-black.json&style=for-the-badge&labelColor=010409&color=1e242a" />
                <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-black.json&style=for-the-badge&labelColor=010409&color=f0f1f2" />
                <img alt="Copier" />
            </picture>
        </a>
        <p/>
        <a href="https://www.python.org/">
            <picture>
                <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/-Python 3.9 — 3.13-1e242a?style=for-the-badge&logoColor=white&labelColor=3776AB&logo=python" />
                <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/-Python 3.9 — 3.13-f0f1f2?style=for-the-badge&logoColor=white&labelColor=3776AB&logo=python" />
                <img alt="Python 3.9 - 3.13" />
            </picture>
        </a>
        <a href="https://github.com/astral-sh/ruff">
            <picture>
                <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/-Linted by Ruff-1e242a?style=for-the-badge&logoColor=30173d&labelColor=D7FF64&logo=ruff" />
                <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/-Linted by Ruff-f0f1f2?style=for-the-badge&logoColor=30173d&labelColor=D7FF64&logo=ruff" />
                <img alt="Linted by Ruff" />
            </picture>
        </a>
        <a href="https://github.com/TimNekk/copier-telegram-bot/blob/main/LICENSE.md">
            <picture>
                <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/-Apache License 2.0-1e242a?style=for-the-badge&logoColor=1e242a&labelColor=white&logo=googledocs" />
                <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/-Apache License 2.0-f0f1f2?style=for-the-badge&logoColor=white&labelColor=1f2328&logo=googledocs" />
                <img alt="Apache License 2.0" />
            </picture>
        </a>
    </div>
</div>

## 🚀 Quickstart

Ensure [uv](https://docs.astral.sh/uv/getting-started/installation/) is installed, then create a new Telegram bot project with:

```bash
uvx --with copier-templates-extensions copier copy --trust -r HEAD gh:TimNekk/copier-telegram-bot ~/path/to/your/project
```

## ✨ Features

Built with [Copier](https://copier.readthedocs.io/), this template lets you toggle features during setup - choose what you need and generate files instantly! Ready for [Docker](https://www.docker.com/) 🐳 and [Coolify](https://coolify.io/) ☁️ deployment.

#### Core Infrastructure

- [x] [**`Docker Compose`**](https://docs.docker.com/compose/) 🐳 Launch bot + services with one command
- [x] [**`Python 3.9–3.13`**](https://www.python.org/) 🐍 Choose your Python version easily
- [x] [**`uv`**](https://docs.astral.sh/uv/) 🚀 Fast dependency management powered by Rust
- [x] [**`Poetry`**](https://python-poetry.org/) 📦 Manage dependencies safely with virtual environments
- [x] [**`pip`**](https://pip.pypa.io/) 📜 Classic Python package installer

#### Telegram Bot Framework

- [x] [**`Aiogram`**](https://docs.aiogram.dev/) ⚡ Modern async bot framework with state management
- [x] [**`Aiogram Dialog`**](https://github.com/Tishka17/aiogram_dialog) 🖼️ Create menus and interactive interfaces
- [x] [**`Redis`**](https://redis.io/) ❤️ Keep bot data safe between restarts

#### Database & ORM

- [x] [**`PostgreSQL`**](https://www.postgresql.org/) 🐘 Powerful database for complex projects
- [x] [**`SQLAlchemy`**](https://www.sqlalchemy.org/) 🛠️ Work with databases using Python code
- [x] [**`Alembic`**](https://alembic.sqlalchemy.org/) ⏳ Track and apply database changes easily
- [x] [**`User Table`**](./example/bot/database/models/user.py) 👤 id, username, first_name, last_name, etc

#### Middlewares

- [x] [**`Dependency Injection`**](https://docs.aiogram.dev/en/latest/dispatcher/middlewares.html) 💉 Share tools/data across bot handlers
- [x] [**`Throttling`**](https://docs.aiogram.dev/en/latest/dispatcher/middlewares.html) 🛑 Stop spam with automatic speed limits
- [x] [**`Database Sessions`**](https://docs.sqlalchemy.org/en/20/orm/session_basics.html) ♻️ Auto-manage database connections
- [x] [**`Loguru`**](https://github.com/Delgan/loguru) 📜 Simple logging with colors and fun
- [x] [**`User Register`**](./example/bot/middleware/user_register.py) 📝 Adds a user to the database on /start
- [x] [**`Callback Answer`**](https://docs.aiogram.dev/en/latest/utils/callback_answer.html) 🔄 Automatically answer callback queries

#### Tooling

- [x] [**`i18n`**](https://github.com/aiogram/i18n) 🌐 Multiple languages support
- [x] [**`Dependabot`**](https://github.com/dependabot) 🤖 Automatic dependency updates
- [x] [**`Pydantic Settings`**](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) ✅ Safe config management with type checking
- [x] [**`Dynaconf`**](https://www.dynaconf.com/) ⚙️ Configs for dev/test/prod environments
- [x] [**`Ruff`**](https://docs.astral.sh/ruff/) 🪶 Super-fast code linting and cleanup
- [x] [**`Justfile`**](https://just.systems/) 🪄 Short commands for complex tasks
- [x] [**`Cache Decorator`**](https://pypi.org/project/orjson/) ⚡ Speed up functions with Redis caching

## 📂 Project Structure

The **fully-featured** generated project can be found in the [example/](./example) directory.

Below is the folder structure of the generated project:

```sh
.
├── bot                          # Main directory for the bot's source code
│   ├── cache                    # Contains caching-related modules
│   │   ├── redis.py             # Module for Redis-based caching functionality
│   │   └── serialization.py     # Handles serialization and deserialization for cached data
│   │   
│   ├── core                     # Core components of the bot
│   │   ├── loader.py            # Initializes and loads core components of the bot
│   │   └── settings.py          # Configuration and settings for the bot
│   │   
│   ├── database                 # Database-related modules and models
│   │   ├── models               # Directory for database model definitions
│   │   │   ├── base.py          # Base class for database models
│   │   │   └── user.py          # User table model
│   │   └── database.py          # Database connection
│   │   
│   ├── dialogs                  # Dialog flow and interaction logic
│   │   └── example              # Example implementation of dialogs
│   │       ├── dialogs.py       # Defines dialogs
│   │       ├── getters.py       # Retrieves data required for dialogs
│   │       └── handlers.py      # Handles user interactions within dialogs
│   │   
│   ├── filters/                 # Custom filters for handling specific bot commands or messages
│   │   
│   ├── handlers                 # General handlers for bot events
│   │   └── start.py             # Handler for the /start command
│   │   
│   ├── keyboards                # Defines inline and reply keyboards for user interaction
│   │   ├── inline               # Inline keyboards
│   │   └── default_commands.py  # Default commands setup
│   │   
│   ├── middleware               # Middleware modules to extend bot behavior
│   │   ├── database.py          # Middleware to manage database interactions during events
│   │   ├── dependency.py        # Dependency injection middleware for shared resources
│   │   ├── logger.py            # Middleware to log events
│   │   ├── throttling.py        # Middleware to handle rate-limiting of requests
│   │   └── user_register.py     # Add user to DB on /start
│   │   
│   ├── services/                # Auxiliary services with business logic
│   │   └── user.py              # User CRUD and helpers
│   │   
│   ├── __main__.py              # Entry point to run the bot application
│   └── states.py                # FSM states
│   
├── locales                      # Translations (Fluent `.ftl` files)
│   └── en
│       └── LC_MESSAGES
│           └── bot.ftl          # English texts (add more locales similarly)
│   
├── migrations                   # Database migration files (managed by Alembic)
│   ├── versions/                # Directory containing individual migration scripts
│   │   └── add_users_table.py # Creates users table
│   ├── env.py                   # Alembic environment configuration file
│   └── script.py.mako           # Template for generating new migration scripts
│   
├── .dockerignore                # Specifies files and directories to ignore in Docker builds
├── .gitignore                   # Specifies files and directories to ignore in Git version control
├── .github
│   └── dependabot.yml           # Automatic dependency updates
├── .python-version              # Python version specification file for version managers like pyenv
├── .env                         # Environment variable settings file
├── .template.env                # Template file for environment variables
├── alembic.ini                  # Alembic configuration file for database migrations
├── compose.yaml                 # Docker Compose configuration file for multi-container setups
├── Dockerfile                   # Instructions to build a Docker image for the application
├── entrypoint.sh                # Script executed as the container's entry point 
├── justfile                     # Task runner configuration file (for `just` command automation)
├── pyproject.toml               # Python project metadata and dependencies configuration (PEP-518)
├── README.md                    # Documentation readme file describing the project
└── uv.lock                      # Lock file generated by a dependency manager
```

## 📖 Usage

Before using the **Copier Telegram Bot** template, ensure you have the following installed:

- **Copier**: Refer to the [installation guide](https://copier.readthedocs.io/en/latest/#installation)
- **Copier Templates Extensions**: Refer to the [repository](https://github.com/copier-org/copier-templates-extensions?tab=readme-ov-file#installation) for installation instructions

Once these prerequisites are installed, you're ready to use the template!

```bash
copier copy --trust -r HEAD gh:TimNekk/copier-telegram-bot ~/path/to/your/project
```

Copier will ask you a lot of questions. Answer them to properly generate the template.

## 🗺️ Roadmap

Help shape the future! Planned improvements:

- [ ] [**`Testing`**](https://docs.pytest.org/) ✅ Add testing framework
- [ ] [**`Flake8`**](https://flake8.pycqa.org/) / [**`wemake`**](https://wemake-python-styleguide.readthedocs.io/en/latest/) 🧹 Alternative strict linting for code quality fans
- [ ] [**`Admin Role`**](https://docs.aiogram.dev/en/latest/dispatcher/filters/index.html) 🔒 Add admin filter
- [ ] [**`Commands i18n`**](https://github.com/aiogram/aiogram_i18n) 🌐 Add i18n support for bot commands

*Got ideas? Star ⭐ the repo or open an issue to collaborate!* 🚀

## ⭐ Star History

<a href="https://star-history.com/#TimNekk/copier-telegram-bot&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=TimNekk/copier-telegram-bot&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=TimNekk/copier-telegram-bot&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=TimNekk/copier-telegram-bot&type=Date" />
 </picture>
</a>

## 👷 Contributing

- For a small change, just send a PR.
- For bigger changes open an issue for discussion before sending a PR.
- PR should have:
  - Test case
  - Documentation
  - Example (If it makes sense)

## 📝 License

Distributed under the Apache License 2.0. See [`LICENSE`](./LICENSE.md) for more information.
