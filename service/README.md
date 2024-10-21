<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="center">
    <h1 align="center">WATCH-DATA-SERVICE</h1>
</p>
<p align="center">
    <em></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/serdaraltin/Watch-Data-Service?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/serdaraltin/Watch-Data-Service?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/serdaraltin/Watch-Data-Service?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/serdaraltin/Watch-Data-Service?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat&logo=tqdm&logoColor=black" alt="tqdm">
	<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=flat&logo=Jupyter&logoColor=white" alt="Jupyter">
	<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat&logo=Pydantic&logoColor=white" alt="Pydantic">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=flat&logo=Jinja&logoColor=white" alt="Jinja">
	<img src="https://img.shields.io/badge/SciPy-8CAAE6.svg?style=flat&logo=SciPy&logoColor=white" alt="SciPy">
	<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat&logo=OpenAI&logoColor=white" alt="OpenAI">
	<img src="https://img.shields.io/badge/Plotly-3F4F75.svg?style=flat&logo=Plotly&logoColor=white" alt="Plotly">
	<br>
	<img src="https://img.shields.io/badge/SymPy-3B5526.svg?style=flat&logo=SymPy&logoColor=white" alt="SymPy">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=flat&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy">
	<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat&logo=JSON&logoColor=white" alt="JSON">
	<img src="https://img.shields.io/badge/Flask-000000.svg?style=flat&logo=Flask&logoColor=white" alt="Flask">
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running Watch-Data-Service](#-running-Watch-Data-Service)
>   - [ Tests](#-tests)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

 `overview`

---

##  Features

 `features`

---

##  Repository Structure

```sh
└── Watch-Data-Service/
    ├── LICENSE
    ├── api
    │   └── __init__.py
    ├── app
    │   ├── __init__.py
    │   └── static
    │       └── swagger.json
    ├── app.py
    ├── config
    │   ├── __init__.py
    │   ├── config_manager.py
    │   └── jsons
    │       ├── app.json
    │       ├── auth.json
    │       ├── aws.json
    │       ├── cors.json
    │       ├── database.json
    │       ├── filesystems.json
    │       ├── logging.json
    │       ├── queue.json
    │       └── services.json
    ├── controller
    │   └── __init__.py
    ├── database
    │   ├── __init__.py
    │   ├── connector
    │   │   ├── __init__.py
    │   │   ├── connector_postgre.py
    │   │   └── connector_sqlite.py
    │   ├── controller
    │   │   └── __init__.py
    │   ├── interfaces
    │   │   └── __init__.py
    │   └── migrations
    │       └── __init__.py
    ├── docker
    │   ├── Docker-Compose.yaml
    │   └── Dockerfile
    ├── docs
    │   ├── README.md
    │   ├── notes
    │   │   ├── export_paramters.todo
    │   │   ├── notes
    │   │   └── response.example.json
    │   ├── requirements.txt
    │   └── swagger.json
    ├── interfaces
    │   └── __init__.py
    ├── logs
    │   └── __init__.py
    ├── models
    │   └── __init__.py
    ├── notification
    │   └── __init__.py
    ├── routes
    │   ├── __init__.py
    │   └── routes.py
    ├── script
    │   └── __init__.py
    ├── services
    │   ├── __init__.py
    │   └── camera
    │       └── video_face_blur.py
    ├── temp
    │   └── __init__.py
    ├── tests
    │   ├── __init__.py
    │   └── unit
    │       └── __init__.py
    ├── utils
    │   ├── __init__.py
    │   ├── archive
    │   │   ├── create_example_data.py
    │   │   ├── demo2.py
    │   │   ├── example_data_weekly.csv
    │   │   └── main.ipynb
    │   ├── aws
    │   │   └── s3.py
    │   ├── data_preprocessing.py
    │   ├── database
    │   │   └── get_data.py
    │   ├── export
    │   │   ├── create_pdf.py
    │   │   ├── raport_charts.py
    │   │   └── wd.jpg
    │   └── query.sql
    └── view
        ├── __init__.py
        ├── camera.py
        ├── data.py
        └── views.py
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                           | Summary                            |
| ---                                                                            | ---                                |
| [app.py](https://github.com/serdaraltin/Watch-Data-Service/blob/master/app.py) |  `app.py` |

</details>

<details closed><summary>services.camera</summary>

| File                                                                                                                   | Summary                                                        |
| ---                                                                                                                    | ---                                                            |
| [video_face_blur.py](https://github.com/serdaraltin/Watch-Data-Service/blob/master/services/camera/video_face_blur.py) |  `services/camera/video_face_blur.py` |

</details>

<details closed><summary>docs</summary>

| File                                                                                                    | Summary                                           |
| ---                                                                                                     | ---                                               |
| [requirements.txt](https://github.com/serdaraltin/Watch-Data-Service/blob/master/docs/requirements.txt) |  `docs/requirements.txt` |

</details>

<details closed><summary>utils</summary>

| File                                                                                                               | Summary                                                 |
| ---                                                                                                                | ---                                                     |
| [data_preprocessing.py](https://github.com/serdaraltin/Watch-Data-Service/blob/master/utils/data_preprocessing.py) |  `utils/data_preprocessing.py` |
| [query.sql](https://github.com/serdaraltin/Watch-Data-Service/blob/master/utils/query.sql)                         |  `utils/query.sql`             |

</details>

<details closed><summary>utils.database</summary>

| File                                                                                                    | Summary                                                |
| ---                                                                                                     | ---                                                    |
| [get_data.py](https://github.com/serdaraltin/Watch-Data-Service/blob/master/utils/database/get_data.py) |  `utils/database/get_data.py` |

</details>

<details closed><summary>utils.aws</summary>

| File                                                                                   | Summary                                     |
| ---                                                                                    | ---                                         |
| [s3.py](https://github.com/serdaraltin/Watch-Data-Service/blob/master/utils/aws/s3.py) |  `utils/aws/s3.py` |

</details>

<details closed><summary>utils.archive</summary>

| File                                                                                                                         | Summary                                                          |
| ---                                                                                                                          | ---                                                              |
| [demo2.py](https://github.com/serdaraltin/Watch-Data-Service/blob/master/utils/archive/demo2.py)                             |  `utils/archive/demo2.py`               |
| [create_example_data.py](https://github.com/serdaraltin/Watch-Data-Service/blob/master/utils/archive/create_example_data.py) |  `utils/archive/create_example_data.py` |
| [main.ipynb](https://github.com/serdaraltin/Watch-Data-Service/blob/master/utils/archive/main.ipynb)                         |  `utils/archive/main.ipynb`             |

</details>

<details closed><summary>utils.export</summary>

| File                                                                                                            | Summary                                                   |
| ---                                                                                                             | ---                                                       |
| [create_pdf.py](https://github.com/serdaraltin/Watch-Data-Service/blob/master/utils/export/create_pdf.py)       |  `utils/export/create_pdf.py`    |
| [raport_charts.py](https://github.com/serdaraltin/Watch-Data-Service/blob/master/utils/export/raport_charts.py) |  `utils/export/raport_charts.py` |

</details>

<details closed><summary>database.connector</summary>

| File                                                                                                                          | Summary                                                             |
| ---                                                                                                                           | ---                                                                 |
| [connector_sqlite.py](https://github.com/serdaraltin/Watch-Data-Service/blob/master/database/connector/connector_sqlite.py)   |  `database/connector/connector_sqlite.py`  |
| [connector_postgre.py](https://github.com/serdaraltin/Watch-Data-Service/blob/master/database/connector/connector_postgre.py) |  `database/connector/connector_postgre.py` |

</details>

<details closed><summary>routes</summary>

| File                                                                                        | Summary                                      |
| ---                                                                                         | ---                                          |
| [routes.py](https://github.com/serdaraltin/Watch-Data-Service/blob/master/routes/routes.py) |  `routes/routes.py` |

</details>

<details closed><summary>config</summary>

| File                                                                                                        | Summary                                              |
| ---                                                                                                         | ---                                                  |
| [config_manager.py](https://github.com/serdaraltin/Watch-Data-Service/blob/master/config/config_manager.py) |  `config/config_manager.py` |

</details>

<details closed><summary>config.jsons</summary>

| File                                                                                                            | Summary                                                   |
| ---                                                                                                             | ---                                                       |
| [auth.json](https://github.com/serdaraltin/Watch-Data-Service/blob/master/config/jsons/auth.json)               |  `config/jsons/auth.json`        |
| [cors.json](https://github.com/serdaraltin/Watch-Data-Service/blob/master/config/jsons/cors.json)               |  `config/jsons/cors.json`        |
| [queue.json](https://github.com/serdaraltin/Watch-Data-Service/blob/master/config/jsons/queue.json)             |  `config/jsons/queue.json`       |
| [logging.json](https://github.com/serdaraltin/Watch-Data-Service/blob/master/config/jsons/logging.json)         |  `config/jsons/logging.json`     |
| [filesystems.json](https://github.com/serdaraltin/Watch-Data-Service/blob/master/config/jsons/filesystems.json) |  `config/jsons/filesystems.json` |
| [database.json](https://github.com/serdaraltin/Watch-Data-Service/blob/master/config/jsons/database.json)       |  `config/jsons/database.json`    |
| [aws.json](https://github.com/serdaraltin/Watch-Data-Service/blob/master/config/jsons/aws.json)                 |  `config/jsons/aws.json`         |
| [services.json](https://github.com/serdaraltin/Watch-Data-Service/blob/master/config/jsons/services.json)       |  `config/jsons/services.json`    |
| [app.json](https://github.com/serdaraltin/Watch-Data-Service/blob/master/config/jsons/app.json)                 |  `config/jsons/app.json`         |

</details>

<details closed><summary>view</summary>

| File                                                                                      | Summary                                    |
| ---                                                                                       | ---                                        |
| [camera.py](https://github.com/serdaraltin/Watch-Data-Service/blob/master/view/camera.py) |  `view/camera.py` |
| [data.py](https://github.com/serdaraltin/Watch-Data-Service/blob/master/view/data.py)     |  `view/data.py`   |
| [views.py](https://github.com/serdaraltin/Watch-Data-Service/blob/master/view/views.py)   |  `view/views.py`  |

</details>

<details closed><summary>docker</summary>

| File                                                                                                            | Summary                                                |
| ---                                                                                                             | ---                                                    |
| [Dockerfile](https://github.com/serdaraltin/Watch-Data-Service/blob/master/docker/Dockerfile)                   |  `docker/Dockerfile`          |
| [Docker-Compose.yaml](https://github.com/serdaraltin/Watch-Data-Service/blob/master/docker/Docker-Compose.yaml) |  `docker/Docker-Compose.yaml` |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version x.y.z`

###  Installation

1. Clone the Watch-Data-Service repository:

```sh
git clone https://github.com/serdaraltin/Watch-Data-Service
```

2. Change to the project directory:

```sh
cd Watch-Data-Service
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running Watch-Data-Service

Use the following command to run Watch-Data-Service:

```sh
python main.py
```

###  Tests

To execute tests, run:

```sh
pytest
```

