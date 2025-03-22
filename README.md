<div align="center">
    <h1 "><code>Telegram Bot Template</code></h1>
    <div>
        <a href="https://github.com/copier-org/copier">
            <picture>
               <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-black.json&style=for-the-badge&labelColor=010409&color=1e242a" />
               <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-black.json&style=for-the-badge&labelColor=010409&color=f0f1f2" />
               <img alt="Copier" />
             </picture>
        </a>
        <picture>
           <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/-Python 3.9 — 3.13-1e242a?style=for-the-badge&logoColor=white&labelColor=3776AB&logo=python" />
           <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/-Python 3.9 — 3.13-f0f1f2?style=for-the-badge&logoColor=white&labelColor=3776AB&logo=python" />
           <img alt="Python 3.9 - 3.13" />
         </picture>
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
uvx --with copier-templates-extensions copier copy --trust gh:TimNekk/copier-telegram-bot ~/path/to/your/project
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

#### Middlewares

- [x] [**`Dependency Injection`**](https://docs.aiogram.dev/en/latest/dispatcher/middlewares.html) 💉 Share tools/data across bot handlers
- [x] [**`Throttling`**](https://docs.aiogram.dev/en/latest/dispatcher/middlewares.html) 🛑 Stop spam with automatic speed limits
- [x] [**`Database Sessions`**](https://docs.sqlalchemy.org/en/20/orm/session_basics.html) ♻️ Auto-manage database connections
- [x] [**`Loguru`**](https://github.com/Delgan/loguru) 📜 Simple logging with colors and fun

#### Tooling

- [x] [**`Pydantic Settings`**](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) ✅ Safe config management with type checking
- [x] [**`Dynaconf`**](https://www.dynaconf.com/) ⚙️ Configs for dev/test/prod environments
- [x] [**`Ruff`**](https://docs.astral.sh/ruff/) 🪶 Super-fast code linting and cleanup
- [x] [**`Justfile`**](https://just.systems/) 🪄 Short commands for complex tasks
- [x] [**`Cache Decorator`**](https://pypi.org/project/orjson/) ⚡ Speed up functions with Redis caching

## 🔧 Prerequisites

Before using the **Copier Telegram Bot** template, ensure you have the following installed:

- **Copier**: Refer to the [installation guide](https://copier.readthedocs.io/en/latest/#installation).
- **Copier Templates Extensions**: Refer to the [repository](https://github.com/copier-org/copier-templates-extensions?tab=readme-ov-file#installation) for installation instructions.

## 📖 Usage

Once these prerequisites are installed, you're ready to use the template!

```bash
copier copy --trust gh:TimNekk/copier-telegram-bot ~/path/to/your/project
```

Copier will ask you a lot of questions. Answer them to properly generate the template.

## 🗺️ Roadmap

Help shape the future! Planned improvements:

- [ ] [**`Bot Internationalization`**](https://docs.aiogram.dev/en/latest/dispatcher/i18n.html) 🌐 Support multiple languages for global audiences
- [ ] [**`Prompts Internationalization`**](https://github.com/aiogram/aiogram) 📋 Translate copier prompts
- [ ] [**`Dependabot`**](https://github.com/dependabot) 🤖 Add dependencies auto-update to generated project for security and freshness
- [ ] [**`Testing`**](https://docs.pytest.org/) ✅ Add testing framework
- [ ] [**`Flake8`**](https://flake8.pycqa.org/) / [**`wemake`**](https://wemake-python-styleguide.readthedocs.io/en/latest/) 🧹 Alternative strict linting for code quality fans

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

First off, thanks for taking the time to contribute! Contributions are what makes the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. `Fork` this repository
2. Create a `branch`
3. `Commit` your changes
4. `Push` your `commits` to the `branch`
5. Submit a `pull request`

## 📝 License

Distributed under the Apache License 2.0. See [`LICENSE`](./LICENSE.md) for more information.
