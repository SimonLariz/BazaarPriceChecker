# Hypixel Bazaar Price Checker
Basic python program that fetches buy and sell values of all items sold by the Bazaar in the Hypixel Skyblock minigame. Additionally, the script calculates an optimal bid value which will cause anyone outbidding you to overpay for the item. The program requests all the data from the public hypixel API and exports it to an xlsx file.

### Prerequisites

- 2 API Keys (/api in-game on 2 different accounts) *2 keys are required as with only one key, the requests time out after about 100 items, a second key is needed to continue the request for the remaining ~100 items.
- Program that can open .xlsx files (excell)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Simply download the .py file and replace the "[[KEY]]" with your API keys. [[KEY 1]] is your first key and [[KEY 2]] is the second then simply run the .py file. 

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

[Simon Lariz](https://github.com/SimonLariz)

## Acknowledgments

* Thanks Hypixel
