# Hypixel Bazaar Price Checker
Basic python program that fetches buy and sell values of all items sold by Bazaar in the Hypixel Skyblock minigame. Additionally, the script calculates an optimal bid for the item which will cause the person outbidding you to over pay for the item. The program scrapes all the data from the public hypixel API and exports it to an xlsx file.

## Getting Started

These instructios will get you a copy of the project up and running on your local machine for development and testing purposes. Simply download the .py file and run it. 


### Prerequisites

- 2 API Keys (/api in-game on 2 different accounts) *2 keys are required as with one the request time out after about 100 items so a second is need to continue the request
- Program that can open .xlsx files (excell)

### Installing

Make sure the two required libraries are installed.
- requests
- xlsxwriter

```
pip install requests
```

And 

```
pip install xlsxwriter
```

## Authors

* **Simon Lariz ** - [Simon Lariz](https://github.com/SimonLariz)

## Acknowledgments

* Thanks Hypixel
