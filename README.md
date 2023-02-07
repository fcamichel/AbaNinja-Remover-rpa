# AbaNinja-Remover-rpa
Visual Robotic Process Automation (RPA) to remove addresses in AbaNinja

## Idea
After several address imports (csv) I had the problem that I had to archive and delete all wrong imported addresses. In February 2023, bulk deletion of archived addresses was not possible in AbaNinja. Since I now would have had to delete over 1800 entries manually, I wrote this code without further ado.

## Requirements
* [RPA-Python](https://github.com/tebelorg/RPA-Python)
* [AbaNinja](http://app.abaninja.ch/) in German (otherwise change the two png images: menu and remove)

## Demo
![Animated Demo of the rpa project](/doc/Demo-blurred.gif)

## Usage
* Create virtual env (opt) 
* pip install -r requirements.txt
* Log into your AbaNinja account and open [archvided address list](http://app.abaninja.ch/addresses/archived)
* python main.py
* makes sure that the AbaNinja browser window is open and visible
