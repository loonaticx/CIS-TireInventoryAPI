# CIS3368 Assignment 2: Tire Inventory API

Created by Erica Miller (2031854) for the Spring 2024 semester.

## Installation

This program was made with the SQLAlchemy, MySQL connector, and Flask packages.

Ensure you have the required dependencies downloaded by running the following command in this directory:

```
python -m pip install -r requirements.txt
```

## Usage

First, take a look at ``config/Config.py`` and check if the ``CONNECTION_MODE`` is what you intend.
The default value is ``REMOTE_SERVER``, which is the AWS server -- our final presenting database.
Other values such as ``LOCAL_FILE`` and ``LOCAL_MEMORY`` can be used for testing purposes.

Keep in mind that the program, including the utility and interface code, will interact with the database 
as determined by ``CONNECTION_MODE``.

To start the show, you can simply run:
```
python main.py
```

To generate arbitrary tires into the database, you can run the following:
```
python -m utils.TireGenerator
```

## Keywords

| Attribute Name | Description                                              | Data Type   |
|----------------|----------------------------------------------------------|-------------|
| _id_           | _Internal identifier; primary key._                      | _int_       |   |   |
| brand          | Brand of the tire                                        | String (64) |
| model          | Model associated with the branded tire                   | String (64) |
| loadRating     | How much weight the tire can support                     | Integer     |
| speedRating    | Letter that indicates the speed capabilities of the tire | String (1)  |
| itemType       | The type and usage of the tire                           | String (64) |
| stock          | The quantity availble to purchase                        | Integer     |

---

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/6tNZvTAw)
