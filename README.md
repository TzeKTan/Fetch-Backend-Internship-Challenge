# Project Name

Fetch Rewards Coding Exercise

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)

## Introduction

This is a REST API for keeping track of points and points transactions. It is built with Flask and Python.

## Features

- add_points(): Add points to a user's account, checks if the data is valid and returns a 200 status code if successful.
- deduct_points(): Deduct points from a user's account, checks if the data is valid and returns a list of subtracted 
payers with points subtracted and a 200 status code if successful.
- get_points(): Returns a list of all payers and their points.
## Installation

1. Python 3.9 is used for this project. Install Python 3.9 if you don't have it already.
2. Install Flask using `pip install flask`.
3. Run `python app.py` to start the server.
4. Use Postman to test the API.

